jQuery("document").ready(function(){
    $('#fine-uploader-gallery').fineUploader({
            template: 'qq-template-gallery',
            request: {
                endpoint: $('#fine-uploader-gallery').attr('form-url'),
                customHeaders: {
                    'X-CSRFToken': $('#fine-uploader-gallery').attr('form-token')
                }
            },
            thumbnails: {
                placeholders: {
                    waitingPath: 'static/scripts/fine-uploader-5.14.0/placeholders/waiting-generic.png',
                    notAvailablePath: 'static/scripts/fine-uploader-5.14.0/placeholders/not_available-generic.png'
                }
            },
            validation: {
                allowedExtensions: ['txt']
            },
            callbacks: {
                onComplete: function (id, name, responseJSON, xhr) {
                    var text_link = '<a href='+responseJSON.url+'>'+responseJSON.name+'</a>'
                    $("[qq-file-id="+id+"] .qq-file-name").append(text_link)
                }
            }
        });
});