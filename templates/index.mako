<%inherit file="base.mako"/>

% for i in items:
  <img src=${i.images.thumbnail.url}></img>
% endfor
