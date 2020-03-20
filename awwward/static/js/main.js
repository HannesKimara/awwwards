function onLoadSeq(siteId) {
    function drawProgress(designScore, usabilityScore, contentScore) {
        var circleDesign = new ProgressBar.Circle('#progress-design', {
            color: '#FCB03C',
            duration: 2000,
            easing: 'easeInOut',
            strokeWidth: 3,
        });
    
        circleDesign.animate(designScore);
    
        var circleUsabilty = new ProgressBar.Circle('#progress-usability', {
            color: '#49c5b6',
            duration: 2000,
            easing: 'easeInOut',
            strokeWidth: 3,
        });
    
        circleUsabilty.animate(usabilityScore);
    
        var circleContent = new ProgressBar.Circle('#progress-content', {
            color: 'green',
            duration: 2000,
            easing: 'easeInOut',
            strokeWidth: 3,
        });
    
        circleContent.animate(contentScore);
    };

    $.ajax({
        'url':`/api/projects/${siteId}`,
        'type':'GET',
        'success': function(data){
            drawProgress(data['total_design']/10, data['total_usability']/10, data['total_content']/10)
    }});
}

document.addEventListener('DOMContentLoaded', function() {
    var options = {};
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function() {
    var options={};
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
});