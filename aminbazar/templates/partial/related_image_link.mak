%if related_image_links:
  <div class="related-image-links">
    <ul>
      %for i in related_image_links:
        <li title="${i.title}">
          <a target="_blank" href="${i.url}">
            <img src="${i.image.url}" alt="${i.title}">
          </a>
        </li>
      %endfor
    </ul>
  </div>
%endif