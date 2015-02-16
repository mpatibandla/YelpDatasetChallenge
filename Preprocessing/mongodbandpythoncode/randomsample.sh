if [ -f $3 ]
then
echo " file exist already . so deleting it "
rm $3
fi

count=1;
echo $count
while read line
do
    echo $count
    egrep "$line" $2 >> $3	
    count=`expr $count + 1`
done < $1
echo $count

