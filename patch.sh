#!/bin/bash

FONTS=/mnt/c/Windows/Fonts
# URL of the latest release
url="https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip"
fontMergeUrl="https://github.com/nowar-fonts/Warcraft-Font-Merger/releases/download/v1.1.0/WarFontMerger-SC-1.1.0-windows-x64.7z"

function die {
  echo "$1"
  exit 1
}

tmp=$(mktemp -d)
if [ ! -e $tmp ]; then
  die "failed to create tempdir"
fi

cp $FONTS/consola* $tmp
curl -fsSL --retry 5 --retry-all-errors "$url" -o FontPatcher.zip
curl -fsSL --retry 5 --retry-all-errors "$fontMergeUrlurl" -o WarFontMerger.zip
unzip FontPatcher.zip
unzip WarFontMerger.zip

for font in $tmp/consola*; do
  echo "patching $font"
  fontforge --script font-patcher "$font" --quiet --no-progressbars --complete -out consolas
done
