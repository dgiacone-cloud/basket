estado="suma"
function set_estado_reloj(valor) {
    estado=valor
}
function suma_tiempo(){
    var estado = $("#estado").html()
    var minutos=$("#min_set").val()
    var segundos=$("#seg_set").val()
 
        var timer = setInterval(function(){

            if (segundos>=0 && minutos<10){
                document.getElementById('timerJuego').innerHTML='0'+minutos+":"+segundos;
            }else if (segundos<10 && minutos>=10){
                document.getElementById('timerJuego').innerHTML=minutos+':0'+segundos;
            }  
        
         
            var estado = $("#estado").html()
            alert(segundos)
            if (segundos==0){
                minutos--
                segundos=60
            }
            if (estado!='detenido') {
                segundos--
            }
            
            
        }, 1000);  
}
 



$(document).ready(function(){
    set_estado_reloj("cero")
     
    $(".op2").hide()

    
    
    $( "#adelante" ).click(function() {suma_tiempo()});
    $( "#atras" ).click(function() {$("#estado").html("resta")});
    $( "#detiene" ).click(function() {$("#estado").html("detenido")});

    $("#btn_lanzamientos").click(function(){ $("#lanzamientos").slideDown();});
    $("#btn_tapones").click(function(){ $("#tapones").slideDown();});

    $(".btn_lanza").click(function(){ valor=$(this).attr("data"); $("#lanzamientos").slideUp();});
    $(".btn_tapon").click(function(){ valor=$(this).attr("data"); $("#tapones").slideUp();});
 
    
 
});