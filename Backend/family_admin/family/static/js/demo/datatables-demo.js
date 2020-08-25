// Call the dataTables jQuery plugin

$(document).ready(function() {
  $('#dataTable').DataTable( {
      "language": {
          "lengthMenu": "Mostrar _MENU_ entradas",
          "zeroRecords": "No se ha encontrado nada - :c",
          "info": "Mostrar página _PAGE_ de _PAGES_",
          "infoEmpty": "No encontrado",
          "infoFiltered": "(filtrado de _MAX_ en total)",
          "search": "Buscar:",
          "paginate": {
              "previous":   "Anterior",
              "next":       "Siguiente",
          },

      }
  } );
} );

// $(document).ready(function() {
//     // messages timeout for 10 sec 
//     setTimeout(function() {
//         $('.message').fadeOut('slow');
//     }, 10000); // <-- time in milliseconds, 1000 =  1 sec

//     // delete message
//     $('.del-msg').live('click',function(){
//         $('.del-msg').parent().attr('style', 'display:none;');
//     })
// });

var count_image = 0;
$('#addimg').click(function(){
    var div_image    = $('#image');
    if(count_image<3){
        var clone = div_image.clone();
        var child = clone.children();
        child.children().attr('id',count_image);
        child.children().attr('name',"image_"+count_image);
        // clone.find(':text').val('');
        // clone.find('[type=number]').val('');
        // clone.attr('value', parseInt(clone.attr('value'))+1);
        $('#image').before(clone);
        count_image++;
    }
});

var count_video = 0;
$('#addvideo').click(function(){
    var div_video    = $('#video');
    if(count_video<3){
        var clone = div_video.clone();
        var child = clone.children();
        child.children().attr('id',count_video);
        child.children().attr('name',"video_"+count_video);

        console.log(clone.children()[1]);
        // clone.find(':text').val('');
        // clone.find('[type=number]').val('');
        // clone.attr('value', parseInt(clone.attr('value'))+1);
        $('#video').before(clone);
        count_video++;
    }
});