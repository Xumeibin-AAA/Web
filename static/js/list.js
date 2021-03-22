function list(data,n){
	debugger
	console.log(typeof(data))
	var arr = eval('(' + data + ')')
	console.log(typeof(arr))
	var l = 1;
	var div = document.getElementById("tb");
	//删除节点
	if(div.hasChildNodes()){
		div.innerHTML="";
	}
	//表头
	var tr = document.createElement("tr");
	var th = document.createElement("th");
	var text = document.createTextNode("序号");
	th.appendChild(text);
	tr.appendChild(th);
	var th = document.createElement("th");
	var text = document.createTextNode("小说名");
	th.appendChild(text);
	tr.appendChild(th);
	var th = document.createElement("th");
	var text = document.createTextNode("链接");
	th.appendChild(text);
	tr.appendChild(th);
	var th = document.createElement("th");
	var text = document.createTextNode("下载");
	th.appendChild(text);
	tr.appendChild(th);
	var th = document.createElement("th");
	var text = document.createTextNode("删除");
	th.appendChild(text);
	tr.appendChild(th);
	div.appendChild(tr);
	for(var i=0;i<arr.length;i++){
		if(arr[i].length>2){
			var book = arr[i];
			var div = document.getElementById("tb");

			
			var tr = document.createElement("tr");
			//第一列
			var td = document.createElement("td");
			var text = document.createTextNode((n-1)*10+i+1);
			l++;
			td.appendChild(text);
			tr.appendChild(td);
			//第二列
			var td = document.createElement("td");
			var text = document.createTextNode(book);
			td.appendChild(text);
			tr.appendChild(td);
			//第三列
			var td = document.createElement("td");
			var a = document.createElement("a");
			var url ="http://"+window.location.host;
			a.href = url+"/load" + "?name=" + book;
			var text1 = document.createTextNode(book);
			a.appendChild(text1);
			td.appendChild(a);
			tr.appendChild(td);
			//第四列
			var td = document.createElement("td");
			var a = document.createElement("a");
			a.href = "../../data/Novels/load/" + book + ".txt";
			a.download = book;
			var text = document.createTextNode("下载");
			a.appendChild(text);
			td.appendChild(a);
			tr.appendChild(td);
			div.appendChild(tr);
			//第四列
			var td = document.createElement("td");
			var a = document.createElement("a");
			a.href = "../../data/Novels/load/" + book + ".txt";
			a.download = book;
			var text = document.createTextNode("删除");
			a.appendChild(text);
			td.appendChild(a);
			tr.appendChild(td);
			div.appendChild(tr);
				
		}
		
	}
}

function title(book_name){
	//获取标题所在位置的div
	var book_name_div = document.getElementById("title");
	//新建h1标签
	var h1 = document.createElement("h1");
	//将book_name写入到文本中
	var text = document.createTextNode(book_name);
	//将文本载入到h1标签中
	h1.appendChild(text);
	//将h1载入到div中
	book_name_div.appendChild(h1);
}

function content(content_data){
	var  arr = content_data.split(", ")
	console.log(arr);
	for(var i=1;i<arr.length;i++){
		if(arr[i].length<50 && arr[i].length>3 ){
			var div_content = document.getElementById("content");
			var h4 = document.createElement("h4");
			//标题
			var text = document.createTextNode(arr[i].replace("'","").replace("'","").replace("&#39;","").replace("&#39;",""));
			h4.appendChild(text);
			div_content.appendChild(h4);
		}else{
			var div_content = document.getElementById("content");
			var h4 = document.createElement("h6");
			//正文
			var text = document.createTextNode("----"+arr[i].replace("'","").replace("'","").replace("&#39;","").replace("&#39;",""));
			h4.appendChild(text);
			div_content.appendChild(h4);
		}
	}
}

function img_list(data,n){
	debugger
	console.log(typeof(data))
	var arr = eval('(' + data + ')')
	console.log(typeof(arr))
	var l = 1;
	var div = document.getElementById("img");
	//删除节点
	if(div.hasChildNodes()){
		div.innerHTML="";
	}
	console.log(n);
	var number=0;
	for(var i=0;i<Math.ceil(arr.length/5);i++){
		var tr = document.createElement("tr");
		for(var j=0;j<5;j++){
			var td = document.createElement("td");
			var a = document.createElement("a");
			var img = document.createElement("img");
			if(arr[number]==undefined ){
				tr.appendChild(td);
				div.appendChild(tr);
			}else{
				img.src='../../data/Image/'+ arr[number]+".gif"
				a.href='../../data/Image/'+arr[number++]+'.gif'
				a.appendChild(img);
				td.appendChild(a);
				tr.appendChild(td);
				div.appendChild(tr);
			}
		}
	}	
}
function video_list(data,n){
	debugger
	console.log(typeof(data))
	var arr = eval('(' + data + ')')
	console.log(typeof(arr))
	var l = 1;
	var div = document.getElementById("video");
	//删除节点
	if(div.hasChildNodes()){
		div.innerHTML="";
	}
	console.log(n);
	var number=0;
	for(var i=0;i<Math.ceil(arr.length/5);i++){
		var tr = document.createElement("tr");
		for(var j=0;j<5;j++){
			var td = document.createElement("td");
			var a = document.createElement("a");
			var img = document.createElement("img");
			img.src='../../data/Image/'+ arr[number]+".gif"
			a.href='../../data/image/'+arr[number++]+'.gif'
			a.appendChild(img);
			td.appendChild(a);
			tr.appendChild(td);
			div.appendChild(tr);
		}
	}	
}