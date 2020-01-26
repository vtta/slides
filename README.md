# slides

An out-of-box markdown slideshow toolkit via [remark](https://github.com/gnab/remark), [here is a example](https://vtta.github.io/slides/2.html).

## usage

The surrounding environment is already configured for you.
Just read the markdown specifications [here](https://github.com/gnab/remark/wiki/Markdown), edit the markdown file and start presentating! 

```bash
git clone https://github.com/vtta/slides
cd slides
chmod a+x build.py
./build.py new new_slide
nvim new_slide.md
./build.py build new_slide
# show sub-command only works on mac now
./build.py show new_slide
```
