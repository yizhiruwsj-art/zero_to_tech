function changeText() {
    // document用于访问网页的 DOM，console用于在浏览器的控制台输出信息,window.alert用于弹出提示框
    console.log('按钮被点击了！');
    document.getElementById('msg').textContent = '你刚刚触发了一段 JavaScript。';
    window.alert("你好");
}