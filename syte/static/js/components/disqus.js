var _embed_disqus = function() {
    var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
    dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
};   

var _embed_disqus_count = function () {
    var s = document.createElement('script'); s.async = true;
    s.type = 'text/javascript';
    s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
    (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
}

var on_element_ready = function(selector, fn) {
    // since the blog templates may be loaded dynamically we need to
    // wait for the selectors to appear before running disqus code
    var check = function() {
        if ($(selector).length > 0) return fn();
        setTimeout(check, 100);
    }
    
    check();
}

var embed_disqus = function() {
    on_element_ready('#disqus_thread', _embed_disqus);
}

var embed_disqus_count = function() {
    on_element_ready('.comments', _embed_disqus_count);
}