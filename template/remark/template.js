let options = {
    ratio: '4:3',
    // highlightStyle: 'solarized-light',
    highlightLines: true,
    highlightSpans: true,
};
let slideshow = remark.create(options);
mermaid.initialize({
    startOnLoad: false,
    cloneCssStyles: false
});
function initMermaid(s) {
    let diagrams = document.querySelectorAll('.mermaid');
    for (let i = 0; i < diagrams.length; i++) {
        if (diagrams[i].offsetWidth > 0) {
            mermaid.init(undefined, diagrams[i]);
        }
    }
}
slideshow.on('afterShowSlide', initMermaid);
initMermaid(slideshow.getSlides()[slideshow.getCurrentSlideIndex()]);
