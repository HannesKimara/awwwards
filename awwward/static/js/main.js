window.onload = function onLoad() {
    var circleDesign = new ProgressBar.Circle('#progress-design', {
        color: '#FCB03C',
        duration: 3000,
        easing: 'easeInOut',
        strokeWidth: 4,
        text: {
            value:'Text'
        }
    });

    circleDesign.animate(0.78);

    var circleUsabilty = new ProgressBar.Circle('#progress-usability', {
        color: '#49c5b6',
        duration: 3000,
        easing: 'easeInOut',
        strokeWidth: 4,
        text: {
            value:'Text'
        }
    });

    circleUsabilty.animate(0.78);

    var circleContent = new ProgressBar.Circle('#progress-content', {
        color: 'green',
        duration: 3000,
        easing: 'easeInOut',
        strokeWidth: 4,
        text: {
            value:'Text'
        }
    });

    circleContent.animate(0.78);
};