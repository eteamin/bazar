<div class="advertisement">
    %if ads:
        <ul>
            %for a in ads:
                <li>
                    <a href="${a.url}">
                        <img src="${a.image.url}"/>
                    </a>
                </li>
            %endfor
        </ul>
    %else:
        <h4>هیچ تبلیغاتی وجود ندارد</h4>
    %endif
</div>
