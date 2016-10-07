<footer id="mainFooter">
  <div class="container">
    %if contact_info:
      <ul class="contact-info">
        <li>
          <div>آدرس</div>
          <div>${contact_info.address}</div>
        </li>
        <li>
          <div>تلفن</div>
          <div>${contact_info.phone1}</div>
          <div>${contact_info.phone2}</div>
        </li>
        <li>
          <div>تلفکس</div>
          <div>${contact_info.fax}</div>
        </li>
        <li>
          <div>پست الکترونیکی</div>
          <div>${contact_info.email}</div>
        </li>
      </ul>
    %endif
    <div class="spacer"></div>
    %if related_links:
      <div class="related-links">
        <ul>
          %for link in related_links:
            <li><a target="_blank" href="${link.url}">${link.title}</a></li>
          %endfor
        </ul>
      </div>
    %endif
    <div class="grid-24">
      <p>
        ${h.footer() | n}
      </p>
    </div>
  </div>
</footer>