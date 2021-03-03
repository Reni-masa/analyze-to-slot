$(function() {

    // 
    const class_list = $(".set_class")
    for (let i = 0; i < class_list.length; i++) {
        var class_value = class_list[i].innerText
        if (class_value === "6") {
            $(class_list[i]).css('background-color',"#FF3333")
        }
        if (class_value === "") {
            $(class_list[i]).text("0")
        }
    }
    // 
    $('#select_font-size').change(function() {
        // 選択されているvalue属性値を取り出す
        var val = $(this).val();
        // console.log(val); // 出力：ABC
        $('table').css('font-size',val);
    });
});
