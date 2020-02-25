# encoding: utf-8

mv fanfou/target/ ./
mv fanfou/.git ./
mv fanfou/.idea ./
mv fanfou/.mvn ./
tar -zcvf fanfou-$(date +"%Y%m%d").tar.gz fanfou/
mv fanfou-$(date +"%Y%m%d").tar.gz /c/zsxhome/forAICT/
mv target/ ./fanfou/
mv .git ./fanfou/
mv .mvn ./fanfou/
mv .idea ./fanfou/
echo "done"
