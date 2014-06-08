$(document).ready(function() {
    if(typeof customExportTitle == "undefined") {
        customExportTitle = document.title;
    }

    $("select, input[type=text], input[type=checkbox], password").uniform();

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

        $('#data-table tfoot th').each( function (i) {
            var title = $('#data-table thead th').eq( $(this).index() ).text();
        /*if (title==="Industry"||title==="Help Type"||title==="Visit Site") {
            var select = $('<select><option value=""></option></select>')
            .appendTo( $(this).empty() )
            .on( 'change', function () {
                table.column( i )
                .search( this.value )
                .draw();
            } );

            table.column( i ).data().unique().sort().each( function ( d, j ) {
                select.append( '<option value="'+d+'">'+d+'</option>' )
            } );
        } else {
            */
            $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
            table.columns().eq( 0 ).each( function ( colIdx ) {
                $( 'input', table.column( colIdx ).footer() ).on( 'keyup change', function () {
                    table
                    .column( colIdx )
                    .search( this.value )
                    .draw();
                } );
            } );
        //}
    } );

}

});
