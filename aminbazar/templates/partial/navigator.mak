<nav id="mainNavigator" class="navbar">
  <ul>
    %for parent_menu in h.parent_menus():
      <li>
        <a
          %if parent_menu.url:
            href="${parent_menu.url}"
          %endif
          >${parent_menu.title}</a>
        %if parent_menu.submenus:
          <ul>
            %for sub_menu in parent_menu.submenus:
              <li>
                <a href="${sub_menu.url if sub_menu.url else ''}">${sub_menu.title}</a>
                %if sub_menu.submenus:
                  <ul>
                    %for sub_sub_menu in sub_menu.submenus:
                      <li>
                        <a href="${sub_sub_menu.url if sub_sub_menu.url else ''}">${sub_sub_menu.title}</a>
                      </li>
                    %endfor
                  </ul>
                %endif
              </li>
            %endfor
          </ul>
        %endif
      </li>
    %endfor

  </ul>
  <div class="social-container">
    <ul>
        %for s in h.socials():
            <li>
                <a href="${s.url}" target="_blank">
                    <img title="${s.title}" src="${s.image.url}"/>
                </a>
            </li>
        %endfor
    </ul>
  </div>
</nav>

