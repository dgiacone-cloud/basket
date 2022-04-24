const ruta = window.location.origin;
$(document).ready(function() {
    if(document.getElementById('reporteDeCruceCliente') != null){
        reloadDataTableReporteDeCruceCliente();
    }
    if(document.getElementById('derivaciones') != null){
        reloadDataTableDerivaciones();
        document.querySelector("input[aria-controls='derivaciones']").setAttribute('onkeypress', "return (event.charCode >= 48 && event.charCode <= 57 || event.charCode == 45)");
    }
    
    if(document.getElementById('loteCruceCliente') != null){
        reloadDataTableLoteCruceCliente();
    }

    if(document.getElementById('detalleAnexo') != null){
        reloadDataTableDetalleAnexo();
      }
     
});


function reloadDataTableReporteDeCruceCliente(){
    let dniSeleccionado = '';
    let nombreSeleccionado = '';
    let arrayColor = ['#99B5DB','#f5f5f7'];
    let contadorColor = 0;

    $('#reporteDeCruceCliente').DataTable( {
          "destroy":true, 
          "ajax": {
              "url":ruta+"/reporteDeCruceFrecuenciaClienteWS",
              "type": "POST",
              "data" : {
                  "cliente" : document.getElementById('cliente').value,
                  "lote":document.getElementById('lote').value,
              },
            },
          "ordering": false,
          "processing": true,
          "autoWidth": false,
          "columns": [
            // DEFINO LAS COLUMAS Y LAS RELACIONO CON EL DATA DEL QUE OBTENDRA LOS DATOS A MOSTRAR
              { "data":  "frecuencia"  ,"title":"Frecuencia"}, //0
              { "data": "nombre" ,"title":"Nombre"}, //1
              { "data": "dni" ,"title":"DNI"}, //2
              { "data": "rol" ,"title":"Rol"}, //3
              { "data": "fechaSiniestro" ,"title":"Fecha de Siniestro"}, //4
              { "data": "abogado" ,"title":"Abogado", }, //5
              { "data": "cuit" ,"title":"CUIT/CUIL"}, //6
              { "data": "categorizacion" ,"title":"Categorizacion"},//7
              { "data": "aseguradora" ,"title":"Aseguradora"}, //8
              { "data": "nro_siniestro" ,"title":"Nº Siniestro"},  //9
              { "data": "expediente" ,"title":"Expediente"}, //10
              { "data": "jurisdiccion" ,"title":"Jurisdiccion"}, //11
              { "data": "juzgado" ,"title":"Juzgado"}, //12
              { "data": "fuero" ,"title":"Fuero"}, //13
              { "data": "comentario" ,"title":"Comentario"},//14
              { "data": "documento" ,"title":"Documento"}//15
              
          ],
          "columnDefs": [
            // ME ENCARGO DE OCULTAR LAS COLUMNAS
            {
                "targets": [ 7,11,12,13,14 ],
                "visible": false,
                "searchable": false
            },
          ],
          /*
            ///////// CONFIGURACION PARA LOS FILTROS POR COLUMNA
          initComplete: function () {
              this.api().columns().every( function () {
                
                  var column = this;
                  if(column[0] != 6){
                    var select = $('<br><select><option value=""></option></select>')
                        //.appendTo( $(column.header()).empty() )
                        .appendTo( column.header() )
                        .on( 'change', function () {
                            var val = $.fn.dataTable.util.escapeRegex(
                                $(this).val()
                            );

                            column
                                .search( val ? '^'+val+'$' : '', true, false )
                                .draw();
                        } );

                    column.data().unique().sort().each( function ( d, j ) {
                        select.append( '<option value="'+d+'">'+d+'</option>' )
                    } );
                  }else{
                    var select = $('<br>')
                        .appendTo( column.header() )
                  }
              } );
          },*/
          "dom": 'Bfrtip',
          "buttons": [
            {
              text: ' Reporte completo',
              extend: 'excelHtml5',
              filename: "Informe_de_cruce_"+(document.getElementById('tipo').value == 'f'?'_FECHA_':'_DOCUMENTO_')+document.getElementById('nombrecliente').value.replaceAll(' ', '').toLowerCase()*'_'+document.getElementById('dato').value.replaceAll(' ', '').toLowerCase(),
              title: null,
              customize: function ( xlsx ) {
                var sheet = xlsx.xl.worksheets['sheet1.xml'];
                $( 'sheets sheet', xlsx.xl['workbook.xml'] ).attr( 'name', (document.getElementById('tipo').value == 'f'?'_FECHA_':'_DOCUMENTO_')+document.getElementById('nombrecliente').value.replaceAll(' ', '').toLowerCase()+'_'+document.getElementById('dato').value.replaceAll(' ', '').toLowerCase() );

                //var sheet = xlsx.xl.worksheets[(document.getElementById('tipo').value == 'f'?'_FECHA_':'_DOCUMENTO_')+document.getElementById('nombrecliente').value.replaceAll(' ', '').toLowerCase()*'_'+document.getElementById('dato').value.replaceAll(' ', '').toLowerCase()+'.xml'];
                $('c[r=A1] t', sheet).text( 'Frecuencia' );
                $('c[r=B1] t', sheet).text( 'Nombre' );
                $('c[r=C1] t', sheet).text( 'Dni' );
                $('c[r=D1] t', sheet).text( 'Rol' ); 
                $('c[r=E1] t', sheet).text( 'Documento' );
                $('c[r=F1] t', sheet).text( 'Fecha Siniestro' );
                $('c[r=G1] t', sheet).text( 'Abogado' );
                $('c[r=H1] t', sheet).text( 'Cuil Cuit' );1
                $('c[r=I1] t', sheet).text( 'Categorizacion' );
                $('c[r=J1] t', sheet).text( 'Aseguradora' ); 
                $('c[r=K1] t', sheet).text( 'Nro siniestro' );
                $('c[r=L1] t', sheet).text( 'Expediente' );
                $('c[r=M1] t', sheet).text( 'Jurisdiccion' );
                $('c[r=N1] t', sheet).text( 'Juzgado' );
                $('c[r=O1] t', sheet).text( 'Fuero' );
                $('c[r=P1] t', sheet).text( 'Comentario' );
              }
              
            }
          ],
          "rowCallback": function( row, data ) {
            // FUNCION PARA PINTAR LAS FILAS DE COLORES AGRUPANDO LOS QUE SE REPITEN
            if ( data['dni'] != "Sin dato" ) {
              
              if(dniSeleccionado == ''){
                dniSeleccionado =data['dni'];
              }
              if(nombreSeleccionado == ''){
                nombreSeleccionado =data['nombre'];
              }
              
              if( (dniSeleccionado == data['dni'] && nombreSeleccionado == data['nombre']) ||  (dniSeleccionado == data['dni']  && nombreSeleccionado != data['nombre']) || (dniSeleccionado != data['dni']  && nombreSeleccionado == data['nombre'])){
                $(row).css('background-color',arrayColor[contadorColor]);
                //$($(row).children("td")[0]).css('background-color',arrayColor[contadorColor]);
              }else{
                dniSeleccionado = data['dni'];
                contadorColor = inicializadorIndice(contadorColor,arrayColor);
                $(row).css('background-color',arrayColor[contadorColor]);
                //$($(row).children("td")[0]).css('background-color',arrayColor[contadorColor]);
              }
              
            }else{
              if(nombreSeleccionado == ''){
                nombreSeleccionado =data['nombre'];
              }

              if(nombreSeleccionado == data['nombre']){
                $(row).css('background-color',arrayColor[contadorColor]);
                //$($(row).children("td")[0]).css('background-color',arrayColor[contadorColor]);
              }else{
                nombreSeleccionado = data['nombre'];
                contadorColor = inicializadorIndice(contadorColor,arrayColor);
                $(row).css('background-color',arrayColor[contadorColor]);
                //$($(row).children("td")[0]).css('background-color',arrayColor[contadorColor]);
              }
            }
          },
          "pageLength": 25,
          "lengthMenu": [25, 50, 75, 100],
          "language": {
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "o se ha encontrado nada, lo siento",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            //"infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(filtered from _MAX_ total records)",
            "search": "Buscar",
            'paginate': {
              'previous': 'Previo',
              'next': 'Siguiente'
            }
          }
          
      } );


    return false;
  }


function reloadDataTableDerivaciones(){
$('#derivaciones').DataTable( {
        "destroy":true,
        "ajax": {
            "url":ruta+"/lotesWS",
            "type": "POST",
        },
        "processing": true,
        "columns": [
            //{ "data": "cliente" ,"title":"Cliente"},
            { "data": "lote","title":"Fecha Derivaciones" },
            //{ "data": "fecha_carga","title":"Fecha" },
            { "data": "documentos" ,"title":"Demandas"},
            { "data": "estado","title":"Estado" },
            { "data": "cruces" ,"title":"Hallazgos"},
            { "data": "features","title":"Detalle de Demandas"}
        ],
        "columnDefs": [
          // ME ENCARGO DE OCULTAR LAS COLUMNAS
          {
              "targets": [ 1,2,3,4 ],
              "searchable": false
          },
        ],
        /*
        ///////// CONFIGURACION PARA LOS FILTROS POR COLUMNA
        initComplete: function () {
            this.api().columns().every( function () {

                var column = this;
                if(column[0] != 0 && column[0] != 2 && column[0] != 3 && column[0] != 4){
                var select = $('<br><select><option value=""></option></select>')
                    //.appendTo( $(column.header()).empty() )
                    .appendTo( column.header() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    console.log(d);
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
                }else{
                var select = $('<br>')
                    .appendTo( column.header() )
                }
            } );
        },*/
        /*"dom": 'Bfrtip',
        "buttons": [
            'csv', 'excel'
        ],*/
        "order": [[ 0, "desc" ]],
        "pageLength": 25,
        //"lengthMenu": [25, 50, 75, 100],
        "bLengthChange": false,
        "language": {
        "lengthMenu": "Mostrar _MENU_ registros por página",
        "zeroRecords": "o se ha encontrado nada, lo siento",
        "info": "Mostrando página _PAGE_ de _PAGES_",
        //"infoEmpty": "No hay registros disponibles",
        "infoFiltered": "(filtered from _MAX_ total records)",
        "search": "Buscar por Fecha",
        'paginate': {
            'previous': 'Previo',
            'next': 'Siguiente'
        }
    }
    } );


return false;
}

function reloadDataTableLoteCruceCliente(){
    $('#loteCruceCliente').DataTable( {
          "destroy":true,
          "ajax": {
              "url":ruta+"/rpcWS",
              "type": "POST"
            },
          "processing": true,
          "columns": [
            { "data": "lote","title":"Fecha de Derivación" },
            { "data": "numerosiniestro","title":"Número siniestro" },            
            { "data": "jurisdiccion","title":"Jurisdicción" },
            { "data": "fuero","title":"Fuero" },
            { "data": "juzgado","title":"Juzgado" },
            { "data": "numeroexpediente","title":"Número expediente" },
            { "data": "accion","title":"" }
              
            ],
            "columnDefs": [
              // ME ENCARGO DE OCULTAR LAS COLUMNAS
              {
                  "targets": [ 6 ],
                  "orderable": false
              },
            ],
            ///////// CONFIGURACION PARA LOS FILTROS POR COLUMNA
            initComplete: function () {
              this.api().columns().every( function () {
                
                  var column = this;
                  if(column[0] != 6 && column[0] != 0 && column[0] != 1 && column[0] != 5){
                    var select = $('<br><select><option value=""></option></select>')
                        //.appendTo( $(column.header()).empty() )
                        .appendTo( column.header() )
                        .on( 'change', function () {
                            var val = $.fn.dataTable.util.escapeRegex(
                                $(this).val()
                            );
  
                            column
                                .search( val ? '^'+val+'$' : '', true, false )
                                .draw();
                        } );
  
                    column.data().unique().sort().each( function ( d, j ) {
                        select.append( '<option value="'+d+'">'+d+'</option>' )
                    } );
                  }else{
                    var select = $('<br>')
                        .appendTo( column.header() )
                  }
              } );
          },
          /*
        "dom": 'Bfrtip',
        "buttons": [
            'csv', 'excel'
        ],*/
        "order": [[ 0, "desc" ]],
        "pageLength": 25,
        "lengthMenu": [25, 50, 75, 100],
        "bLengthChange": false,
        "language": {
        "lengthMenu": "Mostrar _MENU_ registros por página",
        "zeroRecords": "o se ha encontrado nada, lo siento",
        "info": "Mostrando página _PAGE_ de _PAGES_",
        //"infoEmpty": "No hay registros disponibles",
        "infoFiltered": "(filtered from _MAX_ total records)",
        "search": "Buscar",
        'paginate': {
            'previous': 'Previo',
            'next': 'Siguiente'
        }
        }
      } );
  
  
    return false;
}

function reloadDataTableDetalleAnexo(){
    $('#detalleAnexo').DataTable( {
            "destroy":true,
            "ajax": {
                "url":ruta+"/detalle_anexoWS",
                "type": "POST",
                "data" : {
                    "cliente" : document.getElementById('cliente').value,
                    "fecha_carga":document.getElementById('fecha_carga').value,
                },
            },
            "processing": true,
            "columns": [
            { "data": "cliente","title":"Aseguradora" },//0
            { "data": "fecha_carga ","title":"Fecha Derivación" },//1
            { "data": "nro_siniestro ","title":"Número siniestro" },//2
            { "data": "jurisdiccion","title":"Jurisdicción" },//3
            { "data": "fuero","title":"Fuero" },//4
            { "data": "juzgado","title":"Juzgado" },//5
            { "data": "expediente ","title":"Expediente" },//6
            { "data": "Abogados2","title":"Abogados" },//7
            { "data": "Actores","title":"Actores" },//8
            { "data": "Demandado","title":"Demandado" },//9
            { "data": "Fecha_siniestro","title":"Fecha Siniestro" },//10
            { "data": "Calle","title":"Calle" },//11
            { "data": "Altura","title":"Altura" },//12
            { "data": "Interseccion","title":"Intersección" },//13
            { "data": "Localidad","title":"Localidad" },//14
            { "data": "Testigos","title":"Testigos" },//15
            { "data": "Hospital","title":"Hospital" },//16
            { "data": "Comisaria","title":"Comisaría" },//17
            { "data": "Medico","title":"Médico" },//18
            { "data": "Lesion","title":"Lesión" },//19	
            { "data": "Partido","title":"Partido" },//20
            { "data": "filename","title":"Documento" }//21
            ],
            "columnDefs": [
                // ME ENCARGO DE OCULTAR LAS COLUMNAS
                {
                    "targets": [ 0,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                    "visible": false,
                    "searchable": false
                },
            ],
            /*
            ///////// CONFIGURACION PARA LOS FILTROS POR COLUMNA
            initComplete: function () {
                this.api().columns().every( function () {
                
                    var column = this;
                    if(column[0] != 6 && column[0] != 9){
                    var select = $('<br><select><option value=""></option></select>')
                        //.appendTo( $(column.header()).empty() )
                        .appendTo( column.header() )
                        .on( 'change', function () {
                            var val = $.fn.dataTable.util.escapeRegex(
                                $(this).val()
                            );
    
                            column
                                .search( val ? '^'+val+'$' : '', true, false )
                                .draw();
                        } );
    
                    column.data().unique().sort().each( function ( d, j ) {
                        select.append( '<option value="'+d+'">'+d+'</option>' )
                    } );
                    }else{
                    var select = $('<br>')
                        .appendTo( column.header() )
                    }
                } );
            },*/
            "dom": 'Bfrtip',
            "pageLength": 25,
            "lengthMenu": [25, 50, 75, 100],
            "language": {
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "o se ha encontrado nada, lo siento",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            //"infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(filtered from _MAX_ total records)",
            "search": "Buscar",
            'paginate': {
                'previous': 'Previo',
                'next': 'Siguiente'
            }
            },
            "buttons": [
            {   
                text: 'Detalle de demandas completo',
                extend: 'excelHtml5',
                filename: document.getElementById('tituloListadoAnexo').innerHTML.replaceAll(' ', '').toLowerCase(),
                title : null,
                customize: function ( xlsx ) {
                    var sheet = xlsx.xl.worksheets['sheet1.xml'];
                    $( 'sheets sheet', xlsx.xl['workbook.xml'] ).attr( 'name', document.getElementById('tituloListadoAnexo').innerHTML.replaceAll(' ', '').toLowerCase() );

                    //$('c[r=A1] t', sheet).text( document.getElementById('tituloListadoAnexo').innerHTML.replaceAll(' ', '').toLowerCase());
                    $('c[r=A1] t', sheet).text( 'Aseguradora' );
                    $('c[r=B1] t', sheet).text( 'Fecha carga' );
                    $('c[r=C1] t', sheet).text( 'Nro siniestro' ); 
                    $('c[r=D1] t', sheet).text( 'Jurisdiccion' );
                    $('c[r=E1] t', sheet).text( 'Fuero' );
                    $('c[r=F1] t', sheet).text( 'Juzgado' );
                    $('c[r=G1] t', sheet).text( 'Expediente' );
                    $('c[r=H1] t', sheet).text( 'Abogados' ); 
                    $('c[r=I1] t', sheet).text( 'Actores' );
                    $('c[r=J1] t', sheet).text( 'Demandado' );
                    $('c[r=K1] t', sheet).text( 'Fecha Siniestro' );
                    $('c[r=L1] t', sheet).text( 'Calle' );
                    $('c[r=M1] t', sheet).text( 'Altura' );
                    $('c[r=N1] t', sheet).text( 'Interseccion' );
                    $('c[r=O1] t', sheet).text( 'Localidad' );
                    $('c[r=P1] t', sheet).text( 'Testigos' );
                    $('c[r=Q1] t', sheet).text( 'Hospital' );
                    $('c[r=R1] t', sheet).text( 'Comisaria' );
                    $('c[r=S1] t', sheet).text( 'Medico' );
                    $('c[r=T1] t', sheet).text( 'Lesion' );
                    $('c[r=U1] t', sheet).text( 'Partido' );
                    $('c[r=V1] t', sheet).text( 'Documento' );
                }
            }
        ]
        } );
    
    
    return false;
}
    




function inicializadorIndice(valor,arry){
    if((arry.length -1) > valor){
        valor ++;
    }else{
        valor = 0;
    }
    return valor;
}
      