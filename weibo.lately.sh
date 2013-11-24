
mkdir -p weibo

for file in $(ls -t txt_cn/*.txt | sed 's/^.*\///g' | head)
do
    ./freq_hanzi.py txt_cn/$file > $file.wf
    ./weibo.hanzi.py txt_cn/$file > ./weibo/$file.htm
done

