$(document).ready(function() {
    if(typeof customExportTitle == "undefined") {
        customExportTitle = document.title;
    }

    $("select, input[type=text], input[type=checkbox], password").uniform();

    $('#data-table tfoot th').each( function () {
        var title = $('#data-table thead th').eq( $(this).index() ).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    } );

    var table = $("#data-table").DataTable({
        "bLengthChange" : false,
        "iDisplayLength": 100,
        "sDom": 'T<"clear">lfrtip',
        "oTableTools": {
            "sSwfPath": "/static/swf/copy_csv_xls_pdf.swf",
            "aButtons" : [
            {
                "sExtends" : "xls",
                "sTitle" : customExportTitle
            },
            {
                "sExtends" : "pdf",
                "sTitle" : customExportTitle
            }
            ]
        }
    });

    table.columns().eq( 0 ).each( function ( colIdx ) {
        $( 'input', table.column( colIdx ).footer() ).on( 'keyup change', function () {
            table
            .column( colIdx )
            .search( this.value )
            .draw();
        } );
    } );

});
