
//https://blog.csdn.net/u010895119/article/details/77186159
//执行在chrome console中, 用于计算某个楼盘租房价格平均数

num=parseInt($x('//*[@id="content"]/div[1]/p/span[1]')[0].innerText);
sum=Number(0);
elePathPre='//*[@id="content"]/div[1]/div[1]/div[';
elePathSuff=']/div/span/em';

for(var i=1;i<=15;++i){
    var elePath=elePathPre+i+elePathSuff;
    price=$x(elePath)[0].textContent;
//    console.log(price);
    sum+=parseInt(price);
}
console.log(sum/num);





