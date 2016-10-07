%if boss.title.strip():
<section class="box bayanat-box">
  <div>
    <header>
      <h3 class="pull-right">${boss.job_title}</h3>
    </header>
    <article>
      <img src="${boss.image.url}" class="pull-right" style="margin-left: 8px;"/>
      <div class="pull-right">
        <h4 style="margin-top: 8px;">${boss.title}</h4>
        %if boss_histories:
          <h5 style="margin-top: 8px;">سوابق</h5>
          <ul>
            %for i in boss_histories:
              <li>${i.description}</li>
            %endfor
          </ul>
        %endif
      </div>
    </article>
  </div>
</section>
%endif