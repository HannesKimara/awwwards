window.onload = function onLoad() {
    var circleDesign = new ProgressBar.Circle('#progress-design', {
        color: '#FCB03C',
        duration: 2000,
        easing: 'easeInOut',
        strokeWidth: 3,
        text: {
            value:'Text',
        }
    });

    circleDesign.animate(0.568);

    var circleUsabilty = new ProgressBar.Circle('#progress-usability', {
        color: '#49c5b6',
        duration: 2000,
        easing: 'easeInOut',
        strokeWidth: 3,
        text: {
            value:'Text'
        }
    });

    circleUsabilty.animate(0.78);

    var circleContent = new ProgressBar.Circle('#progress-content', {
        color: 'green',
        duration: 2000,
        easing: 'easeInOut',
        strokeWidth: 3,
        text: {
            value:'Text'
        }
    });

    circleContent.animate(0.9);
};

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