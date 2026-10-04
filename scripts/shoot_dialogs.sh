#!/usr/bin/env bash
# Renders the dialog screenshots of an ABBA release into docs/source/assets/dialogs/.
#
# The dialogs are painted offscreen by the scijava-screenshots tool (ShotCommands.java), from
# the released ImageToAtlasRegister artifact, never from a local checkout (which is usually a
# SNAPSHOT ahead of the documented release).
#
# Usage:
#   scripts/shoot_dialogs.sh <version> [extra Class=slug,...]
#
# Shoots every Class=slug line of cli-outputs/<version>/dialogs.txt (written by
# scripts/build_menu_reference.py), plus the optional extra list.
#
# Environment (defaults fit the maintainer's Windows machine):
#   JAVA_HOME      a JDK 21
#   SHOT_TOOL      path to ShotCommands.java
#   WORK_DIR       scratch folder for the throwaway Maven project and compiled classes
#   SHOT_THEME     dark (default) | light
set -euo pipefail

VERSION="${1:?usage: scripts/shoot_dialogs.sh <version> [extra Class=slug,...]}"
EXTRA="${2:-}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
: "${JAVA_HOME:=$USERPROFILE/.jdks/ms-21.0.11}"
: "${SHOT_TOOL:=$USERPROFILE/.claude/skills/scijava-screenshots/ShotCommands.java}"
: "${WORK_DIR:=${TMPDIR:-/tmp}/abba-dialog-shots-$VERSION}"
: "${SHOT_THEME:=dark}"
export JAVA_HOME PATH="$JAVA_HOME/bin:$PATH"
SEP=';'; [[ "$(uname -s)" == MINGW* || "$(uname -s)" == MSYS* ]] || SEP=':'

mkdir -p "$WORK_DIR"
cat > "$WORK_DIR/pom.xml" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>local</groupId><artifactId>abba-dialog-shots</artifactId><version>0</version>
  <repositories><repository><id>scijava.public</id><url>https://maven.scijava.org/content/groups/public</url></repository></repositories>
  <dependencies>
    <dependency><groupId>ch.epfl.biop</groupId><artifactId>ImageToAtlasRegister</artifactId><version>$VERSION</version></dependency>
    <dependency><groupId>com.formdev</groupId><artifactId>flatlaf</artifactId><version>3.6.1</version></dependency>
  </dependencies>
</project>
EOF

cd "$WORK_DIR"
mvn -B -q dependency:build-classpath -Dmdep.outputFile=cp.txt
CP="$(tr '\\' '/' < cp.txt)"
printf -- '-cp "%s"\n' "$CP" > args.txt
javac -nowarn @args.txt -d shot-classes "$SHOT_TOOL"
printf -- '-cp "shot-classes%s%s"\n' "$SEP" "$CP" > runargs.txt

ONLY="$(paste -sd, "$ROOT/cli-outputs/$VERSION/dialogs.txt" | tr -d '[:cntrl:]')"  # tr: drop Windows line ends
[[ -n "$EXTRA" ]] && ONLY="$ONLY,$EXTRA"

# ABBA's logging ignores scijava.log.level: keep only the tool's own OK / FAIL lines.
java -Dscijava.log.level=error --add-opens=java.base/java.lang=ALL-UNNAMED @runargs.txt ShotCommands \
     --out "$ROOT/docs/source/assets/dialogs" --theme "$SHOT_THEME" --scale 2 --only "$ONLY" 2> shots.log \
  | grep -E '^(OK|FAIL)' || true
