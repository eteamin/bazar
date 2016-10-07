/**
 * Created by vahid on 4/30/15.
 * version: 0.1.0
 */

(function ($) {

    function inputHidden(name, id) {
        if (!id) id = name;
        return $('<input type="hidden" />').attr({id: id, name: name});
    }

    function sind(x) {
        return (Math.sin(Math.PI / 180.0 * x));
    }

    function cosd(x) {
        return (Math.cos(Math.PI / 180.0 * x));
    }

    function tand(x) {
        return (Math.tan(Math.PI / 180.0 * x));
    }

    function atand(x) {
        return (Math.atan(x) * 180.0 / Math.PI);
    }

    function asind(x) {
        return (Math.asin(x) * 180.0 / Math.PI);
    }

    function acosd(x) {
        return (Math.acos(x) * 180.0 / Math.PI);
    }

    function loc2hor(z, d, p) {
        return (acosd((cosd(z) - sind(d) * sind(p)) / cosd(d) / cosd(p)) / 15);
    }

    function round(x, a) {
        var tmp = x % a;
        if (tmp < 0)
            tmp += a;
        return tmp;
    }


    $.fn.prayerTimes = function (options) {

        var settings = $.extend({
            city: "تهران",
            longitudes: [0, 49.70, 48.30, 45.07, 51.64, 48.68, 46.42, 57.33, 56.29, 50.84, 59.21, 46.28, 51.41, 48.34, 49.59, 60.86, 48.50, 53.06, 53.39, 47.00, 50.86, 52.52, 50.00, 50.88, 57.06, 47.09, 54.44, 59.58, 48.52, 51.59, 54.35],
            latitudes: [0, 34.09, 38.25, 37.55, 32.68, 31.32, 33.64, 37.47, 27.19, 28.97, 32.86, 38.08, 35.70, 33.46, 37.28, 29.50, 36.68, 36.57, 35.58, 35.31, 32.33, 29.62, 36.28, 34.64, 30.29, 34.34, 36.84, 36.31, 34.80, 30.67, 31.89],
            cities: ['', 'اراک', 'اردبیل', 'ارومیه', 'اصفهان', 'اهواز', 'ایلام', 'بجنورد', 'بندرعباس', 'بوشهر', 'بیرجند', 'تبریز', 'تهران', 'خرم آباد', 'رشت', 'زاهدان', 'زنجان', 'ساری', 'سمنان', 'سنندج', 'شهرکرد', 'شیراز', 'قزوین', 'قم', 'کرمان', 'کرمانشاه', 'گرگان', 'مشهد', 'همدان', 'یاسوج', 'یزد'],
            dst: dstOffset,
            arrowImageUrl: 'img/arrow.gif',
            blinkerArrowImageUrl: 'img/arrow-blinker.gif'
        }, options);


        this.each(function () {

            /* INIT START */

            var prefix = this.id,
                id = function (i) {
                    return prefix + i
                },
                refreshIntervalId,
                lastst = 0;

            function row(index, title) {
                var li = $('<li />');
                $('<img />').attr({
                    id: '%sazan_p%s'.format(prefix, index),
                    src: settings.arrowImageUrl
                }).appendTo(li);
                $('<label />').text(title).appendTo(li);
                $('<span />').attr({
                    id: '%sazan_t%s'.format(prefix, index)
                }).appendTo(li);
                return li;
            }

            function setCoordination() {
                var c = document.getElementById(id("cities"));
                var i = c.selectedIndex;
                if (i == 0) {
                    document.getElementById(id("longitude")).value = "";
                    document.getElementById(id("latitude")).value = "";
                }
                else {
                    document.getElementById(id("longitude")).value = settings.longitudes[i].toString();
                    document.getElementById(id("latitude")).value = settings.latitudes[i].toString();
                }
            }

            function hms(x) {
                x = Math.floor(3600 * x);
                var h = Math.floor(x / 3600);
                var mp = x - 3600 * h;
                var m = Math.floor(mp / 60);
                var s = Math.floor(mp - 60 * m);
                h = h + settings.dst;
                return (((h < 10) ? "0" : "") + h.toString() + ":" + ((m < 10) ? "0" : "") + m.toString() + ":" + ((s < 10) ? "0" : "") + s.toString())
            }

            function hhh(x) {
                x = Math.floor(3600 * x);
                var h = Math.floor(x / 3600);
                //var mp = x - 3600 * h;
                //var m = Math.floor(mp / 60);
                //var s = Math.floor(mp - 60 * m);
                return (((h < 10) ? "0" : "") + h.toString())
            }

            function mmm(x) {
                x = Math.floor(3600 * x);
                var h = Math.floor(x / 3600);
                var mp = x - 3600 * h;
                var m = Math.floor(mp / 60);
                //var s = Math.floor(mp - 60 * m);
                return (((m < 10) ? "0" : "") + m.toString())
            }


            function azanSun(m, d, h, lg) {
                if (m < 7)
                    d = 31 * (m - 1) + d + h / 24;
                else
                    d = 6 + 30 * (m - 1) + d + h / 24;
                var M = 74.2023 + 0.98560026 * d;
                var L = -2.75043 + 0.98564735 * d;
                var lst = 8.3162159 + 0.065709824 * Math.floor(d) + 1.00273791 * 24 * (d % 1) + lg / 15;
                var e = 0.0167065;
                var omega = 4.85131 - 0.052954 * d;
                var ep = 23.4384717 + 0.00256 * cosd(omega);
                var ed = 180.0 / Math.PI * e;
                var u = M;
                for (var i = 1; i < 5; i++)
                    u = u - (u - ed * sind(u) - M) / (1 - e * cosd(u));
                var v = 2 * atand(tand(u / 2) * Math.sqrt((1 + e) / (1 - e)));
                var theta = L + v - M - 0.00569 - 0.00479 * sind(omega);
                var delta = asind(sind(ep) * sind(theta));
                var alpha = 180.0 / Math.PI * Math.atan2(cosd(ep) * sind(theta), cosd(theta));
                if (alpha >= 360)
                    alpha -= 360;
                var ha = lst - alpha / 15;
                var zr = round(h - ha, 24);
                return ([zr, delta])
            }


            function azanShowDate() {
                var
                    a = new Date(),
                    day = a.getDate(),
                    highcmsmonth = a.getMonth() + 1;
                switch (highcmsmonth) {
                    case 1:
                        if (day < 21) {
                            highcmsmonth = 10;
                            day += 10;
                        } else {
                            highcmsmonth = 11;
                            day -= 20;
                        }
                        break;
                    case 2:
                        if (day < 20) {
                            highcmsmonth = 11;
                            day += 11;
                        } else {
                            highcmsmonth = 12;
                            day -= 19;
                        }
                        break;
                    case 3:
                        if (day < 21) {
                            highcmsmonth = 12;
                            day += 9;
                        } else {
                            highcmsmonth = 1;
                            day -= 20;
                        }
                        break;
                    case 4:
                        if (day < 21) {
                            highcmsmonth = 1;
                            day += 11;
                        } else {
                            highcmsmonth = 2;
                            day -= 20;
                        }
                        break;
                    case 5:
                    case 6:
                        if (day < 22) {
                            highcmsmonth -= 3;
                            day += 10;
                        } else {
                            highcmsmonth -= 2;
                            day -= 21;
                        }
                        break;
                    case 7:
                    case 8:
                    case 9:
                        if (day < 23) {
                            highcmsmonth -= 3;
                            day += 9;
                        } else {
                            highcmsmonth -= 2;
                            day -= 22;
                        }
                        break;
                    case 10:
                        if (day < 23) {
                            highcmsmonth = 7;
                            day += 8;
                        } else {
                            highcmsmonth = 8;
                            day -= 22;
                        }
                        break;
                    case 11:
                    case 12:
                        if (day < 22) {
                            highcmsmonth -= 3;
                            day += 9;
                        } else {
                            highcmsmonth -= 2;
                            day -= 21;
                        }
                        break;
                    default:
                        break;
                }
                document.getElementById(id("azanday")).value = day;
                document.getElementById(id("azanhighcmsmonth")).value = highcmsmonth;
            }

            function azanOffShowNow() {
                document.getElementById(id("azan_p1")).src = settings.arrowImageUrl;
                document.getElementById(id("azan_p2")).src = settings.arrowImageUrl;
                document.getElementById(id("azan_p3")).src = settings.arrowImageUrl;
                document.getElementById(id("azan_p4")).src = settings.arrowImageUrl;
                document.getElementById(id("azan_p5")).src = settings.arrowImageUrl;
            }

            function updateAzanAzan(v) {
                $('#%s'.format(id('azanazan'))).html(v);
            }

            function azanShowNow() {
                var today = new Date(),
                    azan_ttt = new Date(),
                    diff,
                    hh,
                    ss;

                azan_ttt.setHours(parseFloat(document.getElementById(id("azan_ht1")).value) + settings.dst);
                azan_ttt.setMinutes(document.getElementById(id("azan_mt1")).value);
                if (azan_ttt.getTime() - today.getTime() > 20) {
                    if (lastst != 1) {
                        azanOffShowNow();
                        document.getElementById(id("azan_p1")).src = settings.blinkerArrowImageUrl;
                        lastst = 1;
                    }
                    diff = azan_ttt.getTime() - today.getTime();
                    diff = Math.floor(diff / (1000 * 60 ));
                    hh = Math.floor(diff / ( 60 ));
                    ss = diff - (hh * 60);
                    if (ss > 59) {
                        ss = 0;
                        hh++
                    }
                    updateAzanAzan('%s:%s %s'.format(hh, ss, 'مانده تا اذان صبح'));
                }
                else {

                    if (azan_ttt.getTime() - today.getTime() < 20 && azan_ttt.getTime() - today.getTime() > -1) {
                        if (lastst != 1) {
                            azanOffShowNow();
                            document.getElementById(id("azan_p1")).src = settings.blinkerArrowImageUrl;
                            lastst = 1;
                        }
                        updateAzanAzan('%s %s'.format("اذان صبح به افق ", document.getElementById(id("cities")).value));
                    }

                    else {
                        azan_ttt = new Date();
                        azan_ttt.setHours(parseFloat(document.getElementById(id("azan_ht2")).value) + settings.dst);
                        azan_ttt.setMinutes(document.getElementById(id("azan_mt2")).value);
                        if (azan_ttt.getTime() - today.getTime() > 20) {
                            if (lastst != 2) {
                                azanOffShowNow();
                                document.getElementById(id("azan_p2")).src = settings.blinkerArrowImageUrl;
                                lastst = 2;
                            }
                            diff = azan_ttt.getTime() - today.getTime();
                            diff = Math.floor(diff / (1000 * 60 ));
                            hh = Math.floor(diff / ( 60 ));
                            ss = diff - (hh * 60);
                            updateAzanAzan('%s:%s %s'.format(hh, ss, 'مانده تا طلوع خورشید'));
                        }

                        else {
                            if (azan_ttt.getTime() - today.getTime() < 20 && azan_ttt.getTime() - today.getTime() > -1) {
                                if (lastst != 2) {
                                    azanOffShowNow();
                                    document.getElementById(id("azan_p2")).src = settings.blinkerArrowImageUrl;
                                    lastst = 2;
                                }
                                updateAzanAzan('طلوع خورشید');
                            }

                            else {

                                azan_ttt = new Date();
                                azan_ttt.setHours(parseFloat(document.getElementById(id("azan_ht3")).value) + settings.dst);
                                azan_ttt.setMinutes(document.getElementById(id("azan_mt3")).value);


                                if (azan_ttt.getTime() - today.getTime() > 20) {
                                    if (lastst != 3) {
                                        azanOffShowNow();
                                        document.getElementById(id("azan_p3")).src = settings.blinkerArrowImageUrl;
                                        lastst = 3;
                                    }
                                    diff = azan_ttt.getTime() - today.getTime();

                                    diff = Math.floor(diff / (1000 * 60 ));
                                    hh = Math.floor(diff / ( 60 ));

                                    ss = diff - (hh * 60);
                                    updateAzanAzan('%s:%s %s'.format(hh, ss, 'مانده تا اذان ظهر'));
                                }

                                else {

                                    if (azan_ttt.getTime() - today.getTime() < 20 && azan_ttt.getTime() - today.getTime() > -1) {
                                        if (lastst != 3) {
                                            azanOffShowNow();
                                            document.getElementById(id("azan_p3")).src = settings.blinkerArrowImageUrl;
                                            lastst = 3;
                                        }
                                        updateAzanAzan('%s %s'.format("اذان ظهر به افق ", document.getElementById(id("cities")).value));
                                    }

                                    else {

                                        azan_ttt = new Date();
                                        azan_ttt.setHours(parseFloat(document.getElementById(id("azan_ht4")).value) + settings.dst);
                                        azan_ttt.setMinutes(document.getElementById(id("azan_mt4")).value);
                                        //alert(azan_ttt.getTime( ) - today.getTime( ));
                                        if (azan_ttt.getTime() - today.getTime() > 20) {
                                            if (lastst != 4) {
                                                azanOffShowNow();
                                                document.getElementById(id("azan_p4")).src = settings.blinkerArrowImageUrl;
                                                lastst = 4;
                                            }
                                            diff = azan_ttt.getTime() - today.getTime();
                                            diff = Math.floor(diff / (1000 * 60 ));
                                            hh = Math.floor(diff / ( 60 ));
                                            ss = diff - (hh * 60);
                                            updateAzanAzan('%s:%s %s'.format(hh, ss, 'مانده تا غروب خورشید'));
                                        }
                                        else {
                                            if (azan_ttt.getTime() - today.getTime() < 20 && azan_ttt.getTime() - today.getTime() > -1) {
                                                if (lastst != 4) {
                                                    azanOffShowNow();
                                                    document.getElementById(id("azan_p4")).src = settings.blinkerArrowImageUrl;
                                                    lastst = 4;
                                                }
                                                updateAzanAzan('غروب خورشید');
                                            }
                                            else {

                                                azan_ttt = new Date();
                                                azan_ttt.setHours(parseFloat(document.getElementById(id("azan_ht5")).value) + settings.dst);
                                                azan_ttt.setMinutes(document.getElementById(id("azan_mt5")).value);
                                                if (azan_ttt.getTime() - today.getTime() > 20) {
                                                    if (lastst != 5) {
                                                        azanOffShowNow();
                                                        document.getElementById(id("azan_p5")).src = settings.blinkerArrowImageUrl;
                                                        lastst = 5;
                                                    }
                                                    diff = azan_ttt.getTime() - today.getTime();
                                                    diff = Math.floor(diff / (1000 * 60 ));
                                                    hh = Math.floor(diff / ( 60 ));
                                                    ss = diff - (hh * 60);
                                                    updateAzanAzan('%s:%s %s'.format(hh, ss, 'مانده تا اذان مغرب'));
                                                }
                                                else {

                                                    if (azan_ttt.getTime() - today.getTime() < 20 && azan_ttt.getTime() - today.getTime() > -1) {
                                                        if (lastst != 5) {
                                                            azanOffShowNow();
                                                            document.getElementById(id("azan_p5")).src = settings.blinkerArrowImageUrl;
                                                            lastst = 5;
                                                        }
                                                        updateAzanAzan('%s %s'.format("اذان مغرب به افق ", document.getElementById(id("cities")).value))
                                                    }
                                                    else {

                                                        azan_ttt = new Date();
                                                        azan_ttt.setHours(23);
                                                        azan_ttt.setMinutes(59);
                                                        diff = azan_ttt.getTime() - today.getTime();
                                                        diff = Math.floor(diff / (1000 * 60 ));
                                                        hh = Math.floor(diff / ( 60 ));
                                                        ss = diff - (hh * 60);


                                                        if (lastst != 1) {
                                                            azanOffShowNow();
                                                            document.getElementById(id("azan_p1")).src = settings.blinkerArrowImageUrl;
                                                            lastst = 1;
                                                        }
                                                        hh += Math.floor(document.getElementById(id("azan_ht1")).value);
                                                        ss += Math.floor(document.getElementById(id("azan_mt1")).value);
                                                        if (ss > 59) {
                                                            ss = ss - 59;
                                                            hh++
                                                        }
                                                        updateAzanAzan('%s:%s %s'.format(hh, ss, 'مانده تا اذان صبح'));
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

            }


            function refresh() {
                var delta, ha;
                azanShowDate();
                var i = document.getElementById(id("cities")).selectedIndex;
                if (i == 0)
                    return;
                var m = document.getElementById(id("azanhighcmsmonth")).value;
                var d = eval(document.getElementById(id("azanday")).value);
                var lg = eval(document.getElementById(id("longitude")).value);
                var lat = eval(document.getElementById(id("latitude")).value);
                var ep = azanSun(m, d, 4, lg);
                var zr = ep[0];
                delta = ep[1];
                ha = loc2hor(108.0, delta, lat);
                var t1 = round(zr - ha, 24);
                ep = azanSun(m, d, t1, lg);
                zr = ep[0];
                delta = ep[1];
                ha = loc2hor(108.0, delta, lat);
                t1 = round(zr - ha, 24);
                document.getElementById(id("azan_t1")).innerHTML = hms(t1);
                document.getElementById(id("azan_ht1")).value = hhh(t1);
                document.getElementById(id("azan_mt1")).value = mmm(t1);
                ep = azanSun(m, d, 6, lg);
                zr = ep[0];
                delta = ep[1];
                ha = loc2hor(90.833, delta, lat);
                var t2 = round(zr - ha, 24);
                ep = azanSun(m, d, t2, lg);
                zr = ep[0];
                delta = ep[1];
                ha = loc2hor(90.833, delta, lat);
                t2 = round(zr - ha, 24);
                document.getElementById(id("azan_t2")).innerHTML = hms(t2);
                document.getElementById(id("azan_ht2")).value = hhh(t2);
                document.getElementById(id("azan_mt2")).value = mmm(t2);
                ep = azanSun(m, d, 12, lg);
                ep = azanSun(m, d, ep[0], lg);
                zr = ep[0];
                document.getElementById(id("azan_t3")).innerHTML = hms(zr);
                document.getElementById(id("azan_ht3")).value = hhh(zr);
                document.getElementById(id("azan_mt3")).value = mmm(zr);
                ep = azanSun(m, d, 18, lg);
                zr = ep[0];
                delta = ep[1];
                ha = loc2hor(90.833, delta, lat);
                var t3 = round(zr + ha, 24);
                ep = azanSun(m, d, t3, lg);
                zr = ep[0];
                delta = ep[1];
                ha = loc2hor(90.833, delta, lat);
                t3 = round(zr + ha, 24);
                document.getElementById(id("azan_t4")).innerHTML = hms(t3);
                document.getElementById(id("azan_ht4")).value = hhh(t3);
                document.getElementById(id("azan_mt4")).value = mmm(t3);
                ep = azanSun(m, d, 18.5, lg);
                zr = ep[0];
                delta = ep[1];
                ha = loc2hor(94.3, delta, lat);
                var t4 = round(zr + ha, 24);
                ep = azanSun(m, d, t4, lg);
                zr = ep[0];
                delta = ep[1];
                ha = loc2hor(94.3, delta, lat);
                t4 = round(zr + ha, 24);
                document.getElementById(id("azan_t5")).innerHTML = hms(t4);
                document.getElementById(id("azan_ht5")).value = hhh(t4);
                document.getElementById(id("azan_mt5")).value = mmm(t4);
                azanShowNow();
            }

            function reload() {
                if (refreshIntervalId != null) {
                    clearInterval(refreshIntervalId);
                }
                refresh();
                refreshIntervalId = setInterval(refresh, 60000);
            }

            $(this)
                .append(inputHidden(id("latitude")))
                .append(inputHidden(id("azanday")))
                .append(inputHidden(id("azanhighcmsmonth")))
                .append(inputHidden(id("longitude")))
                .append(inputHidden(id("azan_ht1")))
                .append(inputHidden(id("azan_mt1")))
                .append(inputHidden(id("azan_ht2")))
                .append(inputHidden(id("azan_mt2")))
                .append(inputHidden(id("azan_ht3")))
                .append(inputHidden(id("azan_mt3")))
                .append(inputHidden(id("azan_ht4")))
                .append(inputHidden(id("azan_mt4")))
                .append(inputHidden(id("azan_ht5")))
                .append(inputHidden(id("azan_mt5")))


            $('<label />').attr({id: id('azanazan')}).addClass('azan-status').appendTo(this);

            $('<ul />')
                .append(row(1, 'اذان صبح'))
                .append(row(2, 'طلوع خورشید'))
                .append(row(3, 'اذان ظهر'))
                .append(row(4, 'غروب خورشید'))
                .append(row(5, 'اذان مغرب'))
                .appendTo(this);


            $('<label />').addClass('ofogh').text('اوقات به افق : ').appendTo(this);
            var select = $('<select />')
                .attr({id: id('cities')})
                .change(function () {
                    setCoordination();
                    reload();
                })
                .appendTo(this);

            for (var c in settings.cities) {
                $('<option />')
                    .attr({value: settings.cities[c]})
                    .text(settings.cities[c])
                    .appendTo(select);
            }

            $('#%scities'.format(prefix)).val(settings.city);

            setCoordination();
            reload();

            /* INIT END */

        });

        return this;
    }
}(jQuery));

