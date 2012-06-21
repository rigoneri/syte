var embedDisqus = function(justCount) {
  var type = "embed";
  if (justCount)
    type = 'count';

  var dsq = document.createElement('script');
  dsq.type = 'text/javascript';
  dsq.async = true;
  dsq.src = 'http://' + disqus_shortname + '.disqus.com/'+ type +'.js';
  (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
}

