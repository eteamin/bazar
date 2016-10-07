<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
##   <url>
##     <loc>http://${domain}/</loc>
##     <lastmod>${seo.last_modification_time.strftime('%Y-%m-%d')}</lastmod>
##     <priority>1.0</priority>
##   </url>
  %for page in pages:
    <url>
      <loc>http://${domain}${page.url}</loc>
      <lastmod>${page.last_modification_time.strftime('%Y-%m-%d')}</lastmod>
      <priority>${page.priority}</priority>
    </url>
  %endfor
</urlset>