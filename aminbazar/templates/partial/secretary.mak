%if secretary.title.strip():
    <section class="box">
        <div>
        <header>
        <h3 class="pull-right">${secretary.job_title}</h3>
    </header>
        <article>
        <img src="${secretary.image.url}" class="pull-right" style="margin-left: 8px;"/>
        <div class="pull-right">
        <h4 style="margin-top: 8px;">${secretary.title}</h4>
    %if secretary_histories:
        <h5 style="margin-top: 8px;">سوابق</h5>
        <ul>
    %for i in secretary_histories:
            <li>${i.description}</li>
        %endfor
    </ul>
    %endif
    </div>
    </article>
    </div>
    </section>
%endif
