#!/usr/bin/env bash

version="2.0"
help="PS2 Icon Maker v$version

Usage: ps2iconmaker <gameid> [-t icon type] [-?]

[-t icon type]: type of icon to generate
                1 - PS2 DVD NTSC case
                2 - PS2 DVD PAL case
                3 - PS1 CD USA case
                4 - PS1 CD USA Greatest Hits case
                5 - PS1 JPN case
                6 - PS1 PAL case
                7 - PS1 multi-disc case
[-?]: shows this help

If an icon type is not given, a PS2 DVD NTSC case icon will be generated"

template_path="./assets/Icon-templates"
image_path="./icons/ico/tmp"

if [ -z $1 ]; then
  echo "$help"
  exit 0
else
  input="$1"
fi

while [[ $# -gt 0 ]]; do
  case $1 in
    -t)
      type="$2"
      shift
      ;;
    -?)
      echo "$help"
      exit 0
      ;;
    *)
      args+=("$1")
      shift
      ;;
  esac
done

case $type in
  1)
    icon="${template_path}/ps2dvdicon.icn"
    template="${template_path}/PS2-NTSC.bmp"
    ;;
  2)
    icon="${template_path}/ps2dvdicon.icn"
    template="${template_path}/PS2-PAL.bmp"
    ;;
  3)
    icon="${template_path}/ps1cdusicon.icn"
    template="${template_path}/PS1-USA.bmp"
    ;;
  4)
    icon="${template_path}/ps1cdusicon.icn"
    template="${template_path}/PS1-USA-GH.bmp"
    ;;
  5)
    icon="${template_path}/ps1cdpaljpicon.icn"
    template="${template_path}/PS1-JPN.bmp"
    ;;
  6)
    icon="${template_path}/ps1cdpaljpicon.icn"
    template="${template_path}/PS1-PAL.bmp"
    ;;
  7)
    icon="${template_path}/ps1multidiscicon.icn"
    template="${template_path}/PS1-MULTI.bmp"
    ;;
  *)
    type="1"
    icon="${template_path}/ps2dvdicon.icn"
    template="${template_path}/PS2-NTSC.bmp"
    ;;
esac

if ! command -v convert > /dev/null 2>&1 ; then
  echo "convert not found."
  exit 1
fi

if [ "$type" -eq 1 ] || [ "$type" -eq 2 ]; then
  convert $template \
    \( "${image_path}/${input}_COV.png" -resize 63x90\! \) -geometry +0+2 -composite \
    \( "${image_path}/${input}_COV2.png" -resize 63x90\! \) -geometry +65+2 -composite \
    \( "${image_path}/${input}_LAB.png" -resize 7x90 -rotate 90 \) -geometry +20+98 -composite \
    "${image_path}/temp.bmp" > /dev/null 2>&1
elif [ "$type" -eq 3 ] || [ "$type" -eq 4 ]; then
  convert $template \
    \( "${image_path}/${input}_COV.png" -resize 62x62\! \) -geometry +8+1 -composite \
    \( "${image_path}/${input}_COV2.png" -resize 69x63\! \) -geometry +1+64 -composite \
    \( "${image_path}/${input}_LAB.png" -resize 4x63\! \) -geometry +93+58 -composite \
    "${image_path}/temp.bmp" > /dev/null 2>&1
elif [ "$type" -eq 5 ] || [ "$type" -eq 6 ]; then
  convert $template \
    \( "${image_path}/${input}_COV.png" -resize 62x62\! \) -geometry +8+1 -composite \
    \( "${image_path}/${input}_COV2.png" -resize 69x63\! \) -geometry +1+64 -composite \
    \( "${image_path}/${input}_LAB.png" -resize 6x63\! \) -geometry +93+58 -composite \
    "${image_path}/temp.bmp" > /dev/null 2>&1
elif [ "$type" -eq 7 ]; then
  convert $template \
    \( "${image_path}/${input}_COV.png" -resize 69x62\! \) -geometry +1+1 -composite \
    \( "${image_path}/${input}_COV2.png" -resize 69x62\! \) -geometry +1+64 -composite \
    \( "${image_path}/${input}_LAB.png" -resize 4x62\! \) -geometry +71+1 -composite \
    \( "${image_path}/${input}_LAB.png" -resize 4x62\! \) -geometry +78+1 -composite \
    \( "${image_path}/${input}_LAB.png" -resize 4x62\! \) -geometry +71+64 -composite \
    \( "${image_path}/${input}_LAB.png" -resize 4x62\! \) -geometry +79+64 -composite \
    "${image_path}/temp.bmp" > /dev/null 2>&1
fi

convert "${image_path}/temp.bmp" \
  -flip \
  -separate +channel \
  -swap 0,2 \
  -combine \
  -alpha off \
  -define bmp:format=bmp4 \
  -define bmp:subtype=RGB555 \
  "${image_path}/temp.bmp"

dd bs=1 if="${image_path}/temp.bmp" of="${image_path}/temp.tex" skip=138 count=32768 iflag=skip_bytes,count_bytes > /dev/null 2>&1 &&

cat "$icon" "${image_path}/temp.tex" > "${image_path}/$input.ico"

if [ -s "${image_path}/$input.ico" ]; then
  rm "${image_path}/temp.bmp" "${image_path}/temp.tex"
  echo
  echo "Icon created sucessfully!"
  exit 0
else
  echo
  echo "Error: failed to create icon for $input."
  exit 1
fi