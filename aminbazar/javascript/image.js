/**
 * Created by vahid on 8/19/14.
 */

Namespace('twa');

Class('twa.Image', {
  __init__: function(el){
    this.element = el;
    this.pngTest = false;
    this.setup();
  },
  setup: function(){

    if (!this.pngTest && Modernizr.inlinesvg) {
        this.createSVG();
    }
    else{
        this.createFailsafeImage();
    }
    this.element.viewModel = this;
  },
  getImageKey: function(){
    var key = $(this.element).data('name');
    if(key){
      return key;
    }
    return 'no-image-available';
  },
  getImageUrl: function(extension){
    return '/img/%s.%s'.format(this.getImageKey(), extension);
  },
  createSVG: function() {
    var self = this,
      $el = $(self.element);

    Snap.load(self.getImageUrl('svg'), function(f) {
        var s = f.select('svg');
        $el.append(s.node);
//        var c = s.select('circle');
//        var p = s.select('polyline');
//        c.hover(function(e) {
//            console.log('hover');
//        });
    });
  },
  createFailsafeImage: function(){
    var self = this,
      $el = $(self.element);
    $el.append($('<img />')
        .attr({src: self.getImageUrl((!self.pngTest && Modernizr.svg) ? 'svg' : 'png')}));
  }
}).StaticMembers({
  get: function(el){
    if (!el.hasOwnProperty('viewModel')){
      return new this(el);
    }
    return el.viewModel;
  }
});

