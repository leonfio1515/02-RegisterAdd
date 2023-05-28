var url_spanish = '../../static/lib/DataTables/js/spanish.txt'


var table = $('#tabla').DataTable({
    "language": {
        url: url_spanish
    },
    responsive: true,
    dom: 'Bfrtilp',
    order: [[0, 'desc']],
    buttons: [{
        extend: 'excelHtml5',
        text: '<i class="bi bi-file-earmark-excel"></i>',
        titleAttr: 'Exportar a Excel',
        className: 'btn btn-success',
    }],
});
