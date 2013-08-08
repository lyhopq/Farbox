Title: FarBox
Date: 2013-08-02 21:00

[TOC]

* * *

# [FarBox][0]

[0]: http://www.farbox.com/

## 模板

拷贝 [衣不如新][motype] 的模板 [https://github.com/deepure/fblog][git]，改名为template放在网站根目录下。


[motype]: http://motype.org
[git]: https://github.com/deepure/fblog

## MathJax

[MathJax][] 让你的blog支持$\LaTeX$

[MathJax]: http://www.mathjax.org

在模板目录的base.html文件中添加：

```
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        extensions: ["tex2jax.js"],
        jax: ["input/TeX", "output/HTML-CSS"],
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true},
            "HTML-CSS": { availableFonts: ["TeX"], linebreaks: {automatic: true}},
            TeX: {equationNumbers: {autoNumber: ["AMS"], useLabelIds: true}},
            <!-- "HTML-CSS": {linebreaks: {automatic: true}}, -->
            SVG: {linebreaks: {automatic: true}}
        });
</script>

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
```

详见： [http://freealbert.farbox.com/post/blog/latex-tips][1]

解决Pygments与MathJax的冲突，在base.html中添加：

    <style type="text/css">.MathJax .mi, .MathJax .mo { color: #111; }</style> 
    
详见： [http://freealbert.farbox.com/post/blog/pygments-mathjax][2]

[1]: http://freealbert.farbox.com/post/blog/latex-tips
[2]: http://freealbert.farbox.com/post/blog/pygments-mathjax
    


