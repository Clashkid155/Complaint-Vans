
// $(document).ready(function () {
//   $("#Test").click(function (event) {
//     alert(event.target.id);
//     $("#py1").toggle();
//   });
// });

$(document).ready(function () {
  $('button[data-select="form-button"]').each(function () {
    let buttonId = $(this).data('id')
    console.log(this, buttonId)
    $(this).bind('click', function () {
      console.log('clicked')
      $(`form[data-select="form"][data-id="${buttonId}"]`).each(function () {
        console.log('to toggle', this)
        $(this).toggle();
      });
    });
  });
});


// $(document).ready(function () {
//   $("button.py").each(function () {
//     $(this).bind('click', function () {
//       $("form.p-3").each(function () {
//         $(this).toggle();
//       });
//     });
//   });
// });

//$(document).ready(function() {
//    $("div.pyy").html('<button id="Test" class="py" type="button" onclick="Openform()";><ion-icon size="large" name="create"></ion-icon></button>');
//    $(document).on("click", "button.py", function(e) {
//        alert("Button was clicked "+ e.id);
//        $("form.p-3").each( function() {
//            $(this).toggle();
//        });
//    });
//});

//function Openform()
//{
//    alert(this.length);
//    var x = document.getElementById('py1');
//    //var x = document.getElementsByClassName("form.p-3");
//    var i;
//    for (i = -1; i < x.length; i++) {
//        x[i].style.display = '';
//       // alert("Hi");
//    }
//}
