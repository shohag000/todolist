$(document).ready(function(){
    // to do text-decoration line-through
    var checkboxesToChangeStyle =  $(".chk");
    var totalTask = checkboxesToChangeStyle.length
    var count = 0;
    $.each(checkboxesToChangeStyle, function(index, value){
      var thisCheckbox = $(this);

      if ($(this).prop("checked")== true){
        count++;
        thisCheckbox.parent().find(".inputval").css("text-decoration","line-through");
      };
    });

    // to show amount of completed task from total task
    var completedTaskHtml =  $("#amountCompleted");
    completedTaskHtml.text(count + " of "+ totalTask + " tasks done" );


    // delete task
    var deletebtns =  $(".deletebtn");
    deletebtns.click(function(){
        var deletebtn = $(this);
        var todoid = deletebtn.parent().find(".chk").val();
        console.log(" delete button clicked ");
        console.log(todoid);
        $.ajax({
                url: "/todo/delete_task/",
                method: "GET",
                data: {
                "id" : todoid,
                },
                success: function(data){
                    console.log(data.msg);
                    $("#bd").load(window.location.href);
                },
                error: function(errorData){

                },
        });
    });


    // edit task
    var editButtons =  $(".editbtn");
    editButtons.click(function(){
        var thisEditButton = $(this);
        thisEditButton.parent().find(".inputval").attr("disabled",false);
    });



    // list update
    var listupdateForm= $(".updateList");
    listupdateForm.submit(function(event){
        event.preventDefault();
        var thisForm = $(this);
        var formDataId = thisForm.find(".chk").val();
        var formDataTaskDesc = thisForm.find(".inputval").val();
        $.ajax({
            url: "/todo/edit_task/",
            method: "GET",
            data: {
            "id" : formDataId,
            "description" : formDataTaskDesc,
            },
            success: function(data){
                $("#bd").load(window.location.href);
            },
            error: function(errorData){

            },
        });
    });



    // checkbox checked or uncheck related
    var checkboxes =  $(".chk");
    checkboxes.change(function(){
    var checkbox = $(this);
    if ($(this).prop("checked")== true){
    checkbox.parent().find(".inputval").css( "text-decoration", "line-through" );
    checkbox.parent().find(".editbtn").attr("disabled",true);

    // increasing completed task when checkbox is checked
    count= count+1;
    completedTaskHtml.text(count + " of "+ totalTask + " tasks done");

    console.log("Checked");
    console.log(checkbox.val());
    $.ajax({
            url: "/todo/make_complete/",
            method: "GET",
            data: {
            "id" : checkbox.val(),
            },
            success: function(data){
                console.log(data.msg);
            },
            error: function(errorData){

            },
    });
    }
    else {
    checkbox.parent().find(".inputval").css( "text-decoration", "none" );
    checkbox.parent().find(".editbtn").attr("disabled",false);

    // decreasing completed task when checkbox is unchecked
    count= count-1;
    completedTaskHtml.text(count + " of "+ totalTask + " tasks done");

    $.ajax({
            url: "/todo/make_uncomplete/",
            method: "GET",
            data: {
            "id" : checkbox.val(),
            },
            success: function(data){
                console.log(data.msg);

            },
            error: function(errorData){

            },
    });
    console.log("Unchecked");
    };

    });

    });