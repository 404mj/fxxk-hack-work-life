// 网大答案获取脚本
var examId=window.location.href.split('/').pop();
$.get(`https://wangda.chinamobile.com/api/v1/exam/exam/front/exam-paper?examId=${examId}`,function(result){
    $.get(`https://wangda.chinamobile.com/api/v1/exam/exam/score-detail?examRecordId=${result.examRecord.id}&examId=${examId}&paperInstanceId=${result.examRecord.paperInstanceId}`
    ,function(obj){
        var questions=obj.paper.questions;
        var ans=[];
        for(var i=0;i<questions.length;i++){
            var _obj={};
            _obj.content=questions[i].content
            _obj.questionAttrCopys=[]
            for(var j=0;j<questions[i].questionAttrCopys.length;j++){
                if(questions[i].questionAttrCopys[j].type=="0"){
                    if(questions[i].questionAttrCopys[j].name=="0"){
                        _obj.questionAttrCopys.push("A:"+questions[i].questionAttrCopys[j].value);
                    }
                    if(questions[i].questionAttrCopys[j].name=="1"){
                        _obj.questionAttrCopys.push("B:"+questions[i].questionAttrCopys[j].value);
                    }
                    if(questions[i].questionAttrCopys[j].name=="2"){
                        _obj.questionAttrCopys.push("C:"+questions[i].questionAttrCopys[j].value);
                    }
                    if(questions[i].questionAttrCopys[j].name=="3"){
                        _obj.questionAttrCopys.push("D:"+questions[i].questionAttrCopys[j].value);
                    }
                }
                if(_obj.questionAttrCopys.length==0&&questions[i].questionAttrCopys[j].value=="0"){
                    _obj.questionAttrCopys.push("错误");
                }
                if(_obj.questionAttrCopys.length==0&&questions[i].questionAttrCopys[j].value=="1"){
                    _obj.questionAttrCopys.push("正确");
                }
            }
        if(_obj.questionAttrCopys.length==4){
            _obj.questionAttrCopys=['全选']
        }
ans.push(_obj)
}

console.log(JSON.stringify(ans,null,2))})})
