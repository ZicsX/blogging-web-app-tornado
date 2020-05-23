$(document).ready(function(){
    $('.i_title').click(function(){
        url = this.attributes["u"].value;
        art.ajax(url);
        ld.layout(true);
    });
});

var art = {};
art.ajax = function(url){
    $.ajax({
        url:"/api/article/"+url,
        type:"get",
        dataType: "json",
        success:function(data){
            art.data(data);
        },
        error:function(){
            alert("error");
        }
    });
};


art.data = function(data){
    var section = document.createElement('section');
    var div = document.createElement('div');
    var h1 = document.createElement('h1');
    $("#content").empty().append(section);
    section.className="post";
    div.className = "date";
    div.innerHTML = data.article['created'];
    h1.innerHTML = data.article['title'];
    $("#content>section").append(div,h1,data.article['content']);
    if(data.comments.length>0){
        $(".main").append(comments.listlayout(data.comments));
    }
    var comment = $("<div id='comm' class='block'>");
    $(".main").append(comment);
    $('#comm').append(comments.getlayout(data.article['aid']));
    ld.layout(false);
};

var ld = {};
ld.layout = function(bool){
    if(bool == true){
        var lodediv = document.createElement('div');
        var div = document.createElement('div');
        lodediv.appendChild(div);
        lodediv.className="ball-scale";
        $('.main').append(lodediv);
    }else{
        $('.ball-scale').remove();
    }
};

var comments = {};

comments.getlayout = function(aid){
    form = $("<form id='commentform'><h3>Add Comments</h3></form>");
    aidinput = $("<input type='hidden' name='aid' />");
    aidinput.attr('value',aid);
    nameinput = $("<input type='text' name='username' placeholder='Username'/>");
    emailinput = $("<input type='email' name='email' placeholder='Email'/>");
    urlinput = $("<input type='url' name='url' placeholder='Subject'/>");
    content = $("<textarea type='text' name='content' placeholder='Message Box'></textarea>");
    submitbtn = $("<button type='button' class='btn' onclick='comments.submit();'>Submit</button>");
    form.append(aidinput);
    form.append(nameinput);
    form.append(emailinput);
    form.append(urlinput);
    form.append(content);
    form.append(submitbtn);
    return form;
};
comments.submit = function(){
    from = $("#commentform").serialize();
    $.ajax({
        url:"/api/comment",
        data:$("#commentform").serialize(),
        type:"post",
        dataType: "json",
        success:function(data){
            if(data.msg['status']=="bad"){
                alert(data.msg['msg']);
                return;
            }
            alert(data.msg['status']);
            var llayout = comments.listlayout(data.comments);
            comments.redrawListLayout(llayout);
        },
        error:function(){
            alert("error");
        }
    });
};

comments.listlayout = function(comlist){
    var llayout = $("<div id='commentslist' class='block'><h3>Comments</h3>");
    for(var item in comlist){
        var c_item = $("<div class='c_item'></div>");
        var c_info = $("<div class='c_info'></div>");
        var c_content = $("<div class='c_content'></div>");
        var author = $("<span class='uname'></span>");
        var timestamp = $("<span class='timestamp'></span>");
        author.html(comlist[item].author);
        timestamp.html(comlist[item].created);
        c_info.append(author,timestamp);
        var c_content = $("<div class='c_content'></div>");
        c_content.html(comlist[item].content);
        c_item.append(c_info);
        c_item.append(c_content);
        llayout.append(c_item);
    }
    return llayout;
};
comments.redrawListLayout = function(llayout){
    //Remove
    $('#commentslist').remove();
    //Insert
    $('#comm').before(llayout);
    //Empty
    $('#commmentform').reset();
};