//Global configs and functions shared between js

function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

require.config({
  baseUrl: "/static/",
  paths: {
    "text": "js/libs/text",
    "json": "js/libs/json"
  },
  waitSeconds: 15
});

var spin_opts = {
  lines: 9,
  length: 5,
  width: 2,
  radius: 4,
  rotate: 9,
  color: '#4c4c4c',
  speed: 1.5,
  trail: 40,
  shadow: false,
  hwaccel: false,
  className: 'spinner',
  zIndex: 2e9
};



