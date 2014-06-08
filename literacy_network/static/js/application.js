$(document).ready(function() {
    if(typeof customExportTitle == "undefined") {
        customExportTitle = document.title;
    }

    $("input[type=text], input[type=checkbox], password").uniform();

    if($("#data-table").length) {

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

        $('#data-table #filters th').each( function (i) {
            var title = $('#data-table #titles th').eq( $(this).index() ).text();
            $(this).html( '<input type="text" placeholder="Filter" />' );
            table.columns().eq( 0 ).each( function ( colIdx ) {
                $( '#filters input'/*, table.column( colIdx ).footer()*/ ).on( 'keyup change', function () {
                    table
                    .column( colIdx )
                    .search( this.value )
                    .draw();
                } );
            } );
    } );

}

});
