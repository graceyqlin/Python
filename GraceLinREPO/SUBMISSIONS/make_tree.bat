
if EXIST week_01. (
	del week_01.)
mkdir week_01\s1\s3
type nul. > week_01\s1\s3\conf.txt
echo I love bash scripting >> week_01\s1\s3\conf.txt
mkdir week_01\s1\s2
type nul. > week_01\s1\s2\text_chunk1.txt
echo A whole new world >> week_01\s1\s2\text_chunk1.txt
echo A new fantastic point of view >> week_01\s1\s2\text_chunk1.txt
mkdir week_01\s1\s2\Advanced
type nul. > week_01\s1\s2\Advanced\text_chunk2.txt
type week_01\s1\s2\text_chunk1.txt >> week_01\s1\s2\Advanced\text_chunk2.txt
echo Do you want to build a snow man >> week_01\s1\s2\Advanced\text_chunk2.txt
