estado="suma"
function set_estado_reloj(valor) {
    estado=valor
}

function suma_tiempo(){
        minutos_actual=$("#minutos").html()
        segundos_actual=$("#segundos").html()
        var timer = setInterval(function(){
             
            var estado = $("#estado").html()
          
            
            if (segundos_actual==0){
                minutos_actual--
                segundos_actual=60
            }
            if (estado!='detenido') {
                segundos_actual--
            } else if ( estado=='detenido'){
                clearInterval(timer)
            }
            

            if  (segundos_actual<10) {
                $("#segundos").html('0'+segundos_actual)
            }
            else
            {
                $("#segundos").html(segundos_actual)
            }
            if  (minutos_actual<10) {
                $("#minutos").html('0'+minutos_actual)
            }
            else
            {
                $("#minutos").html(minutos_actual)
            }
        
            
        }, 1000);  
}
 



$(document).ready(function(){
    set_estado_reloj("cero")
     
    $(".op2").hide()

    
    
    $( "#adelante" ).click(function() {$("#estado").html("suma");suma_tiempo()});
    $( "#atras" ).click(function() {$("#estado").html("resta")});
    $( "#detiene" ).click(function() {$("#estado").html("detenido");});

    $(".btn_cami").click(function(){ $("#acciones").slideDown();});
    $("#btn_lanzamientos").click(function(){ $("#lanzamientos").slideDown();});
    $("#btn_tapones").click(function(){ $("#tapones").slideDown();});
    $("#btn_asistencias").click(function(){ $("#asistencias").slideDown();});
    $("#btn_perdidas").click(function(){ $("#perdidas").slideDown();});
    $("#btn_faltas").click(function(){ $("#faltas").slideDown();});

    $(".btn_lanza").click(function(){ valor=$(this).attr("data"); $("#lanzamientos").slideUp();});
    $(".btn_tapon").click(function(){ valor=$(this).attr("data"); $("#tapones").slideUp();});
    $(".btn_asistencia").click(function(){ valor=$(this).attr("data"); $("#asistencias").slideUp();});
    $(".btn_perdidas").click(function(){ valor=$(this).attr("data"); $("#perdidas").slideUp();});
    $(".btn_faltas").click(function(){ valor=$(this).attr("data"); $("#faltas").slideUp();});
 
    $("#cancha").click(function(e) {
       
        var offset = $(this).offset();
        // alert(e.pageX - offset.left);
        // alert(e.pageY - offset.top);
        $("#acciones").slideDown();
        
    });
 
});