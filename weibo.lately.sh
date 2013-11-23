
mkdir -p weibo

for file in $(ls -t *.wf | head)
do
    ./weibo.hanzi.py $file > ./weibo/$file.htm
done

