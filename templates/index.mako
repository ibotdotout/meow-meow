<%inherit file="base.mako"/>

<center>
  % for i in items:
    <div>
      <div>
        <img src=${i.images.low.url}></img>
      </div>
      <div style="width:300px; word-wrap:break-word;">
        ${i.user.username} :::: ${i.caption.text}
      </div>
      <br>
    </div>
  % endfor
</center>
