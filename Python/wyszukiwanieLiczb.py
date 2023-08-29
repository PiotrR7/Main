import re


tekst='''Adam Mickiewicz

Pan Tadeusz
czyli ostatni zajazd na Litwie


Księga pierwsza



Gospodarstwo

Powrót panicza — Spotkanie się pierwsze w pokoiku, drugie u stołu — Ważna Sędziego nauka o grzeczności — Podkomorzego uwagi polityczne nad modami — Początek sporu o Kusego i Sokoła — Żale Wojskiego — Ostatni Woźny Trybunału — Rzut oka na ówczesny stan polityczny Litwy i Europy

    Litwo! Ojczyzno moja! ty jesteś jak zdrowie:
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

    Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(Gdy od płaczącej matki, pod Twoją opiekę
Ofiarowany, martwą podniosłem powiekę;
I zaraz mogłem pieszo, do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono.
Tymczasem przenoś moją duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą.

    Śród takich pól przed laty, nad brzegiem ruczaju,
Na pagórku niewielkim, we brzozowym gaju,
Stał dwór szlachecki, z drzewa, lecz podmurowany;
Świeciły się z daleka pobielane ściany,
Tym bielsze, że odbite od ciemnej zieleni
Topoli, co go bronią od wiatrów jesieni.
Dom mieszkalny niewielki, lecz zewsząd chędogi,
I stodołę miał wielką, i przy niej trzy stogi
Użątku, co pod strzechą zmieścić się nie może.
Widać, że okolica obfita we zboże,
I widać z liczby kopic, co wzdłuż i wszerz smugów
Świecą gęsto jak gwiazdy, widać z liczby pługów
Orzących wcześnie łany ogromne ugoru,
Czarnoziemne, zapewne należne do dworu,
Uprawne dobrze na kształt ogrodowych grządek:
Że w tym domu dostatek mieszka i porządek.
Brama na wciąż otwarta przechodniom ogłasza,
Że gościnna, i wszystkich w gościnę zaprasza.

    Właśnie dwukonną bryką wjechał młody panek
I obiegłszy dziedziniec zawrócił przed ganek.
Wysiadł z powozu; konie porzucone same,
Szczypiąc trawę ciągnęły powoli pod bramę.
We dworze pusto: bo drzwi od ganku zamknięto
Zaszczepkami i kołkiem zaszczepki przetknięto.
Podróżny do folwarku nie biegł sług zapytać,
Odemknął, wbiegł do domu, pragnął go powitać.
Dawno domu nie widział, bo w dalekim mieście
Kończył nauki, końca doczekał nareszcie.
Wbiega i okiem chciwie ściany starodawne
Ogląda czule, jako swe znajome dawne.
Też same widzi sprzęty, też same obicia,
Z którymi się zabawiać lubił od powicia,
Lecz mniej wielkie, mniej piękne niż się dawniej zdały.
I też same portrety na ścianach wisiały:
Tu Kościuszko w czamarce krakowskiej, z oczyma
Podniesionymi w niebo, miecz oburącz trzyma;
Takim był, gdy przysięgał na stopniach ołtarzów,
Że tym mieczem wypędzi z Polski trzech mocarzów,
Albo sam na nim padnie. Dalej w polskiej szacie
Siedzi Rejtan, żałośny po wolności stracie;
W ręku trzyma nóż ostrzem zwrócony do łona,
A przed nim leży Fedon i żywot Katona.
Dalej Jasiński, młodzian piękny i posępny;
Obok Korsak, towarzysz jego nieodstępny:
Stoją na szańcach Pragi, na stosach Moskali,
Siekąc wrogów, a Praga już się wkoło pali.
Nawet stary stojący zegar kurantowy
W drewnianej szafie poznał, u wniścia alkowy;
I z dziecinną radością pociągnął za sznurek,
By stary Dąbrowskiego usłyszeć mazurek.

    Biegał po całym domu i szukał komnaty,
Gdzie mieszkał dzieckiem będąc, przed dziesięciu laty.
Wchodzi, cofnął się, toczył zdumione źrenice
Po ścianach: w tej komnacie mieszkanie kobiéce!
Któż by tu mieszkał? Stary stryj nie był żonaty;
A ciotka w Petersburgu mieszkała przed laty.
To nie był ochmistrzyni pokój? Fortepiano?
Na nim nuty i książki; wszystko porzucano
Niedbale i bezładnie: nieporządek miły!
Niestare były rączki, co je tak rzuciły.
Tuż i sukienka biała, świeżo z kołka zdjęta
Do ubrania, na krzesła poręczu rozpięta;
A na oknach donice z pachnącymi ziołki,
Geranium, lewkonija, astry i fijołki.
Podróżny stanął w jednym z okien — nowe dziwo:
W sadzie, na brzegu niegdyś zarosłym pokrzywą,
Był maleńki ogródek ścieżkami porznięty,
Pełen bukietów trawy angielskiej i mięty.
Drewniany, drobny, w cyfrę powiązany płotek
Połyskał się wstążkami jaskrawych stokrotek;
Grządki, widać, że były świeżo polewane,
Tuż stało wody pełne naczynie blaszane,
Ale nigdzie nie widać było ogrodniczki;
Tylko co wyszła: jeszcze kołyszą się drzwiczki
Świeżo trącone, blisko drzwi ślad widać nóżki
Na piasku, bez trzewika była i pończoszki;
Na piasku drobnym, suchym, białym na kształt śniegu,
Ślad wyraźny, lecz lekki, odgadniesz, że w biegu
Chybkim był zostawiony nóżkami drobnemi
Od kogoś, co zaledwie dotykał się ziemi.

    Podróżny długo w oknie stał patrząc, dumając,
Wonnymi powiewami kwiatów oddychając.
Oblicze aż na krzaki fijołkowe skłonił,
Oczyma ciekawymi po drożynach gonił
I znowu je na drobnych śladach zatrzymywał,
Myślał o nich i, czyje były, odgadywał.
Przypadkiem oczy podniósł, i tuż na parkanie
Stała młoda dziewczyna… Białe jej ubranie
Wysmukłą postać tylko aż do piersi kryje,
Odsłaniając ramiona i łabędzią szyję.
W takim Litwinka tylko chodzić zwykła z rana,
W takim nigdy nie bywa od mężczyzn widziana:
Więc choć świadka nie miała, założyła ręce
Na piersiach, przydawając zasłony sukience.
Włos w pukle nierozwity, lecz w węzełki małe
Pokręcony, schowany w drobne strączki białe,
Dziwnie ozdabiał głowę: bo od słońca blasku
Świecił się jak korona na świętych obrazku.
Twarzy nie było widać; zwrócona na pole
Szukała kogoś okiem, daleko, na dole;
Ujrzała, zaśmiała się i klasnęła w dłonie,
Jak biały ptak zleciała z parkanu na błonie,
I wionęła ogrodem, przez płotki, przez kwiaty,
I po desce opartej o ścianę komnaty…
Nim spostrzegł się, wleciała przez okno, świecąca,
Nagła, cicha i lekka, jak światłość miesiąca.
Nucąc chwyciła suknie, biegła do zwierciadła:
Wtem ujrzała młodzieńca i z rąk jej wypadła
Suknia, a twarz od strachu i dziwu pobladła.
Twarz podróżnego barwą spłonęła rumianą,
Jak obłok, gdy z jutrzenką napotka się raną.
Skromny młodzieniec oczy zmrużył i przysłonił,
Chciał coś mówić, przepraszać; tylko się ukłonił
I cofnął się. Dziewica krzyknęła boleśnie,
Niewyraźnie, jak dziecko przestraszone we śnie;
Podróżny zląkł się, spojrzał; lecz już jej nie było.
Wyszedł zmieszany i czuł, że mu serce biło
Głośno, i sam nie wiedział, czy go miało śmieszyć
To dziwaczne spotkanie, czy wstydzić, czy cieszyć.

    Tymczasem na folwarku nie uszło baczności,
Że przed ganek zajechał któryś z nowych gości.
Już konie w stajnią wzięto, już im hojnie dano,
Jako w porządnym domu, i obrok, i siano:
Bo Sędzia nigdy nie chciał, według nowej mody,
Odsyłać koni gości Żydom do gospody.
Słudzy nie wyszli witać; ale nie myśl wcale,
Aby w domu Sędziego służono niedbale:
Słudzy czekają, nim się pan Wojski ubierze,
Który teraz za domem urządzał wieczerzę.
On pana zastępuje i on, w niebytności
Pana, zwykł sam przyjmować i zabawiać gości
(Daleki krewny pański i przyjaciel domu).
Widząc gościa, na folwark dążył po kryjomu,
Bo nie mógł wyjść spotykać w tkackim pudermanie;
Wdział więc jak mógł najprędzej niedzielne ubranie
Nagotowane z rana, bo od rana wiedział,
Że u wieczerzy będzie z mnóstwem gości siedział.

    Pan Wojski poznał z dala, ręce rozkrzyżował
I z krzykiem podróżnego ściskał i całował.
Zaczęła się ta prędka, zmieszana rozmowa,
W której lat kilku dzieje chciano zamknąć w słowa
Krótkie i poplątane, w ciąg powieści, pytań,
Wykrzykników i westchnień, i nowych powitań.
Gdy się pan Wojski dosyć napytał, nabadał,
Na samym końcu dzieje tego dnia powiadał.

    «Dobrze mój Tadeuszu, (bo tak nazywano
Młodzieńca, który nosił Kościuszkowskie miano
Na pamiątkę, że w czasie wojny się urodził)
Dobrze mój Tadeuszu, żeś się dziś nagodził
Do domu, właśnie kiedy mamy panien wiele.
Stryjaszek myśli wkrótce sprawić ci wesele;
Jest z czego wybrać; u nas towarzystwo liczne
Od dni kilku zbiera się na sądy graniczne,
Dla skończenia dawnego z panem Hrabią sporu.
I pan Hrabia ma jutro sam zjechać do dworu;
Podkomorzy już zjechał z żoną i z córkami.
Młodzież poszła do lasu bawić się strzelbami,
A starzy i kobiety żniwo oglądają
Pod lasem i tam pewnie na młodzież czekają.
Pójdziemy, jeśli zechcesz, i wkrótce spotkamy
Stryjaszka, Podkomorstwo i szanowne damy».

    Pan Wojski z Tadeuszem idą pod las drogą,
I jeszcze się do woli nagadać nie mogą.

Słońce ostatnich kresów nieba dochodziło,
Mniej silnie, ale szerzej niż we dnie świeciło,
Całe zaczerwienione, jak zdrowe oblicze
Gospodarza, gdy prace skończywszy rolnicze
Na spoczynek powraca. Już krąg promienisty
Spuszcza się na wierzch boru i już pomrok mglisty,
Napełniając wierzchołki i gałęzie drzewa,
Cały las wiąże w jedno i jakoby zlewa;
I bór czernił się na kształt ogromnego gmachu,
Słońce nad nim czerwone jak pożar na dachu.
Wtem zapadło do głębi; jeszcze przez konary
Błysnęło, jako świeca przez okiennic szpary,
I zgasło. I wnet sierpy gromadnie dzwoniące
We zbożach, i grabliska suwane po łące,
Ucichły i stanęły: tak pan Sędzia każe,
U niego ze dniem kończą pracę gospodarze.
«Pan świata wie, jak długo pracować potrzeba;
Słońce, Jego robotnik, kiedy znijdzie z nieba,
Czas i ziemianinowi ustępować z pola».
Tak zwykł mawiać pan Sędzia, a Sędziego wola
Była Ekonomowi poczciwemu świętą;
Bo nawet wozy, w które już składać zaczęto
Kopę żyta, niepełne jadą do stodoły:
Cieszą się z niezwyczajnej ich lekkości woły.

    Właśnie z lasu wracało towarzystwo całe,
Wesołe, lecz w porządku. Naprzód dzieci małe
Z dozorcą, potem Sędzia szedł z Podkomorzyną,
Obok pan Podkomorzy otoczon rodziną;
Panny tuż za starszymi, a młodzież na boku;
Panny szły przed młodzieżą o jakie pół kroku
(Tak każe przyzwoitość). Nikt tam nie rozprawiał
O porządku, nikt mężczyzn i dam nie ustawiał:
A każdy mimowolnie porządku pilnował;
Bo Sędzia w domu dawne obyczaje chował,
I nigdy nie dozwalał, by chybiano względu
Dla wieku, urodzenia, rozumu, urzędu.
Tym ładem, mawiał, domy i narody słyną,
Z jego upadkiem domy i narody giną.
Więc do porządku wykli domowi i słudzy;
I przyjezdny gość, krewny albo człowiek cudzy,
Gdy Sędziego nawiedził, skoro pobył mało,
Przyjmował zwyczaj, którym wszystko oddychało.

    Krótkie były Sędziego z synowcem witania:
Dał mu poważnie rękę do pocałowania,
I w skroń ucałowawszy uprzejmie pozdrowił;
A choć przez wzgląd na gości niewiele z nim mówił,
Widać było z łez, które wylotem kontusza
Otarł prędko, jak kochał pana Tadeusza.

    W ślad gospodarza wszystko ze żniwa i z boru,
I z łąk, i z pastwisk razem wracało do dworu.
Tu owiec trzoda becząc w ulice się tłoczy
I wznosi chmurę pyłu; dalej z wolna kroczy
Stado cielic tyrolskich z mosiężnymi dzwonki;
Tam konie rżące lecą ze skoszonej łąki:
Wszystko bieży ku studni, której ramię z drzewa
Raz wraz skrzypi i napój w koryta rozlewa.

    Sędzia, choć utrudzony, chociaż w gronie gości,
Nie chybił gospodarskiej, ważnej powinności:
Udał się sam ku studni. Najlepiej z wieczora
Gospodarz widzi, w jakim stanie jest obora.
Dozoru tego nigdy sługom nie poruczy;
Bo Sędzia wie, że oko pańskie konia tuczy.

    Wojski z Woźnym Protazym ze świecami w sieni
Stali i rozprawiali, nieco poróżnieni:
Bo w niebytność Wojskiego Woźny po kryjomu
Kazał stoły z wieczerzą powynosić z domu,
I ustawić co prędzej w pośrodku zamczyska,
Którego widne były pod lasem zwaliska.
Po cóż te przenosiny? Pan Wojski się krzywił
I przepraszał Sędziego; Sędzia się zadziwił,
Lecz stało się: już późno i trudno zaradzić,
Wolał gości przeprosić i w pustki prowadzić.
Po drodze Woźny ciągle Sędziemu tłumaczył,
Dlaczego urządzenie pańskie przeinaczył:
We dworze żadna izba nie ma obszerności
Dostatecznej dla tylu, tak szanownych gości,
W zamku sień wielka, jeszcze dobrze zachowana,
Sklepienie całe — wprawdzie pękła jedna ściana,
Okna bez szyb, lecz latem nic to nie zawadzi;
Bliskość piwnic wygodna służącej czeladzi.
Tak mówiąc na Sędziego mrugał; widać z miny,
Że miał i taił inne, ważniejsze przyczyny.

    O dwa tysiące kroków zamek stał za domem,
Okazały budową, poważny ogromem,
Dziedzictwo starożytnej rodziny Horeszków;
Dziedzic zginął był w czasie krajowych zamieszków.
Dobra całe zniszczone sekwestrami rządu,
Bezładnością opieki, wyrokami sądu,
W cząstce spadły dalekim krewnym po kądzieli,
A resztę rozdzielono między wierzycieli.
Zamku żaden wziąć nie chciał, bo w szlacheckim stanie
Trudno było wyłożyć koszt na utrzymanie;
Lecz Hrabia, sąsiad bliski, gdy wyszedł z opieki,
Panicz bogaty, krewny Horeszków daleki,
Przyjechawszy z wojażu upodobał mury,
Tłumacząc, że gotyckiej są architektury;
Choć Sędzia z dokumentów przekonywał o tem,
Że architekt był majstrem z Wilna, nie zaś Gotem.
Dość, że Hrabia chciał zamku. Właśnie i Sędziemu
Przyszła nagle taż chętka, nie wiadomo czemu.
Zaczęli proces w ziemstwie, potem w głównym sądzie,
W senacie, znowu w ziemstwie i guberskim rządzie;
Wreszcie, po wielu kosztach i ukazach licznych,
Sprawa wróciła znowu do sądów granicznych.

    Słusznie Woźny powiadał, że w zamkowej sieni
Zmieści się i palestra, i goście proszeni.
Sień wielka jak refektarz, z wypukłym sklepieniem
Na filarach, podłoga wysłana kamieniem,
Ściany bez żadnych ozdób, ale mur chędogi;
Sterczały wkoło sarnie i jelenie rogi
Z napisami, gdzie, kiedy te łupy zdobyte;
Tuż myśliwców herbowne klejnoty wyryte,
I stoi wypisany każdy po imieniu;
Herb Horeszków, Półkozic, jaśniał na sklepieniu.

    Goście weszli w porządku i stanęli kołem.
Podkomorzy najwyższe brał miejsce za stołem;
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się damom, starcom i młodzieży.
Przy nim stał kwestarz, Sędzia tuż przy bernardynie.
Bernardyn zmówił krótki pacierz po łacinie;
Mężczyznom dano wódkę; wtenczas wszyscy siedli,
I chołodziec litewski milcząc żwawo jedli.

    Pan Tadeusz, choć młodzik, ale prawem gościa
Wysoko siadł przy damach obok jegomościa;
Między nim i stryjaszkiem jedno pozostało
Puste miejsce, jak gdyby na kogoś czekało.
Stryj nieraz na to miejsce i na drzwi poglądał,
Jakby czyjegoś przyjścia był pewny i żądał.
I Tadeusz wzrok stryja ku drzwiom odprowadzał,
I z nim na miejscu pustym oczy swe osadzał.
Dziwna rzecz! miejsca wkoło są siedzeniem dziewic,
Na które mógłby spojrzeć bez wstydu królewic,
Wszystkie zacnie zrodzone, każda młoda, ładna:
Tadeusz tam pogląda, gdzie nie siedzi żadna.
To miejsce jest zagadką; młodź lubi zagadki;
Roztargniony, do swojej nadobnej sąsiadki
Ledwo słów kilka wyrzekł, do Podkomorzanki;
Nie zmienia jej talerzów, nie nalewa szklanki,
I panien nie zabawia przez rozmowy grzeczne,
Z których by wychowanie poznano stołeczne;
To jedno puste miejsce nęci go i mami,
Już nie puste, bo on je napełnił myślami.
Po tym miejscu biegało domysłów tysiące,
Jako po deszczu żabki na samotnej łące;
Śród nich jedna króluje postać, jak w pogodę
Lilia jezior skroń białą wznosząca nad wodę.

    Dano trzecią potrawę. Wtem pan Podkomorzy,
Wlawszy kropelkę wina w szklankę panny Róży,
A młodszej przysunąwszy z talerzem ogórki,
Rzekł: «Muszę ja wam służyć, moje panny córki,
Choć stary i niezgrabny». Zatem się rzuciło
Kilku młodych od stołu i pannom służyło.
Sędzia, z boku rzuciwszy wzrok na Tadeusza
I poprawiwszy nieco wylotów kontusza,
Nalał węgrzyna i rzekł: «Dziś, nowym zwyczajem,
My na naukę młodzież do stolicy dajem;
I nie przeczym, że nasi synowie i wnuki
Mają od starych więcej książkowej nauki;
Ale co dzień postrzegam, jak młodź cierpi na tem,
Że nie ma szkół uczących żyć z ludźmi i światem.
Dawniej na dwory pańskie jachał szlachcic młody;
Ja sam lat dziesięć byłem dworskim Wojewody,
Ojca Podkomorzego, mościwego pana
(Mówiąc, Podkomorzemu ścisnął za kolana);
On mnie radą do usług publicznych sposobił,
Z opieki nie wypuścił, aż człowiekiem zrobił.
W mym domu wiecznie będzie jego pamięć droga,
Co dzień za duszę jego proszę Pana Boga.
Jeślim tyle na jego nie korzystał dworze
Jak drudzy, i wróciwszy w domu ziemię orzę,
Gdy inni, więcej godni Wojewody względów,
Doszli potem najwyższych krajowych urzędów,
Przynajmniej tom skorzystał, że mi w moim domu
Nikt nigdy nie zarzuci, bym uchybił komu
W uczciwości, w grzeczności; a powiem to śmiało,
Grzeczność nie jest nauką łatwą ani małą.
Niełatwą, bo nie na tym kończy się, jak nogą
Zręcznie wierzgnąć, z uśmiechem witać lada kogo;
Bo taka grzeczność modna, zda mi się kupiecka,
Ale nie staropolska, ani też szlachecka.
Grzeczność wszystkim należy, lecz każdemu inna;
Bo nie jest bez grzeczności i miłość dziecinna,
I wzgląd męża dla żony przy ludziach, i pana
Dla sług swoich, a w każdej jest pewna odmiana.
Trzeba się długo uczyć, ażeby nie zbłądzić
I każdemu powinną uczciwość wyrządzić.
I starzy się uczyli; u panów rozmowa,
Była to historyja żyjąca krajowa,
A między szlachtą dzieje domowe powiatu.
Dawano przez to poznać szlachcicowi bratu,
Że wszyscy o nim wiedzą, lekce go nie ważą;
Więc szlachcic obyczaje swe trzymał pod strażą.
Dziś człowieka nie pytaj: co zacz? kto go rodzi?
Z kim on żył? co porabiał? Każdy gdzie chce wchodzi,
Byle nie szpieg rządowy i byle nie w nędzy.
Jak ów Wespazyjanus nie wąchał pieniędzy
I nie chciał wiedzieć, skąd są, z jakich rąk i krajów,
Tak nie chcą znać człowieka rodu, obyczajów!
Dość, że ważny i że się stempel na nim widzi,
Więc szanują przyjaciół jak pieniądze Żydzi».

    To mówiąc, Sędzia gości obejrzał porządkiem;
Bo choć zawsze i płynnie mówił, i z rozsądkiem,
Wiedział, że niecierpliwa młodzież teraźniejsza,
Że ją nudzi rzecz długa, choć najwymowniejsza.
Ale wszyscy słuchali w milczeniu głębokiem.
Sędzia Podkomorzego zdał się radzić okiem;
Podkomorzy pochwałą rzeczy nie przerywał,
Ale częstym skinieniem głowy potakiwał.
Sędzia milczał, on jeszcze skinieniem przyzwalał;
Więc Sędzia jego puchar i swój kielich nalał,
I dalej mówił: «Grzeczność nie jest rzeczą małą:
Kiedy się człowiek uczy ważyć, jak przystało,
Drugich wiek, urodzenie, cnoty, obyczaje,
Wtenczas i swoją ważność zarazem poznaje:
Jak na szalach, żebyśmy nasz ciężar poznali,
Musim kogoś posadzić na przeciwnej szali.
Zaś godna jest waszmościów uwagi osobnej
Grzeczność, którą powinna młodź dla płci nadobnej;
Zwłaszcza gdy zacność domu, fortuny szczodroty
Objaśniają wrodzone wdzięki i przymioty.
Stąd droga do afektów i stąd się kojarzy
Wspaniały domów sojusz. Tak myślili starzy.
A zatem…» Tu Pan Sędzia nagłym zwrotem głowy
Skinął na Tadeusza, rzucił wzrok surowy:
Znać było, że przychodził już do wniosków mowy.

    Wtem brząknął w tabakierę złotą Podkomorzy,
I rzekł: «Mój Sędzio, dawniej było jeszcze gorzéj!
Teraz, nie wiem, czy moda i nas starych zmienia,
Czy młodzież lepsza, ale widzę mniej zgorszenia.
Ach, ja pamiętam czasy, kiedy do ojczyzny,
Pierwszy raz zawitała moda francuszczyzny!
Gdy raptem paniczyki młode z cudzych krajów
Wtargnęli do nas hordą gorszą od Nogajów,
Prześladując w ojczyźnie Boga, przodków wiarę,
Prawa i obyczaje, nawet suknie stare.
Żałośnie było widzieć wyżółkłych młokosów,
Gadających przez nosy, a często bez nosów,
Opatrzonych w broszurki i w różne gazety,
Głoszących nowe wiary, prawa, toalety.
Miała nad umysłami wielką moc ta tłuszcza;
Bo Pan Bóg, kiedy karę na naród przypuszcza,
Odbiera naprzód rozum od obywateli.
I tak, mędrsi fircykom oprzeć się nie śmieli,
I zląkł ich się jak dżumy jakiej cały naród,
Bo już sam wewnątrz siebie czuł choroby zaród.
Krzyczano na modnisiów, a brano z nich wzory;
Zmieniano wiarę, mowę, prawa i ubiory.
Była to maszkarada, zapustna swawola,
Po której miał przyjść wkrótce wielki post — niewola!

    Pamiętam, chociaż byłem wtenczas małe dziecię,
Kiedy do ojca mego, w Oszmiańskim powiecie,
Przyjechał pan Podczaszyc na francuskim wózku,
Pierwszy człowiek, co w Litwie chodził po francusku.
Biegali wszyscy za nim, jakby za rarogiem,
Zazdroszczono domowi, przed którego progiem
Stanęła Podczaszyca dwukolna dryndulka,
Która się po francusku zwała karyjulka:
Zamiast lokajów, w kielni siedziały dwa pieski,
A na kozłach Niemczysko chude na kształt deski;
Nogi miał długie, cienkie jak od chmielu tyki,
W pończochach, ze srebrnymi klamrami trzewiki,
Peruka z harbajtelem zawiązanym w miechu.
Starzy na on ekwipaż parskali ze śmiechu,
A chłopi żegnali się, mówiąc: że po świecie
Jeździ wenecki diabeł w niemieckiej karecie.
Sam Podczaszyc jaki był, opisywać długo;
Dosyć, że się nam zdawał małpą lub papugą
W wielkiej peruce, którą do złotego runa
On lubił porównywać, a my do kołtuna.
Jeśli kto i czuł wtenczas, że polskie ubranie
Piękniejsze jest niż obcej mody małpowanie,
Milczał; bo by krzyczała młodzież, że przeszkadza
Kulturze, że tamuje progresy, że zdradza!
Taka była przesądów owoczesnych władza!

    Podczaszyc zapowiedział, że nas reformować,
Cywilizować będzie i konstytuować;
Ogłosił nam, że jacyś Francuzi wymówni
Zrobili wynalazek: iż ludzie są równi…
Choć o tym dawno w Pańskim pisano Zakonie,
I każdy ksiądz toż samo gada na ambonie.
Nauka dawną była, szło o jej pełnienie!
Lecz wtenczas panowało takie oślepienie,
Że nie wierzono rzeczom najdawniejszym w świecie,
Jeśli ich nie czytano w francuskiej gazecie.
Podczaszyc, mimo równość, wziął tytuł markiża;
Wiadomo, że tytuły przychodzą z Paryża,
A natenczas tam w modzie był tytuł markiża.
Jakoż, kiedy się moda odmieniła z laty,
Tenże sam markiż przybrał tytuł demokraty;
Wreszcie z odmienną modą, pod Napoleonem,
Demokrata przyjechał z Paryża baronem;
Gdyby żył dłużej, może nową alternatą,
Z barona przechrzciłby się kiedyś demokratą.
Bo Paryż częstą mody odmianą się chlubi;
A co Francuz wymyśli, to Polak polubi.

    Chwała Bogu, że teraz, jeśli nasza młodzież
Wyjeżdża za granicę, to już nie po odzież,
Nie szukać prawodawstwa w drukarskich kramarniach
Lub wymowy uczyć się w paryskich kawiarniach.
Bo teraz Napoleon, człek mądry a prędki,
Nie daje czasu szukać mody i gawędki.
Teraz grzmi oręż, a nam starym serca rosną,
Że znowu o Polakach tak na świecie głośno;
Jest sława, a więc będzie i Rzeczpospolita!
Zawżdy z wawrzynów drzewo wolności wykwita.
Tylko smutno, że nam, ach, tak się lata wleką
W nieczynności! a oni tak zawsze daleko!
Tak długo czekać! nawet tak rzadka nowina —
Ojcze Robaku (ciszej rzekł do bernardyna),
Słyszałem, żeś zza Niemna odebrał wiadomość;
Może też co o naszym wojsku wie Jegomość?»
— «Nic a nic» odpowiedział Robak obojętnie,
(Widać było, że słuchał rozmowy niechętnie)
«Mnie polityka nudzi; jeżeli z Warszawy
Mam list, to rzecz zakonna, to są nasze sprawy
Bernardyńskie: cóż o tym gadać u wieczerzy;
Są tu świeccy, do których nic to nie należy».

    Tak mówiąc, spojrzał zyzem, gdzie śród biesiadników
Siedział gość, Moskal; był to pan kapitan Ryków,
Stary żołnierz, stał w bliskiej wiosce na kwaterze,
Pan Sędzia go przez grzeczność prosił na wieczerzę.
Ryków jadł smaczno, mało wdawał się w rozmowę,
Lecz na wzmiankę Warszawy, rzekł podniósłszy głowę:
«Pan Podkomorzy! Oj wy! Pan zawsze ciekawy
O Bonaparta, zawsze wam tam do Warszawy!
He! Ojczyzna! Ja nie szpieg, a po polsku umiem, —
Ojczyzna! ja to czuję wszystko, ja rozumiem!
Wy Polaki, ja Ruski: teraz się nie bijem,
Jest armistycjum, to my razem jemy, pijem.
Często na awanpostach nasz z Francuzem gada,
Pije wódkę; jak krzykną ura! — kanonada.
Ruskie przysłowie: z kim się biję, tego lubię;
Gładź drużkę jak po duszy, a bij jak po szubie.
Ja mówię, będzie wojna u nas. Do Majora
Płuta, adiutant sztabu przyjechał zawczora:
Gotować się do marszu! Pójdziem, czy pod Turka,
Czy na Francuza; oj ten Bonapart figurka!
Bez Suwarowa to on może nas wytuza.
U nas w pułku gadano, jak szli na Francuza,
Że Bonapart czarował: no, tak i Suwarów
Czarował; tak były czary przeciw czarów.
Raz w bitwie, gdzie podział się? szukać Bonaparta,—
A on zmienił się w lisa, tak Suwarów w charta;
Tak Bonaparte znowu w kota się przerzuca,
Dalej drzeć pazurami, a Suwarów w kuca.
Obaczcież, co się stało w końcu z Bonapartą…»
Tu Ryków przerwał i jadł; wtem, z potrawą czwartą
Wszedł służący i raptem boczne drzwi otwarto.

    Weszła nowa osoba przystojna i młoda.
Jej zjawienie się nagłe, jej wzrost i uroda,
Jej ubiór zwrócił oczy; wszyscy ją witali,
Prócz Tadeusza widać, że ją wszyscy znali.
Kibić miała wysmukłą, kształtną, pierś powabną,
Suknię materyjalną, różową, jedwabną,
Gors wycięty, kołnierzyk z koronek, rękawki
Krótkie; w ręku kręciła wachlarz dla zabawki
(Bo nie było gorąco); wachlarz pozłocisty
Powiewając rozlewał deszcz iskier rzęsisty;
Głowa do włosów, włosy pozwijane w kręgi,
W pukle, i przeplatane różowymi wstęgi,
Pośród nich brylant, niby zakryty od oczu,
Świecił się jako gwiazda w komety warkoczu:
Słowem, ubiór galowy; szeptali niejedni,
Że zbyt wykwintny na wieś i na dzień powszedni.
Nóżek, choć suknia krótka, oko nie zobaczy,
Bo biegła bardzo szybko, suwała się raczéj
Jako osóbki, które na trzykrólskie święta
Przesuwają w jasełkach ukryte chłopięta.
Biegła i wszystkich lekkim witając ukłonem,
Chciała usieść na miejscu sobie zostawionem:
Trudno było; bo krzeseł dla gości nie stało,
Na czterech ławach cztery ich rzędy siedziało:
Trzeba było rzęd ruszyć lub ławę przeskoczyć;
Zręcznie między dwie ławy umiała się wtłoczyć,
A potem, między rzędem siedzących i stołem,
Jak bilardowa kula toczyła się kołem.
W biegu dotknęła blisko naszego młodziana;
Uczepiwszy falbaną o czyjeś kolana,
Pośliznęła się nieco i w tym roztargnieniu
Na pana Tadeusza wsparła się ramieniu.
Przeprosiwszy go grzecznie, na miejscu swym siadła
Pomiędzy nim i stryjem, ale nic nie jadła;
Tylko się wachlowała, to wachlarza trzonek
Kręciła, to kołnierzyk z brabanckich koronek
Poprawiała, to lekkim dotknięciem się ręki
Muskała włosów pukle i wstąg jasnych pęki.

    Ta przerwa rozmów trwała już minut ze cztery.
Tymczasem, w końcu stoła, naprzód ciche szmery,
A potem się zaczęły wpół głośne rozmowy;
Mężczyźni rozsądzali swe dzisiejsze łowy.
Asesora z Rejentem wzmogła się uparta
Coraz głośniejsza kłótnia o kusego charta,
Którego posiadaniem pan Rejent się szczycił
I utrzymywał, że on zająca pochwycił;
Asesor zaś dowodził na złość Rejentowi,
Że ta chwała należy chartu Sokołowi.
Pytano zdania innych; więc wszyscy dokoła
Brali stronę Kusego albo też Sokoła,
Ci jak znawcy, ci znowu jak naoczne świadki.
Sędzia na drugim końcu do nowej sąsiadki
Rzekł półgłosem: «Przepraszam, musieliśmy siadać,
Nie podobna wieczerzy na później odkładać:
Goście głodni, chodzili daleko na pole;
Myśliłem, że dziś z nami nie będziesz przy stole».
To rzekłszy, z Podkomorzym przy pełnym kielichu
O politycznych sprawach rozmawiał po cichu.

    Gdy tak były zajęte stołu strony obie,
Tadeusz przyglądał się nieznanej osobie.
Przypomniał, że za pierwszym na miejsce wejrzeniem
Odgadnął zaraz, czyim miało być siedzeniem.
Rumienił się, serce mu biło nadzwyczajnie:
Więc rozwiązane widział swych domysłów tajnie!
Więc było przeznaczono, by przy jego boku
Usiadła owa piękność widziana w pomroku!
Wprawdzie zdała się teraz wzrostem dorodniejsza,
Bo ubrana, a ubiór powiększa i zmniejsza.
I włos u tamtej widział krótki, jasnozłoty,
A u tej krucze długie zwijały się sploty?
Kolor musiał pochodzić od słońca promieni,
Którymi przy zachodzie wszystko się czerwieni.
Twarzy wówczas nie dostrzegł, nazbyt rychło znikła;
Ale myśl twarz nadobną odgadywać zwykła:
Myślił, że pewnie miała czarniutkie oczęta,
Białą twarz, usta kraśne jak wiśnie bliźnięta;
U tej znalazł podobne oczy, usta, lica.
W wieku może by była największa różnica:
Ogrodniczka dziewczynką zdawała się małą,
A pani ta niewiastą już w latach dojrzałą;
Lecz młodzież o piękności metrykę nie pyta,
Bo młodzieńcowi młodą jest każda kobiéta,
Chłopcowi każda piękność zda się rówiennicą,
A niewinnemu każda kochanka dziewicą.

    Tadeusz, chociaż liczył lat blisko dwadzieście,
I od dzieciństwa mieszkał w Wilnie, wielkim mieście,
Miał za dozorcę księdza, który go pilnował
I w dawnej surowości prawidłach wychował.
Tadeusz zatem przywiózł w strony swe rodzinne
Duszę czystą, myśl żywą i serce niewinne,
Ale razem niemałą chętkę do swawoli.
Z góry już robił projekt, że sobie pozwoli
Używać na wsi długo wzbronionej swobody;
Wiedział, że był przystojny, czuł się rześki, młody,
A w spadku po rodzicach wziął czerstwość i zdrowie.
Nazywał się Soplica: wszyscy Soplicowie
Są, jak wiadomo, krzepcy, otyli i silni,
Do żołnierki jedyni, w naukach mniej pilni.

    Tadeusz się od przodków swoich nie odrodził:
Dobrze na koniu jeździł, pieszo dzielnie chodził,
Tępy nie był, lecz mało w naukach postąpił,
Choć stryj na wychowanie niczego nie skąpił;
On wolał z flinty strzelać albo szablą robić.
Wiedział, że go myślano do wojska sposobić,
Że ojciec w testamencie wyrzekł taką wolę;
Ustawicznie do bębna tęsknił, siedząc w szkole.
Ale stryj nagle pierwsze zamiary odmienił,
Kazał, aby przyjechał i aby się żenił
I objął gospodarstwo; przyrzekł na początek
Dać małą wieś, a potem cały swój majątek.

    Te wszystkie Tadeusza cnoty i zalety
Ściągnęły wzrok sąsiadki, uważnej kobiety.
Zmierzyła jego postać kształtną i wysoką,
Jego ramiona silne, jego pierś szeroką,
I w twarz spojrzała, z której wytryskał rumieniec,
Ilekroć z jej oczyma spotkał się młodzieniec:
Bo z pierwszej lękliwości całkiem już ochłonął,
I patrzył wzrokiem śmiałym, w którym ogień płonął.
Również patrzyła ona: i cztery źrenice
Gorzały przeciw sobie jak roratne świéce.

    Pierwsza z nim po francusku zaczęła rozmowę.
Wracał z miasta, ze szkoły: więc o książki nowe,
O autorów pytała Tadeusza zdania
I ze zdań wyciągała na nowo pytania.
Cóż, gdy potem zaczęła mówić o malarstwie,
O muzyce, o tańcach, nawet o rzeźbiarstwie,
Dowiodła, że zna równie pędzel, nuty, druki;
Aż osłupiał Tadeusz na tyle nauki!
Lękał się, by nie został pośmiewiska celem,
I jąkał się jak żaczek przed nauczycielem.
Szczęściem, że nauczyciel ładny i niesrogi;
Odgadnęła sąsiadka powód jego trwogi,
Wszczęła rzecz o mniej trudnych i mądrych przedmiotach,
O wiejskiego pożycia nudach i kłopotach,
I jak bawić się trzeba, i jak czas podzielić,
By życie uprzyjemnić i wieś rozweselić.
Tadeusz odpowiadał śmielej, szła rzecz daléj,
W pół godziny już byli z sobą poufali;
Zaczęli nawet małe żarciki i sprzeczki.
W końcu, stawiła przed nim trzy z chleba gałeczki.
Trzy osoby na wybór; wziął najbliższą sobie;
Podkomorzanki na to zmarszczyły się obie,
Sąsiadka zaśmiała się, lecz nie powiedziała
Kogo owa szczęśliwsza gałka oznaczała.

    Inaczej bawiono się w drugim końcu stoła;
Bo tam, wzmogłszy się nagle, stronnicy Sokoła
Na partyję Kusego bez litości wsiedli.
Spór był wielki, już potraw ostatnich nie jedli;
Stojąc i pijąc obie kłóciły się strony,
A najstraszniej pan Rejent był zacietrzewiony:
Jak raz zaczął, bez przerwy rzecz swoją tokował,
I gestami ją bardzo dobitnie malował.
(Był dawniej adwokatem pan Rejent Bolesta,
Zwano go kaznodzieją, że zbyt lubił gesta).
Teraz ręce przy boku miał, w tył wygiął łokcie,
Spod ramion wytknął palce i długie paznokcie,
Przedstawiając dwa smycze chartów tym obrazem:
Właśnie rzecz kończył. «Wyczha! puściliśmy razem
Ja i Asesor, razem, jakoby dwa kurki
Jednym palcem spuszczone u jednej dwururki;
Wyczha! poszli, a zając jak struna, smyk w pole,
Psy tuż (to mówiąc, ręce ciągnął wzdłuż po stole
I palcami ruch chartów przedziwnie udawał)
Psy tuż, i hec od lasu odsadzili kawał;
Sokół smyk naprzód; rączy pies, lecz zagorzalec,
Wysadził się przed Kusym, o tyle, o palec:
Wiedziałem, że spudłuje. Szarak, gracz nie lada,
Czchał niby prosto w pole, za nim psów gromada;
Gracz szarak! Skoro poczuł wszystkie charty w kupie
Pstręk na prawo, koziołka, z nim w prawo psy głupie,
A on znowu fajt w lewo, jak wytnie dwa susy,
Psy za nim fajt na lewo: on w las, a mój Kusy
Cap!» Tak krzycząc, pan Rejent na stół pochylony,
Z palcami swymi zabiegł aż do drugiej strony,
I «cap!» Tadeuszowi wrzasnął tuż nad uchem:
Tadeusz i sąsiadka, tym głosu wybuchem
Znienacka przestraszeni właśnie w pół rozmowy,
Odstrychnęli od siebie mimowolnie głowy,
Jako wierzchołki drzewa powiązane społem
Gdy je wicher rozerwie; i ręce pod stołem
Blisko siebie leżące wstecz nagle uciekły,
I dwie twarze w jeden się rumieniec oblekły.

    Tadeusz, by nie zdradzić swego roztargnienia:
«Prawda — rzekł — mój Rejencie, prawda bez wątpienia,
Kusy piękny chart z kształtu, jeśli równie chwytny…»
«Chwytny? — krzyknął pan Rejent — mój pies faworytny
Żeby nie miał być chwytny?…» Więc Tadeusz znowu
Cieszył się, że tak piękny pies nie ma narowu,
Żałował, że go tylko widział idąc z lasu,
I że przymiotów jego poznać nie miał czasu.

    Na to zadrżał Asesor, puścił z rąk kieliszek,
Utopił w Tadeusza wzrok jak bazyliszek.
Asesor mniej krzykliwy i mniej był ruchawy
Od Rejenta, szczuplejszy i mały z postawy,
Lecz straszny na reducie, balu i sejmiku,
Bo powiadano o nim: ma żądło w języku;
Tak dowcipne żarciki umiał komponować,
Iżby je w kalendarzu można wydrukować,
Wszystkie złośliwe, ostre. Dawniej człek dostatni,
Schedę ojca swojego i majątek bratni
Wszystko strwonił na wielkim figurując świecie;
Teraz wszedł w służbę rządu, by znaczyć w powiecie.
Lubił bardzo myślistwo, już to dla zabawy,
Już to że odgłos trąbki i widok obławy
Przypominał mu jego lata młodociane,
Kiedy miał strzelców licznych i psy zawołane:
Teraz mu z całej psiarni dwa charty zostały,
I jeszcze z tych jednemu chciano przeczyć chwały!
Więc zbliżył się i z wolna gładząc faworyty
Rzekł z uśmiechem, a był to uśmiech jadowity:
«Chart bez ogona jest jak szlachcic bez urzędu,
Ogon też znacznie chartom pomaga do pędu:
A pan kusość uważasz za dowód dobroci?
Zresztą zdać się możemy na sąd pańskiej cioci.
Choć pani Telimena mieszkała w stolicy
I bawi się niedawno w naszej okolicy,
Lepiej zna się na łowach niż myśliwi młodzi:
Tak to nauka sama z latami przychodzi».

    Tadeusz, na którego niespodzianie spadał
Grom taki, wstał zmieszany, chwilę nic nie gadał,
Lecz patrzał na rywala coraz straszniej, srożej…
Wtem, wielkim szczęściem, dwakroć kichnął Podkomorzy
«Wiwat!» krzyknęli wszyscy; on się wszystkim skłonił
I z wolna w tabakierę palcami zadzwonił.
Tabakiera ze złota, z brylantów oprawa,
A w środku jej był portret króla Stanisława.
Ojcu Podkomorzego sam król ją darował,
Po ojcu Podkomorzy godnie ją piastował;
Gdy w nią dzwonił, znak dawał, że miał głos zabierać.
Umilkli wszyscy i ust nie śmieli otwierać.
On rzekł: «Wielmożni szlachta bracia dobrodzieje,
Forum myśliwskim tylko są łąki i knieje;
Więc ja w domu podobnych spraw nie decyduję,
I posiedzenie nasze na jutro solwuję,
I dalszych replik stronom dzisiaj nie dozwolę.
Woźny! odwołaj sprawę, na jutro na pole.
Jutro i Hrabia z całym myślistwem tu zjedzie,
I waszeć z nami ruszysz, Sędzio mój sąsiedzie,
I pani Telimena, i panny, i panie,
Słowem, zrobim na urząd wielkie polowanie;
I Wojski towarzystwa nam też nie odmówi».
To mówiąc, tabakierę podawał starcowi.

    Wojski na ostrym końcu śród myśliwych siedział,
Słuchał zmrużywszy oczy, słowa nie powiedział,
Choć młodzież nieraz jego zasięgała zdania,
Bo nikt lepiej nad niego nie znał polowania.
On milczał, szczyptę wziętą z tabakiery ważył
W palcach i długo dumał, nim ją w końcu zażył;
Kichnął, aż cała izba rozległa się echem,
I potrząsając głową, rzekł z gorzkim uśmiechem:
«O, jak mnie to starego i smuci, i dziwi!
Cóż by to o tym starzy mówili myśliwi,
Widząc że w tylu szlachty, w tylu panów gronie,
Mają sądzić się spory o charcim ogonie?
Cóż by rzekł na to stary Rejtan, gdyby ożył?
Wróciłby do Lachowicz i w grób się położył!
Co by rzekł wojewoda Niesiołowski stary,
Który ma dotąd pierwsze na świecie ogary,
I dwiestu strzelców trzyma obyczajem pańskim,
I ma sto wozów sieci w zamku Worończańskim,
A od tylu lat siedzi jak mnich na swym dworze,
Nikt go na polowanie uprosić nie może,
Białopiotrowiczowi samemu odmówił!
Bo cóż by on na waszych polowaniach łowił?
Piękna byłaby sława, ażeby pan taki
Wedle dzisiejszej mody jeździł na szaraki!
Za moich, panie, czasów, w języku strzeleckim,
Dzik, niedźwiedź, łoś, wilk, zwany był zwierzem szlacheckim
A zwierzę niemające kłów, rogów, pazurów,
Zostawiano dla płatnych sług i dworskich ciurów;
Żaden pan nigdy przyjąć nie chciałby do ręki
Strzelby, którą zhańbiono sypiąc w nią śrut cienki!
Trzymano wprawdzie chartów: bo z łowów wracając,
Trafia się, że spod konia mknie się biedak zając:
Puszczano wtenczas za nim dla zabawki smycze
I na konikach małe goniły panicze
Przed oczyma rodziców, którzy te pogonie
Ledwie raczyli widzieć, cóż kłócić się o nie!
Więc niech jaśnie wielmożny Podkomorzy raczy
Odwołać swe rozkazy i niech mi wybaczy,
Że nie mogę na takie jechać polowanie,
I nigdy na nim noga moja nie postanie!
Nazywam się Hreczecha, a od króla Lecha,
Żaden za zającami nie jeździł Hreczecha».

    Tu śmiech młodzieży mowę Wojskiego zagłuszył.
Wstano od stołu, pierwszy Podkomorzy ruszył,
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się damom, starcom i młodzieży;
Za nim szedł kwestarz, Sędzia tuż przy bernardynie.
Sędzia u progu rękę dał Podkomorzynie,
Tadeusz Telimenie, Asesor Krajczance,
A pan Rejent na końcu Wojskiej Hreczeszance.

    Tadeusz z kilku gośćmi poszedł do stodoły,
A czuł się pomieszany, zły i niewesoły.
Rozbierał myślą wszystkie dzisiejsze wypadki:
Spotkanie się, wieczerzę przy boku sąsiadki;
A szczególniej mu słowo «ciocia» koło ucha
Brzęczało ciągle jako naprzykrzona mucha.
Pragnąłby u Woźnego lepiej się wypytać
O pani Telimenie, lecz go nie mógł schwytać;
Wojskiego też nie widział, bo zaraz z wieczerzy
Wszyscy poszli za gośćmi, jak sługom należy,
Urządzając we dworze izby do spoczynku.
Starsi i damy spały we dworskim budynku;
Młodzież Tadeuszowi prowadzić kazano,
W zastępstwie gospodarza, w stodołę na siano.

    W pół godziny tak było głucho w całym dworze
jako po zadzwonieniu na pacierz w klasztorze;
Ciszę przerywał tylko głos nocnego stróża.
Usnęli wszyscy. Sędzia sam oczu nie zmruża;
Jako wódz gospodarstwa obmyśla wyprawę
W pole i w domu przyszłą urządza zabawę.
Dał rozkaz ekonomom, wójtom i gumiennym,
Pisarzom, ochmistrzyni, strzelcom i stajennym
I musiał wszystkie dzienne rachunki przezierać.
Nareszcie rzekł Woźnemu, że się chce rozbierać.
Woźny pas mu odwiązał, pas słucki, pas lity,
Przy którym świecą gęste kutasy jak kity,
Z jednej strony złotogłów w purpurowe kwiaty,
Na wywrót jedwab czarny posrebrzany w kraty;
Pas taki można równie kłaść na strony obie,
Złotą na dzień galowy, a czarną w żałobie.
Sam Woźny umiał pas ten odwiązywać, składać;
Właśnie tym się zatrudniał i kończył tak gadać:

    «Cóż złego, że przeniosłem stoły do zamczyska?
Nikt na tym nic nie stracił, a pan może zyska.
Bo przecież o ten zamek dziś toczy się sprawa.
My od dzisiaj do zamku nabyliśmy prawa
I mimo całą strony przeciwnej zajadłość
Dowiodę, że zamczysko wzięliśmy w posiadłość.
Wszakże kto gości prosi w zamek na wieczerzę,
Dowodzi, że posiadłość tam ma albo bierze;
Nawet strony przeciwne weźmiemy na świadki:
Pamiętam za mych czasów podobne wypadki».

    Już Sędzia spał. Więc Woźny cicho wszedł do sieni,
Siadł przy świecy i dobył książeczkę z kieszeni,
Która mu jak Ołtarzyk Złoty zawsze służy,
Której nigdy nie rzuca w domu i w podróży.
Była to trybunalska wokanda: tam rzędem
Stały spisane sprawy, które przed urzędem
Woźny sam głosem swoim przed laty wywołał,
Albo o których później dowiedzieć się zdołał.
Prostym ludziom wokanda zda się imion spisem;
Woźnemu jest obrazów wspaniałych zarysem.
Czytał więc i rozmyślał: Ogiński z Wizgirdem,
Dominikanie z Rymszą, Rymsza z Wysogirdem,
Radziwił z Wereszczaką, Giedroić z Rdułtowskim,
Obuchowicz z kahałem, Juraha z Piotrowskim,
Maleski z Mickiewiczem, a na koniec Hrabia
Z Soplicą; i czytając, z tych imion wywabia
Pamięć spraw wielkich, wszystkie procesu wypadki,
I stają mu przed oczy sąd, strony i świadki;
I ogląda sam siebie, jak w żupanie białym,
W granatowym kontuszu stał przed trybunałem,
Jedna ręka na szabli, a druga do stoła,
Przywoławszy dwie strony, «Uciszcie się!» woła.
Marząc i kończąc pacierz wieczorny, pomału
Usnął ostatni w Litwie woźny trybunału.

    Takie były zabawy, spory w one lata
Śród cichej wsi litewskiej, kiedy reszta świata
We łzach i krwi tonęła; gdy ów mąż, bóg wojny,
Otoczon chmurą pułków, tysiącem dział zbrojny,
Wprzągłszy w swój rydwan orły złote obok srebrnych,
Od puszcz Libijskich łatał do Alpów podniebnych,
Ciskając grom po gromie, w Piramidy, w Tabor,
W Marengo, w Ulm, w Austerlitz. Zwycięstwo i Zabor
Biegły przed nim i za nim. Sława czynów tylu,
Brzemienna imionami rycerzy, od Nilu
Szła hucząc ku północy, aż u Niemna brzegów
Odbiła się, jak od skał, od Moskwy szeregów,
Które broniły Litwę murami żelaza
Przed wieścią dla Rosyi straszną jak zaraza.

    Przecież nieraz nowina niby kamień z nieba
Spadała w Litwę. Nieraz dziad żebrzący chleba,
Bez ręki lub bez nogi, przyjąwszy jałmużnę,
Stanął i oczy wkoło obracał ostróżne.
Gdy nie widział we dworze rosyjskich żołnierzy
Ani jarmułek, ani czerwonych kołnierzy,
Wtenczas kim był, wyznawał: był legijonistą,
Przynosi kości stare na ziemię ojczystą,
Której już bronić nie mógł… Jak go wtenczas cała
Rodzina pańska, jak go czeladka ściskała,
Zanosząc się od płaczu! On za stołem siadał
I dziwniejsze od baśni historyje gadał.
On opowiadał, jako jenerał Dąbrowski,
Z ziemi włoskiej stara się przyciągnąć do Polski,
Jak on rodaków zbiera na lombardzkim polu;
Jak Kniaziewicz rozkazy daje z Kapitolu
I zwycięzca, wydartych potomkom cezarów
Rzucił w oczy Francuzów sto krwawych sztandarów,
Jak Jabłonowski zabiegł, aż kędy pieprz rośnie,
Gdzie się cukier wytapia i gdzie w wiecznej wiośnie
Pachnące kwitną lasy; z legiją Dunaju
Tam wódz Murzyny gromi, a wzdycha do kraju.

    Mowy starca krążyły we wsi po kryjomu;
Chłopiec, co je posłyszał, znikał nagle z domu,
Lasami i bagnami skradał się tajemnie,
Ścigany od Moskali, skakał kryć się w Niemnie
I nurkiem płynął na brzeg Księstwa Warszawskiego,
Gdzie usłyszał głos miły: «Witaj nam kolego!»
Lecz nim odszedł, wyskoczył na wzgórek z kamienia
I Moskalom przez Niemen rzekł: «Do zobaczenia!»
Tak przekradł się Gorecki, Pac i Obuchowicz,
Piotrowski, Obolewski, Rożycki, Janowicz,
Mierzejewscy, Brochocki i Bernatowicze,
Kupść, Gedymin i inni, których nie policzę:
Opuszczali rodziców i ziemię kochaną,
I dobra, które na skarb carski zabierano.

    Czasem do Litwy kwestarz z obcego klasztoru
Przyszedł, i kiedy bliżej poznał panów dworu,
Gazetę im pokazał, wyprutą z szkaplerza.
Tam stała wypisana i liczba żołnierza,
I nazwisko każdego wodza legijonu,
I każdego z nich opis zwycięstwa lub zgonu.
Po wielu latach pierwszy raz miała rodzina
Wieść o życiu, o chwale i o śmierci syna;
Brał dom żałobę, ale powiedzieć nie śmiano
Po kim była żałoba, tylko zgadywano
W okolicy; i tylko cichy smutek panów,
Lub cicha radość, była gazetą ziemianów.

    Takim kwestarzem tajnym był Robak podobno:
Często on z panem Sędzią rozmawiał osobno;
Po tych rozmowach zawsze jakowaś nowina
Rozeszła się w sąsiedztwie. Postać bernardyna
Wydawała, że mnich ten nie zawsze w kapturze
Chodził i nie w klasztornym zestarzał się murze.
Miał on nad prawym uchem, nieco wyżej skroni,
Bliznę, wyciętej skóry na szerokość dłoni,
I w brodzie ślad niedawny lancy lub postrzału;
Ran tych nie dostał pewnie przy czytaniu mszału.
Ale nie tylko groźne wejrzenie i blizny,
Lecz sam ruch i głos jego miał coś żołnierszczyzny.

    Przy mszy, gdy z wzniesionymi zwracał się rękami
Od ołtarza do ludu, by mówić: «Pan z wami»,
To nieraz tak się zręcznie skręcił jednym razem,
Jakby prawo w tył robił za wodza rozkazem,
I słowa liturgii takim wyrzekł tonem
Do ludu, jak oficer stojąc przed szwadronem:
Postrzegali to chłopcy służący mu do mszy.
Spraw także politycznych był Robak świadomszy,
Niźli żywotów świętych; a jeżdżąc po kweście,
Często zastanawiał się w powiatowym mieście.
Miał pełno interesów: to listy odbierał,
Których nigdy przy obcych ludziach nie otwierał,
To wysyłał posłańców, ale gdzie i po co
Nie powiadał; częstokroć wymykał się nocą
Do dworów pańskich, z szlachtą ustawicznie szeptał,
I okoliczne wioski dokoła wydeptał,
I w karczmach z wieśniakami rozprawiał niemało,
A zawsze o tym, co się w cudzych krajach działo.
Teraz Sędziego, który już spał od godziny,
Przychodzi budzić; pewnie ma jakieś nowiny.




Księga druga



Zamek

Polowanie z chartami na upatrzonego — Gość w zamku — Ostatni z dworzan opowiada historię ostatniego z Horeszków — Rzut oka w sad — Dziewczyna w ogórkach — Śniadanie — Pani Telimeny anegdota petersburska — Nowy wybuch sporów o Kusego i Sokoła — Interwencja Robaka — Rzecz Wojskiego — Zakład — Dalej w grzyby!

Kto z nas tych lat nie pomni, gdy, młode pacholę,
Ze strzelbą na ramieniu świszcząc szedł na pole,
Gdzie żaden wał, płot żaden nogi nie utrudza,
Gdzie, przestępując miedzę, nie poznasz, że cudza!
Bo na Litwie myśliwiec jak okręt na morzu,
Gdzie chcesz, jaką chcesz drogą, buja po przestworzu:
Czyli jak prorok patrzy w niebo, gdzie w obłoku
Wiele jest znaków widnych strzeleckiemu oku;
Czy jak czarownik gada z ziemią, która, głucha
Dla mieszczan, mnóstwem głosów szepce mu do ucha.

Tam derkacz wrzasnął z łąki, szukać go daremnie,
Bo on szybuje w trawie jako szczupak w Niemnie;
Tam ozwał się nad głową ranny wiosny dzwonek,
Również głęboko w niebie schowany skowronek;
Ówdzie orzeł szerokim skrzydłem przez obszary
Zaszumiał, strasząc wróble, jak kometa cary;
Zaś jastrząb, pod jasnymi wiszący błękity,
Trzepie skrzydłem jak motyl na szpilce przybity,
Aż ujrzawszy wśród łąki ptaka lub zająca,
Runie nań z góry jako gwiazda spadająca.

    Kiedyż nam Pan Bóg wrócić z wędrówki dozwoli,
I znowu dom zamieszkać na ojczystej roli,
I służyć w jeździe, która wojuje szaraki,
Albo w piechocie, która nosi broń na ptaki,
Nie znać innych prócz kosy i sierpa rynsztunków,
I innych gazet, oprócz domowych rachunków!

    Nad Soplicowem słońce weszło i już padło
Na strzechy i przez szpary w stodołę się wkradło;
I po ciemnozielonym, świeżym, wonnym sianie,
Z którego młodzież sobie zrobiła posłanie,
Rozpływały się złote, migające pręgi
Z otworu czarnej strzechy jak z warkocza wstęgi;
I słońce usta sennych promykiem poranka
Drażni jak dziewczę kłosem budzące kochanka.
Już wróble skacząc, świerkać zaczęły pod strzechą;
Już trzykroć gęgnął gąsior, a za nim jak echo
Odezwały się chórem kaczki i indyki
I słychać bydła w pole idącego ryki.

    Wstała młodzież. Tadeusz jeszcze senny leży;
Bo też najpóźniej zasnął. Z wczorajszej wieczerzy
Wrócił tak niespokojny, że o kurów pianiu
Jeszcze oczu nie zmrużył, a na swym posłaniu
Tak kręcił się, że w siano jak w wodę utonął,
I spał twardo, aż zimny wiatr w oczy mu wionął,
Gdy skrzypiące stodoły drzwi otwarto z trzaskiem,
I bernardyn, ksiądz Robak, wszedł z węzlastym paskiem,
«Surge puer!» wołając i ponad barkami
Rubasznie wywijając pasek z ogórkami.

    Już na dziedzińcu słychać myśliwskie okrzyki;
Wyprowadzają konie, zajeżdżają bryki,
Ledwie dziedziniec taką gromadę ogarnie,
Odezwały się trąby, otworzono psiarnie;
Zgraja chartów, wypadłszy, wesoło skowycze;
Widząc rumaki szczwaczów, dojeżdżaczów smycze,
Psy jak szalone cwałem śmigają po dworze,
Potem biegną i kładą szyje na obroże:
Wszystko to bardzo dobre polowanie wróży;
Nareszcie Podkomorzy dał rozkaz podróży.

    Ruszyli szczwacze z wolna, jeden tuż za drugim;
Ale za bramą rzędem rozbiegli się długim.
W środku jechali obok Asesor z Rejentem;
A choć na siebie czasem patrzyli ze wstrętem,
Rozmawiali przyjaźnie, jak ludzie honoru
Idąc na rozstrzygnienie śmiertelnego sporu:
Nikt ze słów zawziętości ich poznać nie zdoła;
Pan Rejent wiódł Kusego, Asesor Sokoła.
Z tyłu damy w pojazdach; młodzieńcy, stronami
Cwałując tuż przy kołach, gadali z damami.

    Ksiądz Robak po dziedzińcu wolnym chodził krokiem
Kończąc ranne pacierze; ale rzucał okiem
Na pana Tadeusza, marszczył się, uśmiechał,
Wreszcie kiwnął nań palcem, Tadeusz podjechał;
Robak palcem po nosie dawał mu znak groźby:
Lecz mimo Tadeusza pytania i prośby,
Ażeby mu wyraźnie, co chce, wytłumaczył,
Bernardyn odpowiedzieć ni spojrzeć nie raczył;
Kaptur tylko nasunął i pacierz swój kończył,
Więc Tadeusz odjechał i z gośćmi się złączył.

    Właśnie wtenczas myśliwi smycze zatrzymali,
I wszyscy nieruchomi w miejscach swoich stali;
Jeden drugiemu ręką dawał znak milczenia,
A wszyscy obrócili oczy do kamienia,
Nad którym stał pan Sędzia. On zwierza obaczył
I rąk skinieniem swoje rozkazy tłumaczył.
Pojęli wszyscy: stoją, a środkiem po roli
Asesor i pan Rejent kłusują powoli.
Tadeusz, będąc bliższy, obydwu wyprzedził,
Stanął obok Sędziego i oczyma śledził.
Dawno już nie był w polu; na szarej przestrzeni
Trudno dojrzeć szaraka, zwłaszcza śród kamieni.
Pokazał mu pan Sędzia; siedział biedny zając,
Płaszcząc się pod kamieniem, uszy nadstawiając,
Okiem czerwonym spotkał myśliwców wejrzenie
I jakby urzeczony, czując przeznaczenie,
Ze strachu od ich oczu nie mógł zwrócić oka,
I pod opoką siedział martwy jak opoka.
Tymczasem kurz na roli rośnie coraz bliżéj;
Pędzi na smyczy Kusy, za nim Sokół chyży,
Tuż Asesor z Rejentem razem wrzaśli z tyłu:
«Wyczha, wyczha!» i z psami znikli w kłębach pyłu.

    Kiedy tak za szarakiem goniono, tymczasem
Ukazał się pan Hrabia pod zamkowym lasem.
Wiedziano w okolicy, że ten pan nie może
Nigdy nigdzie stawić się w naznaczonej porze.
I dziś zaspał poranek; więc na sługi zrzędził,
Widząc myśliwców w polu cwałem do nich pędził.
Surdut swój angielskiego kroju, biały, długi,
Połami na wiatr puścił; z tyłu konno sługi,
W kapeluszach jak grzybki, czarnych, lśniących, małych,
W kurtkach, w butach stryflastych, w pantalonach białych:
Sługi, które pan Hrabia tym kształtem odzieje,
Nazywają się w jego pałacu dżokeje.

    Cwałująca czereda zleciała na błonia,
Gdy Hrabia ujrzał zamek i zatrzymał konia.
Pierwszy raz widział zamek z rana i nie wierzył,
Że to były też same mury; tak odświeżył
I upięknił poranek zarysy budowy:
Zadziwił się pan Hrabia na widok tak nowy.
Wieża zdała się dwakroć wyższa, bo stercząca
Nad mgłą ranną; dach z blachy złocił się od słońca,
Pod nim błyszczała w kratach reszta szyb wybitych,
Łamiąc promienie wschodu w tęczach rozmaitych;
Niższe piętra oblała tumanu powłoka,
Rozpadliny i szczerby zakryła od oka;
Krzyk dalekich myśliwców wiatrami przygnany,
Odbijał się kilkakroć o zamkowe ściany:
Przysiągłbyś, że krzyk z zamku, że pod mgły zasłoną
Mury odbudowano i znów zaludniono.

    Hrabia lubił widoki niezwykłe i nowe,
Zwał je romansowymi; mawiał, że ma głowę
Romansową: w istocie był wielkim dziwakiem.
Nieraz, pędząc za lisem albo za szarakiem,
Nagle stawał i w niebo poglądał żałośnie,
Jak kot, gdy ujrzy wróble na wysokiej sośnie;
Często bez psa, bez strzelby, błąkał się po gaju
Jak rekrut zbiegły; często siadał przy ruczaju
Nieruchomy, schyliwszy głowę nad potokiem,
Jak czapla wszystkie ryby chcąca pozrzeć okiem:
Takie były Hrabiego dziwne obyczaje.
Wszyscy mówili, że mu czegoś nie dostaje;
Szanowano go przecież, bo pan z prapradziadów,
Bogacz, dobry dla chłopów, ludzki dla sąsiadów,
Nawet dla Żydów.

                        Hrabski koń, zwrócony z drogi,
Prosto kłusował polem aż pod zamku progi.
Hrabia samotny wzdychał, poglądał na mury,
Wyjął papier, ołówek i kreślił figury.
Wtem, spojrzawszy w bok — ujrzał o dwadzieścia kroków
Człowieka, który, równie miłośnik widoków,
Z głową zadartą, ręce włożywszy w kieszenie,
Zdawało się, że liczył oczyma kamienie.
Poznał go zaraz, ale musiał kilka razy
Krzyknąć, nim głos Hrabiego usłyszał Gerwazy.
Szlachcic to był, służący dawnych zamku panów,
Pozostały ostatni z Horeszki dworzanów;
Starzec wysoki, siwy, twarz miał czerstwą, zdrową,
Zmarszczkami pooraną, posępną, surową.
Dawniej pomiędzy szlachtą z wesołości słynął;
Ale od bitwy, w której dziedzic zamku zginął,
Gerwazy się odmienił i już od lat wielu
Ani był na kiermaszu, ani na weselu;
Odtąd jego dowcipnych żartów nie słyszano,
I uśmiechu na jego twarzy nie widziano.
Zawsze nosił Horeszków liberyją dawną;
Kurtę z połami żółtą, galonem oprawną,
Który dziś żółty, dawniej zapewne był złoty,
Wkoło szyte jedwabiem herbowe klejnoty,
Półkozice: i stąd też cała okolica
Półkozicem przezwała starego szlachcica.
Czasem też od przysłowia, które bez ustanku
Powtarzał, nazywano go także Mopanku;
Czasem Szczerbcem, że całą łysinę miał w szczerbach;
Lecz on zwał się Rębajło, a o jego herbach
Nie wiadomo. Klucznikiem siebie tytułował,
Iż ten urząd na zamku przed laty piastował.
I dotąd nosił wielki pęk kluczy za pasem,
Uwiązany na taśmie ze srebrnym kutasem,
Choć nie miał co otwierać, bo zamku podwoje
Stały otworem. Przecież, wynalazł drzwi dwoje;
Sam je własnym nakładem naprawił i wstawił,
I drzwi tych odmykaniem codziennie się bawił.
W jednej z izb pustych, obrał mieszkanie dla siebie;
Mogąc żyć u Hrabiego na łaskawym chlebie,
Nie chciał, bo wszędzie tęsknił i czuł się niezdrowym,
Jeżeli nie oddychał powietrzem zamkowym.

    Skoro ujrzał Hrabiego, czapkę z głowy schwycił,
I krewnego swych panów ukłonem zaszczycił,
Chyląc łysinę wielką, świecącą z daleka,
I naciętą od licznych kordów jak nasieka;
Gładził ją ręką, podszedł, i jeszcze raz nisko
Skłoniwszy się, rzekł smutnie: «Mopanku, panisko,
Daruj mnie, że tak mówię, jaśnie grafie panie,
To jest mój zwyczaj, nie zaś nieuszanowanie:
»mopanku« powiadali wszyscy Horeszkowie,
Ostatni Stolnik, pan mój, miał takie przysłowie…
Czyż to prawda, mopanku, że pan grosza skąpisz
Na proces i ten zamek Soplicom ustąpisz?
Nie wierzyłem, lecz w całym powiecie tak słychać».
Tu, poglądając w zamek, nie przestawał wzdychać.

    «Cóż dziwnego — rzekł Hrabia — koszt wielki, a nuda
Jeszcze większa; chcę skończyć, lecz szlachcic maruda
Upiera się; przewidział, że mię znudzić może:
Dłużej też nie wytrzymam i dzisiaj broń złożę,
Przyjmę warunki zgody, jakie mi sąd poda…»
«Zgody? — krzyknął Gerwazy — z Soplicami zgoda?
Z Soplicami, mopanku?» — To mówiąc wykrzywił
Usta, jakby nad własną mową się zadziwił.
«Zgoda i Soplicowie! Mopanku, panisko,
Pan żartuje, co? Zamek, Horeszków siedlisko,
Ma pójść w ręce Sopliców? Niech pan tylko raczy
Zsiąść z konia. Pójdźmy w zamek. Niech no pan obaczy.
Pan sam nie wie, co robi. Niech się pan nie wzbrania,
Zsiadaj pan» — i przytrzymał strzemię do zsiadania.

    Weszli w zamek; Gerwazy stanął w progu sieni:
«Tu — rzekł — dawni panowie dworem otoczeni,
Często siadali w krzesłach w poobiedniej porze.
Pan godził spory włościan lub w dobrym humorze
Gościom różne ciekawe historyje prawił,
Albo ich powieściami i żarty się bawił,
A młodzież na dziedzińcu biła się w palcaty,
Lub ujeżdżała pańskie tureckie bachmaty».

    Weszli w sień. Rzekł Gerwazy: «W tej ogromnej sieni
Brukowanej nie znajdziesz pan tyle kamieni,
Ile tu pękło beczek wina w dobrych czasach;
Szlachta ciągnęła kufy z piwnicy na pasach,
Sproszona na sejm albo sejmik powiatowy,
Albo na imieniny pańskie, lub na łowy.
Podczas uczty na chorze tym kapela stała,
I w organ, i w rozliczne instrumenty grała;
A gdy wnoszono zdrowie, trąby jak w dniu sądnym
Grzmiały z choru; wiwaty szły ciągiem porządnym:
Pierwszy wiwat za zdrowie Króla Jegomości,
Potem prymasa, potem Królowej Jejmości,
Potem szlachty i całej Rzeczypospolitej,
A na koniec po piątej szklanicy wypitej,
Wnoszono: »Kochajmy się«. Wiwat bez przestanku,
Który dniem okrzykniony, brzmiał aż do poranku;
A już gotowe stały cugi i podwody,
Aby każdego odwieźć do jego gospody».

    Przeszli już kilka komnat. Gerwazy w milczeniu,
Tu wzrok na ścianie wstrzymał, ówdzie na sklepieniu,
Przywołując pamiątkę tu smutną, tam miłą;
Czasem, jakby chciał mówić: «Wszystko się skończyło»,
Kiwnął żałośnie głową; czasem machnął ręką:
Widać, że mu wspomnienie samo było męką,
I że je chciał odpędzić. Aż się zatrzymali
Na górze, w wielkiej, niegdyś zwierciadlanej sali.
Dziś wydartych zwierciadeł stały puste ramy,
Okna bez szyb, z krużgankiem wprost naprzeciw bramy.
Tu wszedłszy, starzec głowę zadumaną skłonił
I twarz zakrył rękami; a gdy ją odsłonił,
Miała wyraz żałości wielkiej i rozpaczy.
Hrabia, chociaż nie wiedział, co to wszystko znaczy,
Poglądając w twarz starca czuł jakieś wzruszenie,
Rękę mu ścisnął; chwilę trwało to milczenie,
Przerwał je starzec, trzęsąc wzniesioną prawicą:
«Nie masz zgody, mopanku, pomiędzy Soplicą
I krwią Horeszków; w panu krew Horeszków płynie,
Jesteś krewnym Stolnika, po matce łowczynie,
Która się rodzi z drugiej córki kasztelana,
Który był, jak wiadomo, wujem mego pana.
Słuchaj pan historyi swej własnej rodzinnej,
Która się stała właśnie w tej izbie, nie innej.

    Nieboszczyk pan mój, Stolnik, pierwszy pan w powiecie,
Bogacz i familiant, miał jedyne dziecię,
Córkę piękną jak anioł; więc się zalecało
Stolnikównie i szlachty, i paniąt niemało.
Między szlachtą był jeden wielki paliwoda,
Kłótnik, Jacek Soplica, zwany Wojewoda
Przez żart; w istocie wiele znaczył w województwie,
Bo rodzinę Sopliców miał jakby w dowództwie,
I trzystu ich kreskami rządził wedle woli,
Choć sam nic nie posiadał prócz kawałka roli,
Szabli i wielkich wąsów od ucha do ucha.
Owoż pan Stolnik nieraz wzywał tego zucha,
I ugaszczał w pałacu, zwłaszcza w czas sejmików,
Popularny dla jego krewnych i stronników.
Wąsal tak wzbił się w dumę łaskawym przyjęciem,
Że mu się uroiło zostać pańskim zięciem.
Do zamku nieproszony coraz częściej jeździł,
W końcu u nas jak w swoim domu się zagnieździł.
I już miał się oświadczać: lecz pomiarkowano,
I czarną mu polewkę do stołu podano.
Podobno Stolnikównie wpadł Soplica w oko,
Ale przed rodzicami taiła głęboko.

    Było to za Kościuszki czasów; pan popierał
Prawo trzeciego maja i już szlachtę zbierał,
Aby konfederatom ciągnąć ku pomocy,
Gdy nagle Moskwa zamek opasała w nocy.
Ledwie był czas z moździerza na trwogę wypalić,
Podwoje dolne zamknąć i ryglem zawalić.
W zamku całym był tylko: pan Stolnik, ja, pani,
Kuchmistrz i dwóch kuchcików, wszyscy trzej pijani,
Proboszcz, lokaj, hajducy czterej, ludzie śmiali.
Więc za strzelby, do okien. Aż tu tłum Moskali,
Krzycząc: »Ura!«, od bramy wali po tarasie;
My im ze strzelb dziesięciu palnęli »A zasie«.
Nic tam nie było widać; słudzy bez ustanku
Strzelali z dolnych pięter, a ja i pan z ganku.
Wszystko szło pięknym ładem, choć w tak wielkiej trwodze:
Dwadzieścia strzelb leżało tu na tej podłodze;
Wystrzeliliśmy jedną, podawano drugą.
Ksiądz proboszcz zatrudniał się czynnie tą usługą,
I pani, i panienka, i nadworne panny:
Trzech było strzelców, a szedł ogień nieustanny.
Grad kul sypały z dołu moskiewskie piechury;
My z rzadka, ale celniej dogrzewali z góry.
Trzy razy aż pode drzwi to chłopstwo się wparło,
Ale za każdym razem trzech nogi zadarło,
Więc uciekli pod lamus; a już był poranek.
Pan Stolnik wesół wyszedł ze strzelbą na ganek,
I skoro spod lamusa Moskal łeb wychylił,
On dawał zaraz ognia, a nigdy nie mylił;
Za każdym razem czarny kaszkiet w trawę padał
I już się rzadko który zza ściany wykradał.
Stolnik, widząc strwożone swe nieprzyjaciele,
Myślił zrobić wycieczkę, porwał karabelę
I z ganku krzycząc sługom wydawał rozkazy;
Obróciwszy się do mnie, rzekł: »Za mną Gerwazy!«
Wtem strzelono spod bramy… Stolnik się zająknął,
Zaczerwienił się, zbladnął, chciał mówić, krwią chrząknął:
Postrzegłem wtenczas kulę, wpadła w piersi same.
Pan słaniając się, palcem ukazał na bramę:
Poznałem tego łotra Soplicę! poznałem!
Po wzroście i po wąsach! Jego to postrzałem
Zginął Stolnik, widziałem! Łotr jeszcze do góry
Wzniesioną trzymał strzelbę, jeszcze dym szedł z rury!
Wziąłem go na cel; zbójca stał jak skamieniały!
Dwa razy dałem ognia, i oba wystrzały
Chybiły: czym ze złości, czy z żalu źle mierzył…
Usłyszałem wrzask kobiet, spojrzałem — pan nie żył».

    Tu Gerwazy umilknął i łzami się zalał,
Potem rzekł kończąc: «Moskal już wrota wywalał:
Bo po śmierci Stolnika stałem bezprzytomnie,
I nie widziałem, co się działo wokoło mnie.
Szczęściem, na odsiecz przyszedł nam Parafianowicz,
Przywiódłszy Mickiewiczów dwiestu z Horbatowicz,
Którzy są szlachta liczna i dzielna, człek w człeka,
A nienawidzą rodu Sopliców od wieka.

    Tak zginął pan potężny, pobożny i prawy,
Który miał w domu krzesła, wstęgi i buławy,
Ojciec włościan, brat szlachty; i nie miał po sobie
Syna, który by zemstę poprzysiągł na grobie!
Ale miał sługi wierne. Ja w krew jego rany
Obmoczyłem mój rapier Scyzorykiem zwany
(Zapewne pan o moim słyszał Scyzoryku,
Sławnym na każdym sejmie, targu i sejmiku).
Przysiągłem wyszczerbić go na Sopliców karkach,
Ścigałem ich na sejmach, zajazdach, jarmarkach.
Dwóch zarąbałem w kłótni, dwóch na pojedynku;
Jednego podpaliłem w drewnianym budynku,
Kiedyśmy zajeżdżali z Rymszą Korelicze:
Upiekł się tam jak piskorz; a tych nie policzę,
Którym uszy obciąłem. Jeden tylko został,
Który dotąd ode mnie pamiątki nie dostał:
Rodzoniutki braciszek owego wąsala!
Żyje dotąd i z swoich bogactw się przechwala,
Zamku Horeszków tyka swych kopców krawędzią,
Szanowany w powiecie, ma urząd, jest Sędzią!
I pan mu zamek oddasz? Niecne jego nogi
Mają krew pana mego zetrzeć z tej podłogi?
O nie! Póki Gerwazy ma choć za grosz duszy,
I tyle sił, że jednym małym palcem ruszy
Scyzoryk swój wiszący dotychczas na ścianie,
Póty Soplica tego zamku nie dostanie!»

    «O! — krzyknął Hrabia, ręce podnosząc do góry —
Dobre miałem przeczucie, żem lubił te mury!
Choć nie wiedziałem, że w nich taki skarb się mieści,
Tyle scen dramatycznych i tyle powieści!
Skoro zamek mych przodków Soplicom zagrabię,
Ciebie osadzę w murach jak mego burgrabię.
Twoja powieść, Gerwazy, zajęła mię mocno.
Szkoda, żeś mię nie przywiódł tu w godzinę nocną;
Udrapowany płaszczem, siadłbym na ruinach,
A ty byś mi o krwawych rozpowiadał czynach.
Szkoda, że masz niewielki dar opowiadania!
Nieraz takie słyszałem i czytam podania;
W Anglii i w Szkocyi każdy zamek lordów,
W Niemczech każdy dwór grafów był teatrem mordów.
W każdej dawnej, szlachetnej, potężnej rodzinie
Jest wieść o jakimś krwawym lub zdradzieckim czynie,
Po którym zemsta spływa na dziedziców w spadku:
W Polsce pierwszy raz słyszę o takim wypadku.
Czuję, że we mnie mężnych krew Horeszków płynie!
Wiem, co winienem sławie i mojej rodzinie.
Tak, muszę zerwać wszelkie z Soplicą układy,
Choćby do pistoletów przyszło lub do szpady!
Honor każe». Rzekł, ruszył uroczystym krokiem,
A Gerwazy szedł z tyłu w milczeniu głębokiem.
Przed bramą stanął Hrabia, sam do siebie gadał,
Poglądając na zamek prędko na koń wsiadał,
Tak samotną rozmowę kończąc roztargniony:
«Szkoda, że ten Soplica stary nie ma żony
Lub córki pięknej, której ubóstwiałbym wdzięki!
Kochając i nie mogąc otrzymać jej ręki,
Nowa by się w powieści zrobiła zawiłość:
Tu serce, tam powinność — tu zemsta, tam miłość!»

    Tak szepcąc spiął ostrogi; koń leciał do dworu,
Gdy z drugiej strony strzelcy wyjeżdżali z boru.
Hrabia lubił myślistwo, ledwie strzelców zoczył,
Zapomniawszy o wszystkim, prosto ku nim skoczył,
Mijając bramę, ogród, płoty: gdy w zawrocie
Obejrzał się, i konia zatrzymał przy płocie.

Był sad. —

                        Drzewa owocne, zasadzone w rzędy,
Ocieniały szerokie pole; spodem grzędy.
Tu kapusta, sędziwe schylając łysiny,
Siedzi i zda się dumać o losach jarzyny;
Tam, plącząc stronki w marchwi zielonej warkoczu,
Wysmukły bób obraca na nią tysiąc oczu;
Owdzie podnosi złotą kitę kukuruza;
Gdzieniegdzie otyłego widać brzuch harbuza,
Który od swej łodygi aż w daleką stronę,
Wtoczył się jak gość między buraki czerwone.

    Grzędy rozcięte miedzą; na każdym przykopie
Stoją jakby na straży w szeregach konopie,
Cyprysy jarzyn; ciche, proste i zielone,
Ich liście i woń służą grzędom za obronę,
Bo przez ich liście nie śmie przecisnąć się żmija,
A ich woń gąsienice i owad zabija.
Dalej maków białawe górują badyle;
Na nich, myślisz, iż rojem usiadły motyle
Trzepiotąc skrzydełkami, na których się mieni
Z rozmaitością tęczy blask drogich kamieni:
Tylą farb żywych, różnych, mak źrenicę mami.
W środku kwiatów, jak pełnia pomiędzy gwiazdami,
Krągły słonecznik licem wielkim, gorejącem,
Od wschodu do zachodu kręci się za słońcem.

    Pod płotem wąskie, długie, wypukłe pagórki,
Bez drzew, krzewów i kwiatów: ogród na ogórki.
Pięknie wyrosły; liściem wielkim, rozłożystym,
Okryły grzędy jakby kobiercem fałdzistym.
Pośrodku szła dziewczyna w bieliznę ubrana,
W majowej zieloności tonąc po kolana;
Z grzęd zniżając się w bruzdy, zdała się nie stąpać,
Ale pływać po liściach, w ich barwie się kąpać.
Słomianym kapeluszem osłoniła głowę,
Od skroni powiewały dwie wstążki różowe
I kilka puklów światłych, rozwitych warkoczy;
Na ręku miała koszyk, w dół spuściła oczy,
Prawą rękę podniosła niby do chwytania,
Jako dziewczę, gdy rybki w kąpieli ugania
Bawiące się z jej nóżką, tak ona co chwila
Z rękami i koszykiem po owoc się schyla,
Który stopą nadtrąci lub dostrzeże okiem.

    Pan Hrabia zachwycony tak cudnym widokiem
Stał cicho. Słysząc tętent towarzyszów w dali,
Ręką dał znak, ażeby wstrzymać konie; stali.
On patrzył z wyciągniętą szyją, jak dziobaty
Żuraw z dala od stada gdy odprawia czaty,
Stojąc na jednej nodze, z czujnymi oczyma,
I by nie zasnąć, kamień w drugiej nodze trzyma.

    Zbudził Hrabiego szelest na plecach i skroni;
Był to bernardyn, kwestarz Robak, a miał w dłoni
Podniesione do góry węzłowate sznurki:
«Ogórków chcesz Waść — krzyknął — oto masz ogórki!
Wara, panie, od szkody; na tutejszej grzędzie
Nie dla Waszeci owoc, nic z tego nie będzie».
Potem palcem pogroził, kaptura poprawił,
I odszedł. Hrabia jeszcze chwilę w miejscu bawił,
Śmiejąc się i klnąc razem tej nagłej przeszkodzie.
Okiem powrócił w ogród, ale już w ogrodzie
Nie było jej; mignęła tylko śród okienka
Jej różowa wstążeczka i biała sukienka.
Widać na grzędach, jaką przeleciała drogą,
Bo liść zielony, w biegu potrącony nogą,
Podnosił się, drżał chwilę, aż się uspokoił,
Jak woda, którą ptaszek skrzydłami rozkroił.
A na miejscu, gdzie stała, tylko porzucony
Koszyk mały z rokity, denkiem wywrócony,
Pogubiwszy owoce na liściach zawisał,
I wśród fali zielonej jeszcze się kołysał.

    Po chwili wszędzie było samotnie i głucho.
Hrabia oczy w dom utkwił i natężył ucho;
Zawsze dumał, a strzelcy zawsze nieruchomie
Za nim stali. Aż w cichym i samotnym domie
Wszczął się naprzód szmer, potem gwar i krzyk wesoły
Jak w ulu pustym, kiedy weń wlatują pszczoły.
Był to znak, że wracali goście z polowania,
I krzątała się służba około śniadania.

    Jakoż po wszystkich izbach panował ruch wielki:
Roznoszono potrawy, sztućce i butelki.
Mężczyźni tak jak weszli, w swych zielonych strojach,
Z talerzami, z szklankami, chodząc po pokojach,
Jedli, pili lub wsparci na okien uszakach,
Rozprawiali o flintach, chartach i szarakach.
Podkomorstwo i Sędzia przy stole; a w kątku
Panny szeptały z sobą. Nie było porządku,
Jaki się przy obiadach i wieczerzach chowa;
Była to w staropolskim domu moda nowa:
Przy śniadaniach pan Sędzia, choć nierad, pozwalał
Na taki nieporządek, lecz go nie pochwalał.

    Różne też były dla dam i mężczyzn potrawy:
Tu roznoszono tace z całą służbą kawy,
Tace ogromne, w kwiaty ślicznie malowane,
Na nich kurzące wonnie imbryki blaszane
I z porcelany saskiej złote filiżanki;
Przy każdej garnuszeczek mały do śmietanki.
Takiej kawy, jak w Polszcze, nie ma w żadnym kraju:
W Polszcze, w domu porządnym, z dawnego zwyczaju,
Jest do robienia kawy osobna niewiasta,
Nazywa się kawiarka; ta sprowadza z miasta,
Lub z wicin bierze ziarna w najlepszym gatunku
I zna tajne sposoby gotowania trunku,
Który ma czarność węgla, przejrzystość bursztynu,
Zapach moki i gęstość miodowego płynu.
Wiadomo, czym dla kawy jest dobra śmietana;
Na wsi nietrudno o nią: bo kawiarka z rana,
Przystawiwszy imbryki, odwiedza mleczarnie
I sama lekko świeży nabiału kwiat garnie
Do każdej filiżanki w osobny garnuszek,
Aby każdą z nich ubrać w osobny kożuszek.

    Panie starsze, już wcześniej wstawszy, piły kawę;
Teraz drugą dla siebie zrobiły potrawę
Z gorącego, śmietaną bielonego piwa,
W którym twaróg gruzłami posiekany pływa.

    Zaś dla mężczyzn wędliny leżą do wyboru:
Półgęski tłuste, kumpie, skrzydliki ozoru,
Wszystkie wyborne, wszystkie sposobem domowym
Uwędzone w kominie dymem jałowcowym;
W końcu wniesiono zrazy na ostatnie danie:
Takie bywało w domu Sędziego śniadanie.

    We dwóch izbach dwa różne skupiły się grona:
Starszyzna przy stoliku małym zgromadzona
Mówiła o sposobach nowych gospodarskich,
O nowych coraz sroższych ukazach cesarskich;
Podkomorzy krążące o wojnie pogłoski
Oceniał i wyciągał polityczne wnioski.
Panna Wojska, włożywszy okulary sine,
Zabawiała kabałą z kart Podkomorzynę.
W drugiej izbie toczyła młodzież rzecz o łowach
W spokojniejszych i cichszych niż zwykle rozmowach:
Bo Asesor i Rejent, oba mówcy wielcy,
Pierwsi znawcy myślistwa i najlepsi strzelcy,
Siedzieli przeciw sobie mrukliwi i gniewni.
Oba dobrze poszczuli, oba byli pewni
Zwycięstwa swoich chartów: gdy pośród równiny
Znalazł się zagon chłopskiej niezżętej jarzyny.
Tam wpadł zając; już Kusy, już go Sokół imał,
Gdy Sędzia dojeżdżaczy na miedzy zatrzymał.
Musieli być posłuszni, chociaż w wielkim gniewie;
Psy powróciły same i nikt pewnie nie wie,
Czy zwierz uszedł, czy wzięty; nikt zgadnąć nie zdoła,
Czy wpadł w paszczę Kusego, czyli też Sokoła,
Czyli obydwu razem: różnie sądzą strony,
I spór na dalsze czasy trwał nierozstrzygniony.

    Wojski stary od izby do izby przechodził,
Po obu stronach oczy roztargnione wodził,
Nie mieszał się w myśliwych ni w starców rozmowę
I widać, że czym innym zajętą miał głowę.
Nosił skórzaną plackę: czasem w miejscu stanie,
Duma długo i — muchę zabije na ścianie.

    Tadeusz z Telimeną, pomiędzy izbami
Stojąc we drzwiach na progu, rozmawiali sami.
Niewielki oddzielał ich od słuchaczów przedział,
Więc szeptali. Tadeusz teraz się dowiedział:
Że ciocia Telimena jest bogata pani,
Że nie są kanonicznie z sobą powiązani
Zbyt bliskim pokrewieństwem; i nawet niepewno,
Czy ciocia Telimena jest synowca krewną,
Choć ją stryj zowie siostrą, bo wspólni rodzice
Tak ich kiedyś nazwali mimo lat różnicę;
Że potem ona żyjąc w stolicy czas długi
Wyrządziła niezmierne Sędziemu usługi;
Stąd ją Sędzia szanował bardzo i przed światem
Lubił, może z próżności, nazywać się bratem,
Czego mu Telimena przez przyjaźń nie wzbrania.
Ulżyły Tadeusza sercu te wyznania.
Wiele też innych rzeczy sobie oświadczyli;
A wszystko to się stało w jednej krótkiej chwili.

    Ale w izbie na prawo, kusząc Asesora,
Rzekł Rejent mimojazdem: «Ja mówiłem wczora,
Że polowanie nasze udać się nie może:
Jeszcze zbyt wcześnie, jeszcze na pniu stoi zboże
I mnóstwo sznurów chłopskiej niezżętej jarzyny:
Stąd i Hrabia nie przybył mimo zaprosiny.
Hrabia na polowaniu bardzo dobrze zna się,
Nieraz gadał o łowów i miejscu, i czasie;
Hrabia chował się w obcych krajach od dzieciństwa
I powiada, że to jest znakiem barbarzyństwa
Polować, tak jak u nas, bez żadnego względu
Na artykuły ustaw, przepisy urzędu,
Nie szanując niczyich kopców ani miedzy,
Jeździć po cudzym gruncie, bez dziedzica wiedzy,
Wiosną równie jak latem zbiegać pola, knieje,
Zabijać nieraz lisa, właśnie gdy linieje,
Albo cierpieć, iż kotną samicę zajęczą
Charty w runi uszczują, a raczej zamęczą,
Z wielką szkodą zwierzyny. Stąd się Hrabia żali,
Że cywilizacyja większa u Moskali;
Bo tam o polowaniu są ukazy cara
I dozór policyi, i na winnych kara».

    Telimena ku lewej izbie obrócona
Wachlując batystową chusteczką ramiona:
«Jak mamę kocham — rzekła — Hrabia się nie myli.
Znam ja dobrze Rosyją. Państwo nie wierzyli,
Gdy im nieraz mówiłam, jak tam z wielu względów
Godna pochwały czujność i srogość urzędów.
Byłam ja w Petersburku, nie raz, nie dwa razy!
Miłe wspomnienia! wdzięczne przeszłości obrazy!
Co za miasto! Nikt z panów nie był w Petersburku?
Chcecie może plan widzieć? Mam plan miasta w biurku.
Latem świat petersburski zwykł mieszkać na daczy,
To jest w pałacach wiejskich (dacza wioskę znaczy).
Mieszkałam w pałacyku, tuż nad Newą rzeką,
Niezbyt blisko od miasta i niezbyt daleko,
Na niewielkim, umyślnie sypanym pagórku:
Ach, co to był za domek! Plan mam dotąd w biurku.
Otóż, na me nieszczęście, najął dom w sąsiedztwie
Jakiś mały czynownik siedzący na śledztwie;
Trzymał kilkoro chartów: co to za męczarnie,
Gdy blisko mieszka mały czynownik i psiarnie!
Ilekroć z książką wyszłam sobie do ogrodu,
Użyć księżyca blasku, wieczornego chłodu
Zaraz i pies przyleciał, i kręcił ogonem,
I strzygł uszami, właśnie jakby był szalonym.
Nieraz się nalękałam. Serce mi wróżyło
Z tych psów jakieś nieszczęście: tak się też zdarzyło.
Bo gdym szła do ogrodu pewnego poranka,
Chart u nóg mych zadławił mojego kochanka
Bonończyka! Ach, była to rozkoszna psina,
Miałam ją w podarunku od księcia Sukina
Na pamiątkę; rozumna, żywa jak wiewiórka:
Mam jej portrecik, tylko nie chcę iść do biurka.
Widząc ją zadławioną, z wielkiej alteracji
Dostałam mdłości, spazmów, serca palpitacji.
Może by gorzej jeszcze z moim zdrowiem było;
Szczęściem, nadjechał właśnie z wizytą Kiryło
Gawrylicz Kozodusin, wielki łowczy dworu.
Pyta się o przyczynę tak złego humoru,
Każe wnet urzędnika przyciągnąć za uszy;
Staje pobladły, drżący i prawie bez duszy.
»Jak śmiesz — krzyknął Kiryło piorunowym głosem —
Szczuć wiosną łanię kotną tuż pod carskim nosem?«
Osłupiały czynownik darmo się zaklinał,
Że polowania dotąd jeszcze nie zaczynał,
Że z wielkiego łowczego wielkim pozwoleniem,
Zwierz uszczuty zda mu się być psem, nie jeleniem.
»Jak to? — krzyknął Kiryło — to śmiałbyś, hultaju,
Znać się lepiej na łowach i zwierząt rodzaju
Niźli ja, Kozodusin, carski jegermajster?
Niechajże nas rozsądzi zaraz policmajster!«
Wołają policmajstra, każą spisać śledztwo.
»Ja — rzecze Kozodusin — wydaję świadectwo,
Że to łania; on plecie, że to pies domowy:
Rozsądź nas, kto zna lepiej zwierzynę i łowy!«
Policmajster powinność służby swej rozumiał:
Bardzo się nad zuchwalstwem czynownika zdumiał
I odwiódłszy na stronę po bratersku radził,
By przyznał się do winy i tym grzech swój zgładził.
Łowczy udobruchany przyrzekł, że się wstawi
Do cesarza i wyrok nieco ułaskawi.
Skończyło się, że charty poszły na powrozy,
A czynownik na cztery tygodnie do kozy.
Zabawiła nas cały wieczór ta pustota;
Zrobiła się nazajutrz z tego anegdota,
Że w sądy o mym piesku wielki łowczy wdał się:
I nawet wiem z pewnością, że sam cesarz śmiał się».

    Śmiech powstał w obu izbach. Sędzia z bernardynem
Grał w mariasza i właśnie z wyświeconym winem
Miał coś ważnego zadać: już ksiądz ledwo dyszał,
Kiedy Sędzia początek powieści posłyszał
I tak nią był zajęty, że z zadartą głową,
I z kartą podniesioną, do bicia gotową,
Siedział cicho i tylko bernardyna trwożył.
Aż gdy skończono powieść, pamfila położył,
I rzekł śmiejąc się: «Niech tam sobie kto chce chwali
Niemców cywilizcją, porządek Moskali;
Niechaj Wielkopolanie uczą się od Szwabów
Prawować się o lisa i przyzywać drabów,
By wziąć w areszt ogara, że wpadł w cudze gaje:
Na Litwie, chwała Bogu, stare obyczaje.
Mamy dosyć zwierzyny dla nas i sąsiedztwa,
I nie będziemy nigdy o to robić śledztwa;
I zboża mamy dosyć, psy nas nie ogłodzą,
Że po jarzynach albo po życie pochodzą:
Na morgach chłopskich bronię robić polowanie».

    Ekonom z lewej izby rzekł: «Nie dziw, mospanie,
Bo też pan tak drogo płaci za taką zwierzynę.
Chłopy i radzi temu, kiedy w ich jarzynę
Wskoczy chart; niech otrząśnie dziesięć kłosów żyta:
To pan mu kopę oddasz i jeszcze nie kwita:
Często chłopi talara w przydatku dostali.
Wierz mi pan, że się chłopstwo bardzo rozzuchwali,
Jeśli…» — Reszty dowodów pana Ekonoma
Nie mógł usłyszeć Sędzia; bo pomiędzy dwoma
Rozprawami, wszczęło się dziesięć rozgoworów,
Anegdot, opowiadań i na koniec sporów.

    Tadeusz z Telimeną, całkiem zapomniani,
Pamiętali o sobie. Rada była pani,
Że jej dowcip tak bardzo Tadeusza bawił;
Młodzieniec jej nawzajem komplementy prawił.
Telimena mówiła coraz wolniej, ciszéj,
I Tadeusz udawał, że jej nie dosłyszy
W tłumie rozmów: więc szepcąc tak zbliżył się do niéj,
Że uczuł twarzą lubą gorącość jej skroni;
Wstrzymując oddech, usty chwytał jej westchnienie
I okiem łowił wszystkie jej wzroku promienie.

    Wtem pomiędzy ich usta mignęła znienacka
Naprzód mucha, a za nią tuż Wojskiego placka.

    Na Litwie much dostatek. Jest pomiędzy nimi
Gatunek much osobny, zwanych szlacheckimi.
Barwą i kształtem całkiem podobne do innych,
Ale pierś mają szerszą, brzuch większy od gminnych,
Latając bardzo huczą i nieznośnie brzęczą,
A tak silne, że tkankę przebiją pajęczą,
Lub jeśli która wpadnie, trzy dni będzie bzykać,
Bo z pająkiem sam na sam może się borykać.
Wszystko to Wojski zbadał i jeszcze dowodził,
Że się z tych much szlacheckich pomniejszy lud rodził,
Że one tym są muchom, czym dla roju matki,
Że z ich wybiciem zginą owadów ostatki.
Prawda, że ochmistrzyni ani pleban wioski,
Nie uwierzyli nigdy w te Wojskiego wnioski
I trzymali inaczej o muszym rodzaju;
Lecz Wojski nie odstąpił dawnego zwyczaju:
Ledwo dostrzegł takową muchę, wnet ją gonił.
Właśnie mu teraz szlachcic nad uchem zadzwonił;
Po dwakroć Wojski machnął, zdziwił się, że chybił,
Trzeci raz machnął, tylko co okna nie wybił;
Aż mucha, odurzona od tyla łoskotu,
Widząc dwóch ludzi w progu broniących odwrotu,
Rzuciła się z rozpaczą pomiędzy ich lica;
I tam za nią mignęła Wojskiego prawica.
Raz tak był tęgi, że dwie odskoczyły głowy,
Jak rozdarte piorunem dwie drzewa połowy;
Uderzyły się mocno oboje w uszaki,
Tak, że obojgu sine zostały się znaki.

    Szczęściem, nikt nie uważał; bo dotychczasowa
Żywa, głośna, lecz dosyć porządna rozmowa
Zakończyła się nagłym wybuchem hałasu.
Jak strzelcy, gdy na lisa zaciągną do lasu,
Słychać gdzieniegdzie trzask drzew, strzały, psiarni granie,
A wtem dojeżdżacz dzika ruszył niespodzianie,
Dał znak i wrzask powstaje w strzelców i psów tłuszczy,
Jak gdyby się ozwały wszystkie drzewa puszczy:
Tak dzieje się z rozmową. Z wolna się pomyka:
Aż natrafi na przedmiot wielki, jak na dzika.
Dzikiem rozmów strzeleckich, był ów spór zażarty
Rejenta z Asesorem o sławne ich charty.
Krótko trwał, lecz zrobili wiele w jedną chwilę;
Bo razem wyrzucili słów i obelg tyle,
Że wyczerpnęli sporu zwyczajne trzy części,
Przycinki, gniew, wyzwanie — i szło już do pięści.

    Więc ku nim z drugiej izby wszyscy się porwali,
I tocząc się przeze drzwi na kształt bystrej fali,
Unieśli młodą parę stojącą na progu,
Podobną Janusowi, dwulicemu bogu.

    Tadeusz z Telimeną nim na skroniach włosy
Poprawili, już groźne ucichły odgłosy.
Szmer zmieszany ze śmiechem śród ciżby się szerzył;
Nastąpił rozejm kłótni, kwestarz ją uśmierzył:
Człowiek stary, lecz krępy i bardzo pleczysty.
Właśnie kiedy Asesor podbiegł do jurysty,
Gdy już sobie gestami grozili szermierze,
On raptem porwał obu z tyłu za kołnierze
I dwakroć uderzywszy głowy obie mocne
Jedną o drugą, jako jaja wielkanocne,
Rozkrzyżował ramiona na kształt drogowskazu
I we dwa kąty izby rzucił ich od razu.
Chwilę z rozciągnionymi stał w miejscu rękami,
I «Pax, pax, pax vobiscum — krzyczał — pokój z wami!»

    Zdziwiły się, zaśmiały nawet strony obie.
Przez szacunek, należny duchownej osobie,
Nie śmiano łajać mnicha; a po takiej probie,
Nikt też nie miał ochoty zaczynać z nim zwadę,
Zaś kwestarz Robak, skoro uciszył gromadę,
Widać było, że wcale tryumfu nie szukał,
Ani groził kłótnikom więcej, ani fukał;
Tylko poprawił kaptur, i ręce za pasem
Zatknąwszy, wyszedł cicho z pokoju.

                        Tymczasem
Podkomorzy i Sędzia między dwiema strony
Plac zajęli. Pan Wojski, jakby przebudzony
Z głębokiego dumania, w środku się postawił,
Wąsy siwe pokręcił, kapoty poprawił,
Iskrzyły mu się oczy (zawżdy postrzegano
Ten blask niezwykły, kiedy o łowach gadano),
Obiegał zgromadzenie ognistą źrenicą
I gdzie szmer jeszcze słyszał, jak ksiądz kropielnicą,
Tam uciszając machał swą placką ze skóry;
Wreszcie podniósłszy trzonek z powagą do góry,
Jak laskę marszałkowską, nakazał milczenie.

    «Uciszcie się! — powtarzał — miejcie też baczenie,
Wy, co jesteście pierwsi myśliwi w powiecie,
Z gorszącej kłótni waszej co będzie? czy wiecie?
Oto młodzież, na której Ojczyzny nadzieje,
Która ma wsławiać nasze ostępy i knieje,
Która niestety, i tak zaniedbuje łowy,
Może do ich wzgardzenia weźmie pochop nowy.
Widząc, że ci, co innym mają dać przykłady,
Z łowów przynoszą tylko poswarki i zwady!
Miejcie też wzgląd powinny dla mych włosów siwych;
Bo znałem większych dawniej niźli wy myśliwych,
A sądziłem ich nieraz sądem polubownym.
Któż był w lasach litewskich Rejtanowi równym?
Czy obławę zaciągnąć, czy spotkać się z zwierzem,
Kto z Białopiotrowiczem porówna się Jerzym?
Gdzie jest dziś taki strzelec jak szlachcic Żegota,
Co kulą z pistoletu w biegu trafiał kota?
Terajewicza znałem, co idąc na dziki,
Nie brał nigdy innego oręża prócz piki;
Budrewicza, co chodził z niedźwiedziem w zapasy:
Takich mężów widziały niegdyś nasze lasy!
Jeśli do sporu przyszło, jakże spór godzili?
Oto obrali sędziów i zakład stawili.
Ogiński sto włók lasu raz przegrał o wilka;
Niesiołowskiemu borsuk kosztował wsi kilka!
I wy, panowie, pójdźcie za starych przykładem,
I rozstrzygnijcie spór wasz choć mniejszym zakładem.
Słowo wiatr, w sporach słownych nigdy nie masz końca;
Szkoda ust dłużej suszyć kłótnią o zająca.
Więc polubownych sędziów najpierwej obierzcie,
A co wyrzekną, temu sumiennie zawierzcie.
Ja uproszę Sędziego, ażeby nie bronił
Dojeżdżaczowi, choćby po pszenicy gonił;
I tuszę, że tę łaskę otrzymam od pana».
To wyrzekłszy, Sędziego ścisnął za kolana.

    «Konia — zawołał Rejent — stawię konia z rzędem,
I opiszę się jeszcze przed ziemskim urzędem,
Iż ten pierścień Sędziemu w salarijum złożę».
«Ja — rzekł Asesor — stawię me złote obroże,
Jaszczurem wykładane, z kółkami ze złota,
I smycz tkany jedwabny, którego robota
Równie cudna jak kamień, co się na nim świeci.
Chciałem ten sprzęt zostawić w dziedzictwie dla dzieci,
Jeślibym się ożenił: ten sprzęt mnie darował
Książę Dominik, kiedym z nim razem polował
I z marszałkiem Sanguszką księciem, z jenerałem
Mejenem, i gdy wszystkich na charty wyzwałem.
Tam, bezprzykładną w dziejach polowania sztuką,
Uszczułem sześć zajęcy pojedynczą suką.
Polowaliśmy wtenczas na Kupiskim błoniu;
Książę Radziwiłł nie mógł dosiedzieć na koniu:
Zsiadł i, objąwszy sławną mą charcicę Kanię,
Trzykroć jej w samą głowę dał pocałowanie,
A potem trzykroć ręką klasnąwszy po pysku,
Rzekł: »Mianuję cię odtąd księżną na Kupisku«.
Tak Napoleon daje wodzom swoim księstwa
Od miejsc, na których wielkie odnieśli zwycięstwa».

    Telimena, znudzona zbyt długimi swary,
Chciała wyjść na dziedziniec, lecz szukała pary;
Wzięła koszyczek z kołka: «Panowie, jak widzę,
Chcecie zostać w pokoju, ja idę na rydze;
Kto łaska, proszę za mną» — rzekła, koło głowy
Obwijając czerwony szal kaszemirowy;
Córeczkę Podkomorstwa wzięła w jedną rękę,
A drugą podchyliła do kostek sukienkę.
Tadeusz milczkiem za nią na grzyby pośpieszył.

    Zamiar przechadzki bardzo Sędziego ucieszył;
Widział sposób rozjęcia krzykliwego sporu,
A więc krzyknął: «Panowie, po grzyby do boru!
Kto z najpiękniejszym rydzem do stołu przybędzie,
Ten obok najpiękniejszej panienki usiędzie:
Sam ją sobie wybierze. Jeśli znajdzie dama,
Najpiękniejszego chłopca weźmie sobie sama».




Księga trzecia



Umizgi

Wyprawa Hrabiego na sad — Tajemnicza nimfa gęsi pasie — Podobieństwo grzybobrania do przechadzki cieniów elizejskich — Gatunki grzybów — Telimena w świątyni dumania — Narady tyczące się postanowienia Tadeusza — Hrabia pejzażysta — Tadeusza uwagi malarskie nad drzewami i obłokami — Hrabiego myśl o sztuce — Dzwon — Bilecik — Niedźwiedź, mospanie!

    Hrabia wracał do siebie; lecz konia wstrzymywał,
Głową coraz w tył kręcił, w ogród się wpatrywał.
I raz mu się zdawało, że znowu z okienka
Błysnęła tajemnicza, bieluchna sukienka
I coś lekkiego znowu upadło z wysoka,
I przeleciawszy cały ogród w mgnieniu oka,
Pomiędzy zielonymi świeciło ogórki:
Jako promień słoneczny, wykradłszy się z chmurki,
Kiedy śród roli padnie na krzemienia skibę
Lub śród zielonej łąki w drobną wody szybę.

    Hrabia zsiadł z konia, sługi odprawił do domu,
A sam ku ogrodowi ruszył po kryjomu.
Dobiegł wkrótce parkanu, znalazł w nim otwory
I wcisnął się po cichu, jak wilk do obory.
Nieszczęściem, trącił krzaki suchego agrestu:
Ogrodniczka, jak gdyby zlękła się szelestu,
Oglądała się wkoło, lecz nic nie spostrzegła;
Przecież ku drugiej stronie ogrodu pobiegła.
A Hrabia bokiem, między wielkie końskie szczawie,
Między liście łopuchu, na rękach, po trawie,
Skacząc jak żaba, cicho przyczołgał się blisko,
Wytknął głowę i ujrzał cudne widowisko.

    W tej części sadu rosły tu i ówdzie wiśnie,
Śród nich zboże w gatunkach zmieszanych umyślnie:
Pszenica, kukuruza, bób, jęczmień wąsaty,
Proso, groszek, a nawet krzewiny i kwiaty.
Domowemu to ptactwu taki ochmistrzyni
Wymyśliła ogródek: sławna gospodyni,
Zwała się Kokosznicka, z domu Jendykowi-
czówna. Jej wynalazek epokę stanowi
W domowym gospodarstwie; dziś powszechnie znany,
Lecz w owych czasach jeszcze za nowość podany,
Przyjęty pod sekretem od niewielu osób,
Nim go wydał kalendarz, pod tytułem: Sposób
Na jastrzębie i kanie, albo nowy środek
Wychowywania drobiu — był to ów ogrodek.

    Jakoż, zaledwie kogut, co odprawia warty,
Stanie i nieruchomie dzierżąc dziób zadarty,
I głowę grzebieniastą pochyliwszy bokiem,
Aby tym łacniej w niebo mógł celować okiem,
Dostrzeże wiszącego jastrzębia śród chmury,
Krzyknie: zaraz w ten ogród chowają się kury,
Nawet gęsi i pawie, i w nagłym przestrachu
Gołębie, gdy nie mogą schronić się na dachu.

    Teraz w niebie żadnego nie widziano wroga;
Tylko skwarzyła słońca letniego pożoga.
Od niej ptaki w zbożowym ukryły się lasku;
Tamte leżą w murawie, te kąpią się w piasku.

    Śród ptaszych głów sterczały główki ludzkie małe,
Odkryte; włosy na nich krótkie, jak len białe;
Szyje nagie do ramion; a pomiędzy nimi
Dziewczyna głową wyższa, z włosami dłuższymi.
Tuż za dziećmi paw siedział i piór swych obręcze
Szeroko rozprzestrzenił w różnofarbną tęczę,
Na której główki białe, jak na tle obrazku,
Rzucone w ciemny błękit, nabierały blasku.
Obrysowane wkoło kręgiem pawich oczu
Jak wiankiem gwiazd, świeciły w zbożu jak w przezroczu,
Pomiędzy kukuruzy złocistymi laski,
I angielską trawicą posrebrzaną w paski,
I szczyrem koralowym, i zielonym ślazem;
Których kształty i barwy mieszały się razem
Niby krata ze srebra i złota pleciona,
A powiewna od wiatru jak lekka zasłona.

    Nad gęstwą różnofarbnych kłosów i badylów
Wisiała jak baldachim jasna mgła motylów,
Zwanych babkami, których poczwórne skrzydełka
Lekkie jak pajęczyna, przejrzyste jak szkiełka,
Gdy w powietrzu zawisną, zaledwo widome,
I chociaż brzęczą, myślisz, że są nieruchome.

    Dziewczyna powiewała podniesioną w ręku
Szarą kitką, podobną do piór strusich pęku;
Nią zdała się oganiać główki niemowlęce
Od złotego motylów deszczu. W drugiej ręce
Coś u niej rogatego, złocistego świeci,
Zdaje się, że naczynie do karmienia dzieci:
Bo je zbliżała dzieciom do ust po kolei;
Miało zaś kształt złotego rogu Amaltei.

    Tak zatrudniona, przecież obracała głowę
Na pamiętne szelestem krzaki agrestowe,
Nie wiedząc, że napastnik już z przeciwnej strony
Przybliżył się, czołgając jak wąż przez zagony,
Aż wyskoczył z łopuchu. Spojrzała — stał blisko,
O cztery grzędy od niej, i kłaniał się nisko.
Już głowę odwróciła i wzniosła ramiona,
I zrywała się lecieć jak kraska spłoszona,
I już lekkie jej stopy wionęły nad liściem,
Kiedy dzieci, przelękłe podróżnego wniściem
I ucieczką dziewczyny, wrzasnęły okropnie.
Posłyszała, uczuła, że jest nieroztropnie
Dziatwę małą, przelękłą i samą porzucić:
Wracała, wstrzymując się, lecz musiała wrócić,
Jak niechętny duch, wróżka przyzwany zaklęciem,
Przybiegła z najkrzykliwszym bawić się dziecięciem,
Siadła przy nim na ziemi, wzięła je na łono;
Drugie głaskała ręką i mową pieszczoną;
Aż się uspokoiły, objąwszy w rączęta
Jej kolana i tuląc główki jak pisklęta
pod skrzydło matki. Ona rzekła: «Czy to pięknie
Tak krzyczeć? Czy to grzecznie? Ten pan się zalęknie.
Ten pan nie przyszedł straszyć; to nie dziad szkaradny,
To gość, dobry pan, patrzcie tylko jaki ładny».

    Sama spojrzała: Hrabia uśmiechnął się mile,
I widocznie był wdzięczny jej za pochwał tyle;
Postrzegła się, umilkła, oczy opuściła
I jako róży pączek cała się spłoniła.

    W istocie był to piękny pan: słusznej urody,
Twarz miał pociągłą, blade lecz świeże jagody,
Oczy modre, łagodne, włos długi, białawy;
Na włosach listki ziela i kosmyki trawy,
Które Hrabia oberwał pełznąc przez zagony,
Zieleniły się jako wieniec rozpleciony.

    «O ty — rzekł — jakimkolwiek uczczę cię imieniem,
Bóstwem jesteś czy nimfą, duchem czy widzeniem!
Mów: własna li cię wola na ziemię sprowadza,
Obca li więzi ciebie na padole władza?
Ach, domyślam się, — pewnie wzgardzony miłośnik,
Jaki pan możny, albo opiekun zazdrośnik,
W tym cię parku zamkowym jak zaklętą strzeże!
Godna, by o cię bronią walczyli rycerze,
Byś została romansów heroiną smutnych!
Odkryj mi, piękna, tajnie twych losów okrutnych!
Znajdziesz wybawiciela. Odtąd twym skinieniem,
Jak rządzisz sercem moim, tak rządź mym ramieniem».
Wyciągnął ramię.

                        Ona z rumieńcem dziewiczym,
Ale z rozweselonym słuchała obliczem.
Jak dziecię lubi widzieć obrazki jaskrawe
I w liczmanach błyszczących znajduje zabawę,
Nim rozezna ich wartość: tak się słuch jej pieści
Z dźwięcznymi słowy, których nie pojęła treści.
Na koniec zapytała: «Skąd tu pan przychodzi?
I czego tu po grzędach szuka pan dobrodziéj?»

    Hrabia oczy roztworzył. Zmieszany, zdziwiony,
Milczał; wreszcie, zniżając swej rozmowy tony:
«Przepraszam — rzekł — panienko! Widzę, żem pomieszał
Zabawy! Ach, przepraszam: jam właśnie pośpieszał
Na śniadanie: już późno, chciałem na czas zdążyć;
Panienka wie, że drogą trzeba wkoło krążyć,
Przez ogród zdaje mi się jest do dworu prościéj».
Dziewczyna rzekła: «Tędy droga jegomości;
Tylko grząd psuć nie trzeba. Tam, między murawą
Ścieżka». — «W lewo — zapytał Hrabia — czy na prawo?»
Ogrodniczka, podniósłszy błękitne oczęta,
Zdawała się go badać ciekawością zdjęta:
Bo dom o tysiąc kroków widny jak na dłoni,
A Hrabia drogi pyta? Ale Hrabia do niéj
Chciał koniecznie coś mówić i szukał powodu
Rozmowy: «Panna mieszka tu? blisko ogrodu?
Czy na wsi? Jak to było, żem panny we dworze
Nie widział? czy niedawno tu? przyjezdna może?»
Dziewczę wstrząsnęło głową. — «Przepraszam, panienko,
Czy nie tam pokój panny, gdzie owe okienko?»

    Myślił zaś w duchu: jeśli nie jest heroiną
Romansów, jest młodziuchną, prześliczną dziewczyną.
Zbyt często wielka dusza, myśl wielka ukryta
W samotności, jak róża śród lasów rozkwita;
Dosyć ją wynieść na świat, postawić przed słońcem,
Aby widzów zdziwiła jasnych barw tysiącem!

    Ogrodniczka tymczasem powstała w milczeniu,
Podniosła jedno dziecię zwisłe na ramieniu,
Drugie wzięła za rękę, a kilkoro przodem
Zaganiając jak gąski, szła dalej ogrodem.

    Odwróciwszy się rzekła: «Czy też pan nie może
Rozbiegłe moje ptastwo wpędzić nazad w zboże?»
«Ja, ptastwo pędzać?» krzyknął Hrabia z zadziwieniem;
Ona tymczasem znikła, zakryta drzew cieniem.
Chwilę jeszcze z szpaleru, przez majowe zwoje,
Przeświecało coś na wskroś jakby oczu dwoje.

    Samotny Hrabia długo jeszcze stał w ogrodzie.
Dusza jego, jak ziemia po słońca zachodzie,
Ostygała powoli, barwy brała ciemne;
Zaczął marzyć, lecz sny miał bardzo nieprzyjemne.
Zbudził się, sam nie wiedząc, na kogo się gniewał:
Niestety, mało znalazł! nadto się spodziewał!
Bo gdy zagonem pełzał ku owej pasterce,
Paliło mu się w głowie, skakało w nim serce;
Tyle wdzięków w tajemnej nimfie upatrywał,
W tyle ją cudów ubrał, tyle odgadywał!
Wszystko znalazł inaczej: prawda, że twarz ładną,
Kibić miała wysmukłą, ale jak nieskładną!
A owa pulchność liców i rumieńca żywość,
Malująca zbyteczną, prostacką szczęśliwość!
Znak, że myśl jeszcze drzemie, że serce nieczynne!
I owe odpowiedzi, tak wiejskie, tak gminne!
«Po cóż się łudzić — krzyknął — zgaduję po czasie:
Moja nimfa tajemna pono gęsi pasie!»

    Z nimfy zniknieniem, całe czarowne przezrocze
Zmieniło się. Te wstęgi, te kraty urocze
Złote, srebrne: niestety! więc to była słoma?

    Hrabia z załamanymi poglądał rękoma
Na snopek uwiązanej trawami mietlicy,
Którą brał za pęk strusich piór w ręku dziewicy.
Nie zapomniał naczynia: złocista konewka,
Ów rożek Amaltei, była to marchewka!
Widział ją w ustach dziecka pożeraną chciwie:
Więc było po uroku! po czarach! po dziwie!

    Tak chłopiec, kiedy ujrzy cykoryi kwiaty,
Wabiące dłoń miękkimi, lekkimi bławaty,
Chce je pieścić, zbliża się, dmuchnie: i z podmuchem
Cały kwiat na powietrzu rozleci się puchem,
A w ręku widzi tylko badacz zbyt ciekawy
Nagą łodygę szarozielonawej trawy.

    Hrabia wcisnął na oczy kapelusz i wracał
Tamtędy, kędy przyszedł; ale drogę skracał,
Stąpając po jarzynach, kwiatach i agreście,
Aż, przeskoczywszy parkan, odetchnął nareście!
Przypomniał, że dziewczynie mówił o śniadaniu;
Może już wszyscy wiedzą o jego spotkaniu
W ogrodzie, blisko domu? może szukać wyślą?
Postrzegli, że uciekał? kto wie, co pomyślą?
Więc wypadało wrócić. Chyląc się u płotów
Około miedz i zielska, po tysiącach zwrotów
Rad był przecież, że wyszedł w końcu na gościniec,
Który prosto prowadził na dworski dziedziniec.
Szedł przy płocie, a głowę odwracał od sadu.
Jak złodziej od spichlerza, aby nie dać śladu,
Że go myśli nawiedzić albo już nawiedził:
Tak Hrabia był ostrożny, choć go nikt nie śledził;
Patrzył w stronę przeciwną ogrodu, na prawo.

    Był gaj z rzadka zarosły, wysłany murawą.
Po jej kobiercach, na wskroś białych pniów brzozowych,
Pod namiotem obwisłych gałęzi majowych,
Snuło się mnóstwo kształtów, których dziwne ruchy,
Niby tańce, i dziwny ubiór: istne duchy
Błądzące po księżycu. Tamci w czarnych, ciasnych,
Ci w długich, rozpuszczonych szatach jak śnieg jasnych;
Tamten pod kapeluszem jak obręcz szerokim,
Ten z gołą głową; inni jak gdyby obłokiem
Obwiani, idąc, na wiatr puszczają zasłony,
Ciągnące się za głową, jak komet ogony.
Każdy w innej postawie: ten przyrósł do ziemi,
Tylko oczyma kręci na dół spuszczonemi;
Ów, patrząc wprost przed siebie, niby senny kroczy,
Jak po linie, ni w prawo, ni w lewo nie zboczy;
Wszyscy zaś ciągle w różne schylają się strony
Aż do ziemi, jak gdyby wybijać pokłony.
Jeżeli się przybliżą albo się spotkają,
Ani mówią do siebie, ani się witają,
Głęboko zadumani, w sobie pogrążeni.
Hrabia widział w nich obraz elizejskich cieni,
Które, chociaż boleściom, troskom niedostępne,
Błąkają się spokojne, ciche, lecz posępne.

    Któż by zgadnął, że owi tak mało ruchomi,
Owi milczący ludzie — są nasi znajomi,
Sędziowscy towarzysze? Z hucznego śniadania
Wyszli na uroczysty obrzęd grzybobrania.
Jako ludzie rozsądni, umieją miarkować
Mowy i ruchy swoje, aby je stosować
W każdej okoliczności do miejsca i czasu.
Dlatego, nim ruszyli za Sędzią do lasu,
Wzięli postawy tudzież ubiory odmienne,
Służące do przechadzki opończe płócienne,
Którymi osłaniają po wierzchu kontusze,
A na głowy słomiane wdziali kapelusze.
Stąd biali wyglądają jak czyśćcowe dusze.
Młodzież także przebrana, oprócz Telimeny
I kilku po francusku chodzących.

                        Tej sceny
Hrabia nie pojął; nie znał wiejskiego zwyczaju:
Więc zdziwiony niezmiernie biegł pędem do gaju.

Grzybów było w bród. Chłopcy biorą krasnolice,
Tyle w pieśniach litewskich sławione *lisice*,
Co są godłem panieństwa: bo czerw ich nie zjada,
I dziwna, żaden owad na nich nie usiada.
Panienki za wysmukłym gonią *borowikiem*,
Którego pieśń nazywa grzybów pułkownikiem.
Wszyscy dybią na *rydza*; ten wzrostem skromniejszy
I mniej sławny w piosenkach, za to najsmaczniejszy,
Czy świeży, czy solony, czy jesiennej pory,
Czy zimą. Ale Wojski zbierał *muchomory*.

    Inne pospólstwo grzybów, pogardzone w braku
Dla szkodliwości albo niedobrego smaku,
Lecz nie są bez użytku: one zwierza pasą
I gniazdem są owadów i gajów okrasą.
Na zielonym obrusie łąk, jako szeregi
Naczyń stołowych sterczą: tu z krągłymi brzegi
*Surojadki* srebrzyste, żółte i czerwone,
Niby czareczki różnym winem napełnione;
*Koźlak*, jak przewrócone kubka dno wypukłe,
*Lejki*, jako szampańskie kieliszki wysmukłe,
*Bielaki* krągłe, białe, szerokie i płaskie,
Jakby mlekiem nalane filiżanki saskie,
I kulista, czarniawym pyłkiem napełniona
*Purchawka*, jak pieprzniczka; zaś innych imiona,
Znane tylko w zajęczym lub wilczym języku,
Od ludzi nieochrzczone; a jest ich bez liku.
Ni wilczych, ni zajęczych nikt dotknąć nie raczy;
A kto schyla się ku nim, gdy błąd swój obaczy,
Zagniewany, grzyb złamie albo nogą kopnie:
Tak szpecąc trawę, czyni bardzo nieroztropnie.

    Telimena ni wilczych, ni ludzkich nie zbiera.
Roztargniona, znudzona, dokoła spoziera,
Z głową w górę zadartą. Więc pan Rejent w gniewie
Mówił o niej, że grzybów szukała na drzewie;
Asesor ją złośliwiej równał do samicy,
Która miejsca na gniazdo szuka w okolicy.

    Jakoż zdała się szukać samotności, ciszy.
Oddalała się z wolna od swych towarzyszy,
I szła lasem na wzgórek pochyło wyniosły,
Ocieniony, bo drzewa gęściej na nim rosły.
W środku szarzał się kamień; strumień spod kamienia
Szumiał, tryskał i zaraz, jakby szukał cienia,
Chował się między gęste i wysokie zioła,
Które wodą pojone bujały dokoła;
Tam ów bystry swawolnik, spowijany w trawy
I liściem podesłany, bez ruchu, bez wrzawy,
Niewidzialny i ledwie dosłyszany szepce,
Jako dziecię krzykliwe złożone w kolebce,
Gdy matka nad nim zwiąże firanki majowe
I liścia makowego nasypie pod głowę.
Miejsce piękne i ciche: tu się często schrania
Telimena, zowiąc je *Świątynią dumania*.

    Stanąwszy nad strumieniem, rzuciła na trawnik
Z ramion swój szal powiewny, czerwony jak krwawnik;
I podobna pływaczce, która do kąpieli
Zimnej schyla się, nim się zanurzyć ośmieli,
Klęknęła i powoli chyliła się bokiem;
Wreszcie, jakby porwana koralu potokiem,
Upadła nań i cała wzdłuż się rozpostarła.
Łokcie na trawie, skronie na dłoniach oparła,
Z głową na dół skłonioną; na dole u głowy,
Błysnął francuskiej książki papier welinowy;
Nad alabastrowymi stronicami księgi,
Wiły się czarne pukle i różowe wstęgi.

    W szmaragdzie bujnych traw, na krwawnikowym szalu,
W sukni długiej, jak gdyby w powłoce koralu,
Od której odbijał się włos z jednego końca,
Z drugiego czarny trzewik; po bokach błyszcząca
Śnieżną pończoszką, chustką, białością rąk, lica,
Wydawała się z dala jak pstra gąsienica,
Gdy wpełźnie na zielony liść klonu.

                        Niestety!
Wszystkie tego obrazu wdzięki i zalety
Darmo czekały znawców, nikt nie zważał na nie,
Tak mocno zajmowało wszystkich grzybobranie.
Tadeusz przecież zważał i w bok strzelał okiem,
I nie śmiejąc iść prosto, przysuwał się bokiem:
Jak strzelec, gdy w ruchomej gałęzistej szopie,
Usiadłszy na dwóch kołach, podjeżdża na dropie,
Albo na siewki idąc, przy koniu się kryje,
Strzelbę złoży na siodle lub pod końską szyję,
Niby to bronę włóczy, niby jedzie miedzą,
A coraz się przybliża, kędy ptaki siedzą:
Tak skradał się Tadeusz.

                        Sędzia czaty zmieszał
I przeciąwszy mu drogę, do źródła pośpieszał.
Z wiatrem igrały białe poły sarafana
I wielka chustka w pasie końcem uwiązana;
Słomiany, podwiązany kapelusz od ruchu
Nagłego chwiał się z wiatrem jako liść łopuchu,
Spadając to na barki, to znowu na oczy;
W ręku ogromna laska: tak pan Sędzia kroczy.
Schyliwszy się i ręce obmywszy w strumieniu,
Usiadł przed Telimeną na wielkim kamieniu,
I, wsparłszy się oburącz na gałkę słoniową
Trzciny ogromnej, z taką ozwał się przemową:

    «Widzi aśćka, od czasu jak tu u nas gości
Tadeuszek, niemało mam niespokojności.
Jestem bezdzietny, stary; ten dobry chłopczyna,
Wszak to moja na świecie pociecha jedyna,
Przyszły dziedzic fortunki mojej. Z łaski nieba,
Zostawię mu kęs niezły szlacheckiego chleba;
Już mu też czas obmyśleć los, postanowienie;
Ale zważaj no, aśćka, moje utrapienie!
Wiesz, że pan Jacek, brat mój, Tadeusza ociec,
Dziwny człowiek, zamiarów jego trudno dociec,
Nie chce wracać do kraju, Bóg wie gdzie się kryje,
Nawet nie chce synowi oznajmić, że żyje,
A ciągle nim zarządza. Naprzód w legijony
Chciał go posyłać; byłem okropnie zmartwiony.
Potem zgodził się przecie, by w domu pozostał
I żeby się ożenił. Jużbyć żony dostał;
Partyję upatrzyłem. Nikt z obywateli
Nie wyrówna z imienia ani z parenteli
Podkomorzemu; jego starsza córka Anna
Jest na wydaniu, piękna i posażna panna;
Chciałem zagaić». Na to Telimena zbladła,
Złożyła książkę, wstała nieco i usiadła.

    «Jak mamę kocham — rzekła — czy to, panie bracie,
Jest w tym sens jaki, czy wy Boga w sercu macie?
To myślisz Tadeusza zostać dobrodziejem,
Jeśli młodego chłopca zrobisz grykosiejem?
Świat mu zawiążesz! wierz mi, kląć was kiedyś będzie!
Zakopać taki talent w lasach i na grzędzie!
Wierz mi, ile poznałam, pojętne to dziecię,
Warto, żeby na wielkim przetarło się świecie.
Dobrze brat zrobi, gdy go do stolicy wyśle,
Na przykład do Warszawy? Lub wie brat, co myślę…
Żeby do Peterburka? Ja pewnie tej zimy
Pojadę tam dla sprawy; razem ułożymy,
Co zrobić z Tadeuszem. Znam tam wiele osób,
Mam wpływy: to najlepszy kreacyi sposób.
Za mą pomocą, znajdzie wstęp w najpierwsze domy,
A kiedy będzie ważnym osobom znajomy,
Dostanie urząd, order; wtenczas niech porzuci
Służbę, jeżeli zechce, niech do domu wróci,
Mając już i znaczenie, i znajomość świata.
I cóż brat myśli o tym?» — «Jużci, w młode lata —
Rzekł Sędzia — nieźle chłopcu trochę się przewietrzyć,
Obejrzeć się na świecie, między ludźmi przetrzéć;
Ja za młodu niemało świata objechałem:
Byłem w Piotrkowie, w Dubnie, to za trybunałem
Jadąc jako palestrant, to własne swe sprawy
Forytując, jeździłem nawet do Warszawy.
Człek niemało skorzystał! Chciałbym i synowca
Wysłać pomiędzy ludzi, prosto jak wędrowca,
Jak czeladnika, który terminuje lata,
Ażeby nabył trochę znajomości świata.
Nie dla rang ni orderów! Proszę uniżenie,
Ranga moskiewska, order: cóż to za znaczenie?
Któryż to z dawnych panów, ba, nawet dzisiejszych,
Między szlachtą w powiecie nieco zamożniejszych,
Dba o podobne fraszki? Przecież są w estymie
U ludzi; bo szanujem w nich ród, dobre imię,
Albo urząd, lecz ziemski, przyznany wyborem
Obywatelskim, nie zaś czyimś tam faworem».

    Telimena przerwała: «Jeśli brat tak myśli,
Tym lepiej, więc go jako wojażera wyślij».

    «Widzi siostra — rzekł Sędzia, skrobiąc smutnie głowę —
Chciałbym bardzo: cóż, kiedy mam trudności nowe!
Pan Jacek nie wypuszcza z opieki swej syna,
I przysłał mi tu właśnie na kark bernardyna
Robaka, który przybył z tamtej strony Wisły,
Przyjaciel brata, wszystkie wie jego zamysły;
A więc o Tadeusza już wyrzekli losie,
I chcą, by się ożenił, aby pojął Zosię,
Wychowankę waćpani. Oboje dostaną,
Oprócz fortunki mojej, z łaski Jacka wiano
W kapitałach; wiesz aśćka, że ma kapitały,
I z łaski jego mam też fundusz prawie cały:
Ma więc prawo rozrządzać… aśćka pomyśl o tem,
Żeby się to zrobiło najmniejszym kłopotem.
Trzeba ich z sobą poznać. Prawda, bardzo młodzi,
Szczególnie Zosia mała, lecz to nic nie szkodzi.
Czas by już Zośkę wreszcie wydobyć z zamknięcia.
Bo wszakci to już pono wyrasta z dziecięcia».

    Telimena zdziwiona i prawie wylękła
Podnosiła się coraz, na szalu uklękła;
Zrazu słuchała pilnie, potem dłoni ruchem
Przeczyła, ręką żwawo wstrząsając nad uchem,
Odpędzając jak owad nieprzyjemne słowa
Na powrót w usta mówcy —

                        «A! a! to rzecz nowa!
Czy to Tadeuszowi szkodzi, czy nie szkodzi —
Rzekła z gniewem — sądź o tym sam waćpan dobrodziéj!
Mnie nic do Tadeusza; sami o nim radźcie,
Zróbcie go ekonomem lub w karczmie posadźcie,
Niech szynkuje lub z lasu niech zwierzynę znosi:
Z nim sobie, co zechcecie, zróbcie. Lecz do Zosi?
Co waćpaństwu do Zosi? Ja jej ręką rządzę,
Ja sama! Że pan Jacek dawał był pieniądze
Na wychowanie Zosi, i że jej wyznaczył
Małą pensyjkę roczną, więcej przyrzec raczył,
Toć jej jeszcze nie kupił. Zresztą, państwo wiecie,
I dotąd jeszcze o tym wiadomo na świecie,
Że hojność państwa dla nas nie jest bez powodu,
Winni coś Soplicowie dla Horeszków rodu».
(Tej części mowy Sędzia słuchał z niepojętem
Pomieszaniem, żałością i widocznym wstrętem;
Jakby lękał się reszty mowy, głowę skłonił,
I ręką potakując, mocno się zapłonił.)

    Telimena kończyła: «Byłam jej piastunką,
Jestem krewną, jedyną Zosi opiekunką.
Nikt oprócz mnie nie będzie myślił o jej szczęściu».
«A jeśli ona szczęście znajdzie w tym zamęściu? —
Rzekł Sędzia wzrok podnosząc. — Jeśli Tadeuszka
Podoba?» — «Czy podoba? to na wierzbie gruszka!
Podoba, nie podoba: a to mi rzecz ważna!
Zosia nie będzie, prawda, partyja posażna;
Ale też nie jest z lada wsi, lada szlachcianka,
Idzie z jaśnie wielmożnych, jest wojewodzianka,
Rodzi się z Horeszkówny; małżonka dostanie!
Staraliśmy się tyle o jej wychowanie!
Chybaby tu zdziczała». Sędzia pilnie słuchał,
Patrząc w oczy; zdało się, że się udobruchał,
Bo rzekł dosyć wesoło: «No, to i cóż robić!
Bóg widzi, szczerze chciałem interesu dobić;
Tylko bez gniewu. Jeśli aśćka się nie zgodzi,
Aśćka ma prawo; smutno: gniewać się nie godzi.
Radziłem, bo brat kazał; nikt tu nie przymusza.
Gdy aśćka rekuzuje pana Tadeusza,
Odpisuję Jackowi, że nie z mojej winy
Nie dojdą Tadeusza z Zosią zaręczyny.
Teraz sam będę radzić. Pono z Podkomorzym
Zagaimy swatowstwo i resztę ułożym».

    Przez ten czas Telimena ostygła z zapału:
«Ja nic nie rekuzuję, braciszku, pomału!
Sam mówiłeś, że jeszcze za wcześnie — zbyt młodzi, —
Rozpatrzmy się, czekajmy, nic to nie zaszkodzi,
Poznajmy z sobą państwo młodych, będziem zważać;
Nie można szczęścia drugich tak na traf narażać.
Ostrzegam tylko wcześnie: niech brat Tadeusza
Nie namawia, kochać się w Zosi nie przymusza;
Bo serce nie jest sługa, nie zna co to pany,
I nie da się przemocą okuwać w kajdany».

    Za czym Sędzia, powstawszy, odszedł zamyślony.
Pan Tadeusz z przeciwnej przybliżył się strony,
Udając, że szukanie grzybów tam go zwabia.
W tymże kierunku z wolna posuwa się Hrabia.

    Hrabia podczas Sędziego sporów z Telimeną
Stał za drzewami, mocno zdziwiony tą sceną.
Dobył z kieszeni papier i ołówek, sprzęty,
Które zawsze miał z sobą, i na pień wygięty,
Rozpiąwszy kartkę, widać, że obraz malował,
Mówiąc sam z sobą: «Jakbyś umyślnie grupował:
Ten na głazie, ta w trawie; grupa malownicza!
Głowy charakterowe! z kontrastem oblicza!»

    Podchodził, wstrzymywał się, lornetkę przecierał,
Oczy chustką obwiewał i coraz spozierał:
«Miałożby to cudowne, śliczne widowisko
Zginąć albo zmienić się, gdy podejdę blisko?
Ten aksamit traw, będzież to mak i botwinie?
W nimfie tej czyż obaczę jaką ochmistrzynię?»

    Choć Hrabia Telimenę już dawniej widywał
W domu Sędziego, w którym dosyć często bywał,
Lecz mało ją uważał: zadziwił się zrazu,
Rozeznając w niej model swojego obrazu.
Miejsca piękność, postawy wdzięk i gust ubrania
Zmieniły ją, zaledwo była do poznania.
W oczach świeciły jeszcze niezagasłe gniewy;
Twarz, ożywiona wiatru świeżymi powiewy,
Sporem z Sędzią i nagłym przybyciem młodzieńców,
Nabrała mocnych, żywszych niż zwykle rumieńców.

    «Pani — rzekł Hrabia — racz mej śmiałości darować;
Przychodzę i przepraszać, i razem dziękować.
Przepraszać, że jej kroków śledziłem ukradkiem;
I dziękować, że byłem jej dumania świadkiem.
Tyle ją obraziłem! winienem jej tyle!
Przerwałem chwilę dumań; winienem ci chwile
Natchnienia, chwile błogie! Potępiaj człowieka;
Ale sztukmistrz twojego przebaczenia czeka!
Na wielem się odważył, na więcej odważę:
Sądź!» — tu ukląkł i podał swoje pejzaże.

    Telimena sądziła malowania proby
Tonem grzecznej, lecz sztukę znającej osoby;
Skąpa w pochwały, lecz nie szczędziła zachętu:
«Brawo — rzekła — winszuję, niemało talentu.
Tylko pan nie zaniedbuj; szczególniej potrzeba
Szukać pięknej natury! O, szczęśliwe nieba
Krajów włoskich! różowe cezarów ogrody!
Wy, klasyczne Tyburu spadające wody!
I straszne Pauzylipu skaliste wydroże!
To, Hrabio, kraj malarzów! U nas, żal się Boże!…
Dziecko muz, w Soplicowie oddane na mamki,
Umrze pewnie. Mój Hrabio, oprawię to w ramki,
Albo w album umieszczę, do rysunków zbiorku,
Które zewsząd skupiałam: mam ich dosyć w biurku».

    Zaczęli więc rozmowę o niebios błękitach,
Morskich szumach i wiatrach wonnych, i skał szczytach,
Mieszając tu i ówdzie, podróżnych zwyczajem,
Śmiech i urąganie się nad ojczystym krajem.

    A przecież wokoło nich ciągnęły się lasy
Litewskie, tak poważne i tak pełne krasy!
Czeremchy oplatane dzikich chmielów wieńcem,
Jarzębiny ze świeżym pasterskim rumieńcem,
Leszczyna jak menada z zielonymi berły,
Ubranymi jak w grona, w orzechowe perły;
A niżej dziatwa leśna: głóg w objęciu kalin,
Ożyna czarne usta tuląca do malin.
Drzewa i krzewy liśćmi wzięły się za ręce,
Jak do tańca stające panny i młodzieńce
Wkoło pary małżonków. Stoi pośród grona
Para, nad całą leśną gromadą wzniesiona
Wysmukłością kibici i barwy powabem:
Brzoza biała, kochanka, z małżonkiem swym grabem.
A dalej, jakby starce na dzieci i wnuki
Patrzą, siedząc w milczeniu, tu sędziwe buki,
Tam matrony topole i mchami brodaty
Dąb, włożywszy pięć wieków na swój kark garbaty,
Wspiera się, jak na grobów połamanych słupach,
Na dębów, przodków swoich, skamieniałych trupach.

    Pan Tadeusz kręcił się, nudząc niepomału
Długą rozmową, w której nie mógł brać udziału.
Aż, gdy zaczęto sławić cudzoziemskie gaje,
I wyliczać z kolei wszystkich drzew rodzaje:
Pomarańcze, cyprysy, oliwki, migdały,
Kaktusy, aloesy, mahonie, sandały,
Cytryny, bluszcz, orzechy włoskie, nawet figi,
Wysławiając ich kształty, kwiaty i łodygi:
Tadeusz nie przestawał dąsać się i zżymać,
Na koniec nie mógł dłużej od gniewu wytrzymać.

    Był on prostak, lecz umiał czuć wdzięk przyrodzenia,
I patrząc w las ojczysty, rzekł pełen natchnienia:
«Widziałem w botanicznym wileńskim ogrodzie,
Owe sławione drzewa rosnące na wschodzie
I na południu, w owej pięknej włoskiej ziemi;
Któreż równać się może z drzewami naszemi?
Czy aloes z długimi jak konduktor pałki?
Czy cytryna, karlica z złocistymi gałki,
Z liściem lakierowanym, krótka i pękata,
Jako kobieta mała, brzydka, lecz bogata?
Czy zachwalony cyprys długi, cienki, chudy,
Co zdaje się być drzewem nie smutku, lecz nudy?
Mówią, że bardzo smutnie wygląda na grobie;
Jest to jak lokaj Niemiec we dworskiej żałobie,
Nieśmiejący rąk podnieść ani głowy skrzywić,
Aby się etykiecie niczym nie sprzeciwić.

    «Czyż nie piękniejsza nasza poczciwa brzezina,
Która jako wieśniaczka, kiedy płacze syna,
Lub wdowa męża, ręce załamie, roztoczy
Po ramionach do ziemi strumienie warkoczy!
Niema z żalu, postawą jak wymownie szlocha!
Czemuż pan Hrabia, jeśli w malarstwie się kocha,
Nie maluje drzew naszych, pośród których siedzi?
Prawdziwie, będą z pana żartować sąsiedzi,
Że mieszkając na żyznej litewskiej równinie,
Malujesz tylko jakieś skały i pustynie».

    «Przyjacielu — rzekł Hrabia — piękne przyrodzenie
Jest formą, tłem, materią; a duszą — natchnienie,
Które na wyobraźni unosi się skrzydłach,
Poleruje się gustem, wspiera na prawidłach.
Nie dość jest przyrodzenia, nie dosyć zapału:
Sztukmistrz musi ulecieć w sfery ideału!
Nie wszystko, co jest piękne, wymalować da się!
Dowiesz się o tym wszystkim z książek w swoim czasie.
Co się tyczy malarstwa: do obrazu trzeba
Punktów widzenia, grupy, ansamblu i nieba,
Nieba włoskiego! Stąd też w kunszcie pejzażów,
Włochy były, są, będą, ojczyzną malarzów!
Stąd też, oprócz Brejgela (lecz nie van der Helle,
Ale pejzażysty: bo są dwaj Brejgele)
I oprócz Ruisdala, na całej północy
Gdzież był pejzażysta który pierwszej mocy?
Niebios, niebios potrzeba». — «Nasz malarz Orłowski,
Przerwała Telimena — miał gust soplicowski.
(Trzeba wiedzieć, że to jest Sopliców choroba,
Że im oprócz ojczyzny nic się nie podoba).
Orłowski, który życie strawił w Peterburku,
Sławny malarz (mam jego kilka szkiców w biurku)
Mieszkał tuż przy cesarzu, na dworze, jak w raju:
A nie uwierzy Hrabia, jak tęsknił po kraju!
Lubił ciągle wspominać swej młodości czasy,
Wystawiał wszystko w Polszcze: ziemię, niebo, lasy…»

    «I miał rozum! — zawołał Tadeusz z zapałem. —
To państwa niebo włoskie, jak o nim słyszałem,
Błękitne, czyste: wszak to jak zamarzła woda;
Czyż nie piękniejsze stokroć wiatr i niepogoda?
U nas dość głowę podnieść: ileż to widoków!
Ileż scen i obrazów z samej gry obłoków!
Bo każda chmura inna: na przykład jesienna
Pełznie jak żółw leniwa, ulewą brzemienna,
I z nieba aż do ziemi spuszcza długie smugi,
Jak rozwite warkocze, to są deszczu strugi;
Chmura z gradem, jak balon szybko z wiatrem leci,
Krągła, ciemnobłękitna, w środku żółto świeci,
Szum wielki słychać wkoło; nawet te codzienne,
Patrzcie państwo, te białe chmurki, jak odmienne!
Zrazu jak stada dzikich gęsi lub łabędzi,
A z tyłu wiatr jak sokół do kupy je pędzi:
Ściskają się, grubieją, rosną — nowe dziwy!
Dostają krzywych karków, rozpuszczają grzywy,
Wysuwają nóg rzędy i po niebios sklepie
Przelatują jak tabun rumaków po stepie:
Wszystkie białe jak srebro, zmieszały się… nagle
Z ich karków rosną maszty, z grzyw szerokie żagle,
Tabun zmienia się w okręt i wspaniale płynie
Cicho, z wolna po niebios błękitnej równinie!»

    Hrabia i Telimena poglądali w górę;
Tadeusz jedną ręką pokazał im chmurę,
A drugą ścisnął z lekka rączkę Telimeny.
Kilka już upłynęło minut cichej sceny;
Hrabia rozłożył papier na swym kapeluszu
I wydobył ołówek. Wtem przykry dla uszu
Odezwał się dzwon dworski i zaraz śród lasu
Cichego pełno było krzyku i hałasu.

    Hrabia, kiwnąwszy głową, rzekł poważnym tonem:
«Tak to na świecie wszystko los zwykł kończyć dzwonem!…
Rachunki myśli wielkiej, plany wyobraźni,
Zabawki niewinności, uciechy przyjaźni,
Wylania się serc czułych: gdy spiż z dala ryknie,
Wszystko miesza się, zrywa, mąci się i niknie!»
Tu, obróciwszy czuły wzrok ku Telimenie,
«Cóż zostaje?» A ona mu rzekła: «Wspomnienie!»
I chcąc Hrabiego nieco ułagodzić smutek,
Podała mu urwany kwiatek niezabudek.
Hrabia go ucałował i na pierś przyszpilał;
Tadeusz z drugiej strony krzak ziela rozchylał,
Widząc, że się ku niemu tym zielem przewija
Coś białego: była to rączka jak lilija;
Pochwycił ją, całował i usty po cichu
Utonął w niej jak pszczoła w liliji kielichu.
Uczuł na ustach zimno; znalazł klucz i biały
Papier w trąbkę zwiniony; był to listek mały.
Porwał, schował w kieszenie; nie wie, co klucz znaczy,
Lecz mu to owa biała kartka wytłumaczy.

    Dzwon wciąż dzwonił i echem z głębi cichych lasów
Odezwało się tysiąc krzyków i hałasów.
Odgłos to był szukania i nawoływania,
Hasło zakończonego na dziś grzybobrania;
Odgłos nie smutny wcale ani pogrzebowy,
Jak się Hrabiemu zdało: owszem, obiadowy.
Dzwon ten, w każde południe krzyczący z poddasza,
Gości i czeladź domu na obiad zaprasza:
Tak było w dawnych licznych dworach we zwyczaju
I zostało się w domu Sędziego. Więc z gaju
Wychodziła gromada, niosąca krobeczki,
Koszyki uwiązane końcami chusteczki,
Pełne grzybów; a panny w jednym ręku niosły,
Jako wachlarz zwiniony, *borowik* rozrosły,
W drugim związane razem jakby polne kwiatki,
*Opieńki* i rozlicznej barwy *surojadki*.
Wojski miał *muchomora*. Z próżnymi przychodzi
Rękami Telimena; z nią panicze młodzi.

    Goście weszli w porządku i stanęli kołem.
Podkomorzy najwyższe brał miejsce za stołem:
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się starcom, damom i młodzieży;
Obok stał kwestarz; Sędzia tuż przy bernardynie.
Bernardyn zmówił krótki pacierz po łacinie;
Podano w kolej wódkę: za czym wszyscy siedli,
I chołodziec litewski milczkiem żwawo jedli.

    Obiadowano ciszej, niż się zwykle zdarza;
Nikt nie gadał, pomimo wezwań gospodarza.
Strony biorące udział w wielkiej o psów zwadzie,
Myśliły o jutrzejszej walce i zakładzie;
Myśl wielka zwykle usta do milczenia zmusza.
Telimena, mówiąca wciąż do Tadeusza,
Musiała ku Hrabiemu nieraz się odwrócić,
Nawet na Asesora nieraz okiem rzucić:
Tak ptasznik patrzy w sidło, kędy szczygły zwabia,
I razem w pastkę wróblą. Tadeusz i Hrabia,
Obadwa radzi z siebie, obadwa szczęśliwi,
Obaj pełni nadziei, więc niegadatliwi.
Hrabia na kwiatek dumne opuszczał wejrzenie,
A Tadeusz ukradkiem spozierał w kieszenie,
Czy ów kluczyk nie uciekł? Ręką nawet chwytał
I kręcił kartkę, której dotąd nie przeczytał.
Sędzia Podkomorzemu węgrzyna, szampana
Dolewał, służył pilnie, ściskał za kolana,
Ale do rozmawiania z nim nie miał ochoty
I widać, że czuł jakieś tajemne kłopoty.

    Przemijały w milczeniu talerze i dania;
Przerwał nareszcie nudny tok obiadowania
Gość niespodziany, szybko wpadając, gajowy;
Nie zważał nawet, że czas właśnie obiadowy,
Pobiegł do pana; widać z postawy i z miny,
Że ważnej i niezwykłej jest posłem nowiny.
Ku niemu oczy całe zwróciło zebranie.
On, odetchnąwszy nieco, rzekł: «Niedźwiedź, mospanie!»
Resztę wszyscy odgadli: że źwierz z *matecznika*
Wyszedł, że w zaniemeńską puszczę się przemyka,
Że go trzeba wnet ścigać, wszyscy wraz uznali,
Choć ani się radzili, ani namyślali;
Spólną myśl widać było z uciętych wyrazów,
Z gestów żywych, z wydanych rozlicznych rozkazów,
Które, wychodząc tłumnie, razem z ust tak wielu,
Dążyły przecież wszystkie do jednego celu.

    «Na wieś! — zawołał Sędzia — hej! konno, setnika!
Jutro na brzask obława, lecz na ochotnika;
Kto wystąpi z oszczepem, temu z robocizny
Wytrącić dwa szarwarki i pięć dni pańszczyzny».

    «W skok — krzyknął Podkomorzy — okulbaczyć siwą,
Dobiec w cwał do mojego dworu; wziąć co żywo
Dwie pjawki, które w całej okolicy słyną,
Pies zowie się Sprawnikiem, a suka Strapczyną;
Zakneblować im pyski, zawiązać je w miechu,
I przystawić je tutaj konno dla pośpiechu».
«Wańka! — krzyknął na chłopca Asesor po rusku —
Tasak mój sanguszkowski pociągnąć na brusku:
Wiesz, tasak co od księcia miałem w podarunku;
Pas opatrzyć, czy kula jest w każdym ładunku».
«Strzelby — krzyknęli wszyscy — mieć na pogotowiu!»
Asesor wołał ciągle: «Ołowiu, ołowiu!
Formę do kul mam w torbie». — «Do księdza plebana
Dać znać — dodał pan Sędzia — żeby jutro z rana
Mszę miał w kaplicy leśnej: króciuchna oferta
Za myśliwych, msza zwykła świętego Huberta».

    Po wydanych rozkazach nastało milczenie;
Każdy dumał i rzucał dokoła wejrzenie,
Jak gdyby kogoś szukał; z wolna wszystkich oczy
Sędziwa twarz Wojskiego ciągnie i jednoczy:
Znak to był, że szukają na przyszłą wyprawę
Wodza i że Wojskiemu oddają buławę.
Wojski powstał, zrozumiał towarzyszów wolę,
I uderzywszy ręką poważnie po stole,
Pociągnął złocistego z zanadrza łańcuszka,
Na którym wisiał gruby zegarek jak gruszka:
«Jutro — rzekł — pół do piątej, przy leśnej kaplicy
Stawią się bracia strzelcy, wiara obławnicy».

    Rzekł i ruszył od stołu, za nim szedł gajowy;
Oni obmyślić mają i urządzić łowy.

    Tak wodze, gdy na jutro bitwę zapowiedzą,
Żołnierze po obozie broń czyszczą i jedzą,
Lub na płaszczach i siodłach śpią próżni kłopotu,
A wodze śród cichego dumają namiotu.

    Przerwał się obiad, dzień zszedł na kowaniu koni,
Karmieniu psów, zbieraniu i czyszczeniu broni;
U wieczerzy, zaledwo kto przysiadł do stoła;
Nawet strona Kusego z partyją Sokoła,
Przestała dawnym wielkim zatrudniać się sporem:
Pobrawszy się pod ręce, Rejent z Asesorem
Wyszukują ołowiu. Reszta spracowana
Szła spać wcześnie, ażeby przebudzić się z rana.




Księga czwarta



Dyplomatyka i łowy

Zjawisko w papilotach budzi Tadeusza — Za późne postrzeżenie omyłki — Karczma — Emisariusz — Zręczne użycie tabakiery zwraca dyskusję na właściwą drogę — Matecznik — Niedźwiedź — Niebezpieczeństwo Tadeusza i Hrabiego — Trzy strzały — Spór Sagalasówki z Sanguszkówką rozstrzygniony na stronę jednorurki horeszkowskiej — Bigos — Wojskiego powieść o pojedynku Doweyki z Domeyką przerwana szczuciem kota — Koniec powieści o Doweyce i Domeyce.

    Rówienniki litewskich wielkich kniaziów, drzewa
Białowieży, Świtezi, Ponar, Kuszelewa!
Których cień spadał niegdyś na koronne głowy
Groźnego Witenesa, wielkiego Mindowy,
I Giedymina, kiedy na Ponarskiej Górze,
Przy ognisku myśliwskim, na niedźwiedziej skórze
Leżał, słuchając pieśni mądrego Lizdejki,
A Wilii widokiem i szumem Wilejki
Ukołysany, marzył o wilku żelaznym,
i zbudzony, za bogów rozkazem wyraźnym
Zbudował miasto Wilno, które w lasach siedzi
Jak wilk pośrodku żubrów, dzików i niedźwiedzi.
Z tego to miasta Wilna, jak z rzymskiej wilczycy,
Wyszedł Kiejstut i Olgierd, i Olgierdowicy,
Równie myśliwi wielcy jak sławni rycerze,
Czyli wroga ścigali, czyli dzikie źwierzę.
Sen myśliwski nam odkrył tajnie przyszłych czasów:
Że Litwie trzeba zawsze żelaza i lasów.

    Knieje! do was ostatni przyjeżdżał na łowy
Ostatni król, co nosił kołpak Witoldowy,
Ostatni z Jagiellonów wojownik szczęśliwy,
I ostatni na Litwie monarcha myśliwy.
Drzewa moje ojczyste! jeśli Niebo zdarzy,
Bym wrócił was oglądać, przyjaciele starzy,
Czyli was znajdę jeszcze? czy dotąd żyjecie?
Wy, koło których niegdyś pełzałem jak dziecię;
Czy żyje wielki Baublis, w którego ogromie
Wiekami wydrążonym, jakby w dobrym domie,
Dwunastu ludzi mogło wieczerzać za stołem?
Czy kwitnie gaj Mendoga pod farnym kościołem?
I tam na Ukrainie czy się dotąd wznosi
Przed Hołowińskch domem, nad brzegami Rosi,
Lipa tak rozrośniona, że pod jej cieniami
Sto młodzieńców, sto panien szło w taniec parami?

    Pomniki nasze! ileż co rok was pożera
Kupiecka lub rządowa, moskiewska siekiera!
Nie zostawia przytułku ni leśnym śpiewakom,
Ni wieszczom, którym cień wasz tak miły jak ptakom.
Wszak lipa czarnoleska, na głos Jana czuła,
Tyle rymów natchnęła! Wszak ów dąb gaduła
Kozackiemu wieszczowi tyle cudów śpiewa!

    Ja ileż wam winienem, o domowe drzewa!
Błahy strzelec, uchodząc szyderstw towarzyszy
Za chybioną źwierzynę, ileż w waszej ciszy
Upolowałem dumań, gdy w dzikim ostępie,
Zapomniawszy o łowach, usiadłem na kępie,
A koło mnie srebrzył się tu mech siwobrody,
Zlany granatem czarnej, zgniecionej jagody,
A tam się czerwieniły wrzosiste pagórki,
Strojne w brusznice jakby w koralów paciórki.
Wokoło była ciemność; gałęzie u góry
Wisiały jak zielone, gęste, niskie chmury;
Wicher kędyś nad sklepem szalał nieruchomym,
Jękiem, szumami, wyciem, łoskotami, gromem:
Dziwny, odurzający hałas! Mnie się zdało,
Że tam nad głową morze wiszące szalało.

    Na dole jak ruiny miast: tu wywrót dębu
Wysterka z ziemi na kształt ogromnego zrębu;
Na nim oparte, jak ścian i kolumn obłamy,
Tam gałęziste kłody, tu wpół zgniłe tramy
Ogrodzone parkanem traw. W środek tarasu
Zajrzeć straszno, tam siedzą gospodarze lasu,
Dziki, niedźwiedzie, wilki; u wrót leżą kości
Na pół zgryzione jakichś nieostrożnych gości.
Czasem wymkną się w górę przez trawy zielenie,
Jakby dwa wodotryski, dwa rogi jelenie,
I mignie między drzewa źwierz żółtawym pasem,
Jak promień, kiedy wpadłszy gaśnie między lasem.

    I znowu cichość w dole. Dzięcioł na jedlinie
Stuka z lekka i dalej odlatuje, ginie,
Schował się, ale dziobem nie przestaje pukać,
Jak dziecko, gdy schowane woła, by go szukać.
Bliżej siedzi wiewiórka, orzech w łapkach trzyma,
Gryzie go; zawiesiła kitkę nad oczyma,
Jak pióro nad szyszakiem u kirasyjera:
Chociaż tak osłoniona, dokoła spoziera,
Dostrzegłszy gościa, skacze gajów tanecznica
Z drzew na drzewa, miga się jako błyskawica;
Na koniec w niewidzialny otwór pnia przepada,
Jak wracająca w drzewo rodzime dryjada.
Znowu cicho.

                        Wtem, gałąź wstrząsła się trącona,
I pomiędzy jarzębin rozsunione grona
Kraśniejsze od jarzębin zajaśniały lica:
To jagód lub orzechów zbieraczka, dziewica.
W krobeczce z prostej kory podaje zebrane
Bruśnice świeże jako jej usta rumiane.
Obok młodzieniec idzie, leszczynę nagina:
Chwyta w lot migające orzechy dziewczyna.

    Wtem, usłyszeli odgłos rogów i psów granie:
Zgadują, że się ku nim zbliża polowanie,
I pomiędzy gałęzi gęstwę, pełni trwogi,
Zniknęli nagle z oczu jako leśne bogi.

    W Soplicowie ruch wielki. Lecz ni psów hałasy,
Ani rżące rumaki, skrzypiące kolasy,
Ni odgłos trąb dających hasło polowania
Nie mogły Tadeusza wyciągnąć z posłania;
Ubrany padłszy w łóżko, spał jak bobak w norze.
Nikt z młodzieży nie myślał szukać go po dworze;
Każdy sobą zajęty śpieszył, gdzie kazano;
O towarzyszu sennym całkiem zapomniano.

    On chrapał. Słońce w otwór, co śród okienicy
Wyrżnięty był w kształt serca, wpadło do ciemnicy
Słupem ognistym, prosto sennemu na czoło.
On jeszcze chciał zadrzemać i kręcił się wkoło,
Chroniąc się blasku. Nagle usłyszał stuknienie,
Przebudził się: wesołe było przebudzenie.
Czuł się rzeźwym jak ptaszek, z lekkością oddychał,
Czuł się szczęśliwym, sam się do siebie uśmiechał:
Myśląc o wszystkim, co mu wczora się zdarzyło,
Rumienił się i wzdychał, i serce mu biło.
Spojrzał w okno, o dziwy! W promieni przezroczu,
W owym sercu, błyszczało dwoje jasnych oczu,
Szeroko otworzonych, jak zwykle wejrzenie,
Kiedy z jasności dziennej przedziera się w cienie.
Ujrzał i małą rączkę, niby wachlarz z boku
Nadstawioną ku słońcu dla ochrony wzroku;
Palce drobne, zwrócone na światło różowe,
Czerwieniły się na wskroś jakby rubinowe.
Usta widział ciekawe, roztulone nieco,
I ząbki, co jak perły śród koralów świecą,
I lica, choć od słońca zasłaniane dłonią
Różową, same całe jak róże się płonią.

    Tadeusz spał pod oknem; sam ukryty w cieniu,
Leżąc na wznak, cudnemu dziwił się zjawieniu
I miał je tuż nad sobą, ledwie nie na twarzy:
Nie wiedział, czy to jawa, czyli mu się marzy
Jedna z tych miłych, jasnych twarzyczek dziecinnych,
Które pomnim widziane we śnie lat niewinnych.
Twarzyczka schyliła się — ujrzał, drżąc z bojaźni
I radości, niestety! ujrzał najwyraźniej,
Przypomniał, poznał włos ów krótki, jasnozłoty,
W drobne, jako śnieg białe, zwity papiloty,
Niby srebrzyste strączki, co od słońca blasku
Świeciły jak korona na świętych obrazku.

    Zerwał się i widzenie zaraz uleciało
Przestraszone łoskotem; czekał, nie wracało!
Tylko usłyszał znowu trzykrotne stukanie
I słowa: «Niech pan wstaje, czas na polowanie.
Pan zaspał». Skoczył z łóżka i obu rękami
Pchnął okienicę, że aż trzasła zawiasami
I rozwarłszy się w obie uderzyła ściany;
Wyskoczył, patrzył wkoło zdumiony, zmieszany,
Nic nie widział, nie dostrzegł niczyjego śladu.
Niedaleko od okna był parkan od sadu,
Na nim chmielowe liście i kwieciste wieńce
Chwiały się; czy je lekkie potrąciły ręce?
Czy wiatr ruszył? Tadeusz długo patrzył na nie,
Nie śmiał iść w ogród; tylko wsparł się na parkanie,
Oczy podniósł i z palcem do ust przyciśnionym
Kazał sam sobie milczeć, by słowem kwapionem
Nie rozerwał milczenia; potem w czoło stukał,
Niby do wspomnień dawnych uśpionych w nim pukał,
Na koniec, gryząc palce, do krwi się zadrasnął
I na cały głos: «Dobrze, dobrze mi tak!» wrzasnął.

    We dworze, gdzie przed chwilą tyle było krzyku,
Teraz pusto i głucho jak na mogilniku:
Wszyscy ruszyli w pole. Tadeusz nadstawił
Uszu i ręce do nich jak trąbki przyprawił;
Słuchał, aż mu wiatr przyniósł, wiejący od puszczy,
Odgłosy trąb i wrzaski polującej tłuszczy.

    Koń Tadeusza czekał w stajni osiodłany.
Wziął więc flintę, skoczył nań i jak opętany
Pędził ku karczmom, które stały przy kaplicy,
Kędy mieli się rankiem zebrać obławnicy.

    Dwie chyliły się karczmy po dwóch stronach drogi,
Oknami wzajem sobie grożące jak wrogi.
Stara należy z prawa do zamku dziedzica;
Nową, na złość zamkowi, postawił Soplica.
W tamtej, jak w swym dziedzictwie, rej wodził Gerwazy,
W tej najwyższe za stołem brał miejsce Protazy.

    Nowa karczma nie była ciekawa z pozoru.
Stara wedle dawnego zbudowana wzoru,
Który był wymyślony od tyryjskich cieśli,
A potem go Żydowie po świecie roznieśli:
Rodzaj architektury obcym budowniczym
Wcale nieznany; my go od Żydów dziedziczym.

    Karczma z przodu jak korab, z tyłu jak świątynia:
Korab, istna Noego czworogranna skrzynia,
Znany dziś pod prostackim nazwiskiem stodoły;
Tam różne są zwierzęta, konie, krowy, woły,
Kozy brodate; w górze zaś ptactwa gromady,
I płazów choć po parze, są też i owady.
Część tylna, na kształt dziwnej świątyni stawiona,
Przypomina z pozoru ów gmach Salomona,
Który pierwsi ćwiczeni w budowań rzemieśle
Hiramscy na Syjonie wystawili cieśle.
Żydzi go naśladują dotąd we swych szkołach,
A szkół rysunek widny w karczmach i stodołach.
Dach z dranic i ze słomy, spiczasty, zadarty,
Pogięty jako kołpak żydowski podarty.
Ze szczytu wytryskują krużganku krawędzie,
Oparte na drewnianym licznych kolumn rzędzie.
Kolumny, co jest wielkie architektów dziwo,
Trwałe, chociaż wpół zgniłe i stawione krzywo,
Jako w wieży pizańskiej, nie podług modelów
Greckich, bo są bez podstaw i bez kapitelów.
Nad kolumnami biegą wpółokrągłe łuki,
Także z drzewa, gotyckiej naśladowstwo sztuki.
Z wierzchu ozdoby sztuczne, nie rylcem, nie dłutem,
Ale zręcznie ciesielskim wyrzezane sklutem,
Krzywe jak szabasowych ramiona świeczników;
Na końcu wiszą gałki, coś na kształt guzików,
Które Żydzi modląc się na łbach zawieszają
I które po swojemu cyces nazywają.
Słowem, z daleka karczma chwiejąca się, krzywa,
Podobna jest do Żyda, gdy się modląc kiwa:
Dach jak czapka, jak broda strzecha roztrzęsiona,
Ściany dymne i brudne jak czarna opona,
A z przodu rzeźba sterczy jak cyces na czole.

    W środku karczmy jest podział jak w żydowskiej szkole:
Jedna część, pełna izbic ciasnych i podłużnych,
Służy dla dam wyłącznie i panów podróżnych;
W drugiej ogromna sala: koło każdej ściany
Ciągnie się wielonożny stół wąski, drewniany;
Przy nim stołki, choć niższe, podobne do stoła,
Jako dzieci do ojca.

                        Na stołkach dokoła
Siedziały chłopy, chłopki tudzież szlachta drobna,
Wszyscy rzędem; ekonom sam siedział z osobna.
Po rannej mszy z kaplicy, że była niedziela,
Zabawić się i wypić przyszli do Jankiela.
Przy każdym już szumiała siwą wódką czarka,
Ponad wszystkimi z butlą biegała szynkarka.
W środku arendarz Jankiel, w długim aż do ziemi
Szarafanie, zapiętym haftkami srebrnemi,
Rękę jedną za czarny pas jedwabny wsadził,
Drugą poważnie sobie siwą brodę gładził;
Rzucając wkoło okiem rozkazy wydawał,
Witał wchodzących gości, przy siedzących stawał
Zagajając rozmowę, kłótliwych zagadzał,
Lecz nie służył nikomu: tylko się przechadzał.
Żyd stary i powszechnie znany z poczciwości,
Od lat wielu dzierżawił karczmę, a nikt z włości,
Nikt ze szlachty nie zaniósł nań skargi do dworu.
O cóż skarżyć? Miał trunki dobre do wyboru,
Rachował się ostrożnie, lecz bez oszukaństwa,
Ochoty nie zabraniał, nie cierpiał pijaństwa,
Zabaw wielki miłośnik: u niego wesele
I chrzciny obchodzono, on w każdą niedzielę
Kazał do siebie ze wsi przychodzić muzyce,
Przy której i basetla była, i kozice.

    Muzykę znał, sam słynął muzycznym talentem;
Z cymbałami, narodu swego instrumentem,
Chadzał niegdyś po dworach i graniem zdumiewał,
I pieśniami, bo biegle i uczenie śpiewał.
Chociaż Żyd, dosyć czystą miał polską wymowę,
Szczególniej zaś polubił pieśni narodowe;
Przywoził mnóstwo z każdej za Niemen wyprawy,
Kołomyjek z Halicza, mazurów z Warszawy;
Wieść, nie wiem czyli pewna, w całej okolicy
Głosiła, że on pierwszy przywiózł z zagranicy
I upowszechnił wówczas, w tamecznym powiecie,
Ową piosenkę, sławną dziś na całym świecie,
A którą po raz pierwszy na ziemi Auzonów
Wygrały Włochom polskie trąby legijonów.
Talent śpiewania bardzo na Litwie popłaca,
Jedna miłość u ludzi, wsławia i wzbogaca:
Jankiel zrobił majątek; syt zysków i chwały,
Zawiesił dźwięcznostrunne na ścianie cymbały;
Osiadłszy z dziećmi w karczmie, zatrudniał się szynkiem,
Przy tym w pobliskim mieście był też podrabinkiem,
A zawsze miłym wszędzie gościem i domowym
Doradcą; znał się dobrze na handlu zbożowym,
Na wicinnym: potrzebna jest znajomość taka
Na wsi. Miał także sławę dobrego Polaka.

    On pierwszy zgodził kłótnie, często nawet krwawe,
Między dwiema karczmami: obie wziął w dzierżawę;
Szanowali go równie i starzy stronnicy
Horeszkowscy, i słudzy Sędziego Soplicy.
On sam powagę umiał utrzymać nad groźnym
Klucznikiem horeszkowskim i kłótliwym Woźnym;
Przed Jankielem tłumili dawne swe urazy
Gerwazy, groźny ręką, językiem Protazy.

    Gerwazego nie było; ruszył na obławę,
Nie chcąc, aby tak ważną i trudną wyprawę
Odbył sam Hrabia, młody i niedoświadczony;
Poszedł więc z nim dla rady tudzież dla obrony.

    Dziś miejsce Gerwazego, najdalsze od progu,
Między dwiema ławami, w samym karczmy rogu,
Zwane *pokuciem*, kwestarz ksiądz Robak zajmował.
Jankiel go tam posadził. Widać, że szanował
Wysoko bernardyna: bo skoro dostrzegał
Ubytek w jego szklance, natychmiast podbiegał
I rozkazał dolewać lipcowego miodu.
Słychać, że z bernardynem znali się za młodu,
Kędyś tam w cudzych krajach. Robak często chadzał
Nocą do karczmy, tajnie z Żydem się naradzał
O ważnych rzeczach; słychać było, że towary
Ksiądz przemycał — lecz potwarz ta niegodna wiary.

    Robak, wsparty na stole, wpół głośno rozprawiał,
Tłum szlachty go otaczał i uszy nadstawiał,
I nosy ku księdzowskiej chylił tabakierze;
Brano z niej, i kichała szlachta jak moździerze.

    «Reverendissime — rzekł kichnąwszy Skołuba —
To mi tabaka, co to idzie aż do czuba!
Od czasu jak nos dźwigam (tu głasnął nos długi)
Takiej nie zażywałem (tu kichnął raz drugi);
Prawdziwa bernardynka, pewnie z Kowna rodem,
Miasta sławnego w świecie tabaką i miodem.
Byłem tam lat już…» — Robak przerwał mu: «Na zdrowie
Wszystkim waszmościom, moi mościwi panowie!
Co się tabaki tyczy, hem, ona pochodzi
Z dalszej strony, niż myśli Skołuba dobrodziéj:
Pochodzi z Jasnej Góry. Księża paulinowie
Tabakę taką robią w mieście Częstochowie,
Kędy jest obraz tylu cudami wsławiony,
Bogarodzicy Panny, Królowej Korony
Polskiej… zowią ją dotąd i Księżną Litewską —
Koronęć jeszcze dotąd piastuje królewską…
Lecz na Litewskim Księstwie teraz syzma siedzi!»
«Z Częstochowy? — rzekł Wilbik. — Byłem tam w spowiedzi,
Kiedym na odpust chodził lat temu trzydzieście.
Czy to prawda, że Francuz gości teraz w mieście,
Że chce kościół rozwalać i skarbiec zabierze:
Bo to wszystko w Litewskim stoi Kuryjerze?»
«Nieprawda — rzekł bernardyn — nie! Pan Najjaśniejszy,
Napoleon, katolik jest najprzykładniejszy:
Wszak go papież namaścił, żyją z sobą w zgodzie
I nawracają ludzi w francuskim narodzie,
Który się trochę popsuł. Prawda, z Częstochowy
Oddano wiele srebra na skarb narodowy
Dla ojczyzny, dla Polski; sam Pan Bóg tak każe:
Skarbcem ojczyzny zawsze są Jego ołtarze.
Wszakże w Warszawskim Księstwie mamy sto tysięcy
Wojska polskiego, może wkrótce będzie więcéj:
A któż wojsko opłaci? czy nie wy, Litwini?
Wy tylko grosz dajecie do moskiewskiej skrzyni».
«Kat by dał — krzyknął Wilbik — gwałtem od nas biorą».
«Oj, dobrodzieju — chłopek ozwał się z pokorą,
Pokłoniwszy się księdzu i skrobiąc się w głowę —
Już to szlachcie, to jeszcze bieda przez połowę;
Lecz nas drą jak na łyka…» «Cham! — Skołuba krzyknął —
Głupi, tobieć to lepiej, tyś chłopie przywyknął,
Jak węgorz do odarcia: lecz nam *urodzonym*,
Nam wielmożnym, do złotych swobód wzwyczajonym!
Ach, bracia! wszak to dawniej szlachcic na zagrodzie…
(«Tak, tak — krzyknęli wszyscy — równy wojewodzie!»)
Dziś nam szlachectwa przeczą, każą nam drabować
Papiery, i szlachectwa papierem próbować».
«Jeszcze Waszeci mniejsza — zawołał Juraha —
Waszeć z pradziadów chłopów uszlachcony szlacha;
Ale ja, z kniaziów! Pytać u mnie o patenta,
Kiedym został szlachcicem? Sam Bóg to pamięta!
Niechaj Moskal w las idzie pytać się dębiny,
Kto jej dał patent rosnąć nad wszystkie krzewiny».
«Kniaziu — rzekł Żagiel — świeć waść baki lada komu,
Tu znajdziesz pono mitry i w niejednym domu».
«Waść ma krzyż w herbie — wołał Podhajski — to skryta
Aluzyja, że w rodzie bywał neofita».
«Fałsz — przerwał Birbasz — Przecież ja z tatarskich hrabiów
Pochodzę, a mam krzyże nad herbem Korabiów».
«Poraj — krzyknął Mickiewicz — z mitrą w polu złotym,
Herb książęcy, Stryjkowski gęsto pisze o tym».

    Za czym wielkie powstały w całej karczmie szmery.
Ksiądz bernardyn uciekł się do swej tabakiery;
W kolej częstował mówców. Gwar zaraz ucichnął;
Każdy zażył przez grzeczność i kilkakroć kichnął.
Bernardyn, korzystając z przerwy, mówił daléj:
«Oj, wielcy ludzie od tej tabaki kichali!
Czy uwierzycie państwo, że z tej tabakiery,
Pan jenerał Dąbrowski zażył razy cztery?»
«Dąbrowski?» — zawołali. «Tak, tak, on, jenerał.
Byłem w obozie, gdy on Gdańsk Niemcom odbierał;
Miał coś pisać; bojąc się, ażeby nie zasnął,
Zażył, kichnął, dwakroć mię po ramieniu klasnął:
»Księże Robaku — mówił — księże bernardynie,
Obaczymy się w Litwie może nim rok minie;
Powiedz Litwinom, niech mnie czekają z tabaką
Częstochowską, nie biorę innej tylko taką».

    Mowa księdza wzbudziła takie zadziwienie,
Taką radość, że całe huczne zgromadzenie
Milczało chwilę; potem na pół ciche słowa
Powtarzano: «Tabaka z Polski? Częstochowa?
Dąbrowski? Z ziemi włoskiej?…» Aż na koniec razem,
Jakby myśl z myślą, wyraz sam zbiegł się z wyrazem,
Wszyscy jednogłośnie, jak na dane hasło,
Krzyknęli: «Dąbrowskiego!» Wszystko razem wrzasło,
Wszystko się uścisnęło: chłop z tatarskim hrabią,
Mitra z Krzyżem, Poraje z Gryfem i z Korabią;
Zapomnieli wszystkiego, nawet bernardyna,
Tylko śpiewali krzycząc: «Wódki, miodu, wina!»

    Długo się przysłuchiwał ksiądz Robak piosence,
Na koniec chciał ją przerwać; wziął w obydwie ręce
Tabakierkę, kichaniem melodyję zmieszał,
I nim się nastroili, tak mówić pośpieszał:
«Chwalicie mą tabakę, mości dobrodzieje;
Obaczcież, co się wewnątrz tabakierki dzieje».
Tu, wycierając chustką zabrudzone denko,
Pokazał malowaną armiję maleńką
Jak rój much; w środku jeden człowiek na rumaku,
Wielki jako chrząszcz, siedział, pewnie wódz orszaku;
Spinał konia, jak gdyby chciał skakać w niebiosa,
Jedną rękę na cuglach, drugą miał u nosa:
«Przypatrzcie się — rzekł Robak — tej groźnej postawie:
Zgadnijcie czyja? — Wszyscy patrzyli ciekawie.—
Wielki to człowiek, cesarz, ale nie Moskali,
Ich carowie tabaki nigdy nie bierali…»
«Wielki człowiek — zawołał Cydzik — a w kapocie?
Ja myśliłem, że wielcy ludzie chodzą w złocie:
Bo u Moskalów lada jenerał, mospanie,
To tak świeci się w złocie jak szczupak w szafranie».
«Ba — przerwał Rymsza — przecież widziałem za młodu
Kościuszkę, naczelnika naszego narodu:
Wielki człowiek! A chodził w krakowskiej sukmanie,
To jest czamarce». «W jakiej czamarce, mospanie? —
Odparł Wilbik. — To przecież zwano taratatką».
«Ale tamta z frędzlami, ta jest całkiem gładką» —
Krzyknął Mickiewicz. Zatem wszczynały się swary
O różnych taratatki kształtach i czamary.

    Przemyślny Robak, widząc, że się tak rozpryska
Rozmowa, jął ją znowu zbierać do ogniska,
Do swojej tabakiery; częstował, kichali,
Życzyli sobie zdrowia, on rzecz ciągnął daléj:
«Gdy cesarz Napoleon w potyczce zażywa
Raz po raz, to znak pewny, że bitwę wygrywa.
Na przykład pod Austerlitz: Francuzi tak stali
Z armatami, a na nich biegła ćma Moskali.
Cesarz patrzył i milczał. Co Francuzi strzelą,
To Moskale pułkami jak trawa się ścielą:
Pułk za pułkiem cwałował i spadał z kulbaki;
Co pułk spadnie, to cesarz zażyje tabaki.
Aż w końcu, Aleksander ze swoim braciszkiem
Konstantym i z niemieckim cesarzem Franciszkiem,
W nogi z pola; więc cesarz, widząc, że po walce,
Spojrzał na nich, zaśmiał się i otrząsnął palce.
Otóż, jeśli kto z panów, coście tu przytomni,
Będzie w wojsku cesarza, niech to sobie wspomni».

    «Ach — zawołał Skołuba — mój księże kwestarzu!
Kiedyż to będzie! Wszak to ile w kalendarzu
Jest świąt, na każde święto Francuzów nam wróżą:
Wygląda człek, wygląda, aż się oczy mrużą;
A Moskal jak nas trzymał, tak trzyma za szyję.
Pono nim słońce wnidzie, rosa oczy wyje».

    «Mospanie — rzekł bernardyn — babska rzecz narzekać,
A żydowska rzecz ręce założywszy czekać,
Nim kto w karczmę zajedzie i do drzwi zapuka.
Z Napoleonem pobić Moskalów nie sztuka.
Jużci on Szwabom skórę trzy razy wymłócił,
Brzydkie Prusactwo zdeptał, Anglików wyrzucił
Het za morze, Moskalom zapewne wygodzi;
Ale co stąd wyniknie, wie asan dobrodziéj?
Oto, szlachta litewska wtenczas na koń wsiędzie
I szable weźmie, kiedy bić się z kim nie będzie;
Napoleon sam wszystkich pobiwszy, nareszcie
Powie: »Obejdę się ja bez was, kto jesteście?«
Więc nie dość gościa czekać, nie dość i zaprosić,
Trzeba czeladkę zebrać i stoły pownosić,
A przed ucztą potrzeba dom oczyścić z śmieci,
Oczyścić dom, powtarzam, oczyścić dom, dzieci!»

    Nastąpiło milczenie, potem głosy w tłumie:
«Jakże to dom oczyścić, jak to ksiądz rozumie?
Jużci my wszystko zrobim, na wszystko gotowi;
Tylko niech ksiądz dobrodziej jaśniej się wysłowi».

    Ksiądz poglądał za okno, przerwawszy rozmowę;
Ujrzał coś ciekawego, z okna wytknął głowę,
Po chwili rzekł powstając: «Dziś czasu nie mamy;
Potem o tym obszerniej z sobą pogadamy.
Jutro będę dla sprawy w powiatowym mieście;
I do waszmościów z drogi zajadę po kweście».

    «Niech też do Niehrymowa ksiądz na nocleg zdąży —
Rzekł ekonom — rad będzie księdzu pan chorąży;
Wszakże na Litwie stare powiada przysłowie:
Szczęśliwy człowiek, jako kwestarz w Niehrymowie!»
«I do nas — rzekł Zubkowski — wstąp jeżeli łaska;
Znajdzie się tam półsztuczek płótna, masła faska,
Baran lub krówka; wspomnij księże na te słowa:
Szczęśliwy człowiek, trafił jak ksiądz do Zubkowa».
«I do nas» — rzekł Skołuba. «Do nas — Terajewicz —
Żaden bernardyn głodny nie wyszedł z Pucewicz».
Tak cała szlachta prośbą i obietnicami
Przeprowadzała księdza; on już był za drzwiami.

    On już pierwej przez okno ujrzał Tadeusza,
Który leciał gościńcem, w cwał, bez kapelusza,
Z głową schyloną, bladym, posępnym obliczem,
A konia ustawicznie bódł i kropił biczem.
Ten widok bardzo księdza bernardyna zmieszał,
Więc za młodzieńcem kroki szybkimi pośpieszał
Do wielkiej puszczy, która, jako oko sięga,
Czerniła się na całym brzegu widnokręga.

    Któż zbadał puszcz litewskich przepastne krainy,
Aż do samego środka, do jądra gęstwiny?
Rybak ledwie u brzegów nawiedza dno morza;
Myśliwiec krąży koło puszcz litewskich łoża,
Zna je ledwie po wierzchu, ich postać, ich lice:
Lecz obce mu ich wnętrzne serca tajemnice;
Wieść tylko albo bajka wie, co się w nich dzieje.
Bo gdybyś przeszedł bory i podszyte knieje,
Trafisz w głębi na wielki wał pniów, kłód, korzeni,
Obronny trzęsawicą, tysiącem strumieni
I siecią zielsk zarosłych, i kopcami mrowisk,
Gniazdami os, szerszeniów, kłębami wężowisk.
Gdybyś i te zapory zmógł nadludzkim męstwem,
Dalej spotkać się z większym masz niebezpieczeństwem:
Dalej co krok czyhają, niby wilcze doły,
Małe jeziorka, trawą zarosłe na poły,
Tak głębokie, że ludzie dna ich nie dośledzą
(Wielkie jest podobieństwo, że diabły tam siedzą).
Woda tych studni sklni się, plamista rdzą krwawą,
A z wnętrza ciągle dymi, zionąc woń plugawą,
Od której drzewa wkoło tracą liść i korę;
Łyse, skarłowaciałe, robaczliwe, chore,
Pochyliwszy konary mchem kołtunowate
I pnie garbiąc, brzydkimi grzybami brodate,
Siedzą wokoło wody jak czarownic kupa
Grzejąca się nad kotłem, w którym warzą trupa.

    Za tymi jeziorkami już nie tylko krokiem,
Ale daremnie nawet zapuszczać się okiem,
Bo tam już wszystko mglistym zakryte obłokiem,
Co się wiecznie ze trzęskich oparzelisk wznosi.
A za tą mgłą na koniec (jak wieść gminna głosi)
Ciągnie się bardzo piękna, żyzna okolica,
Główna królestwa zwierząt i roślin stolica.
W niej są złożone wszystkich drzew i ziół nasiona,
Z których się rozrastają na świat ich plemiona;
W niej, jak w arce Noego, z wszelkich zwierząt rodu
Jedna przynajmniej para chowa się dla płodu.
W samym środku (jak słychać) mają swoje dwory
Dawny Tur, Żubr i Niedźwiedź, puszcz imperatory;
Około nich na drzewach gnieździ się Ryś bystry
I żarłoczny Rosomak jak czujne ministry;
Dalej zaś, jak podwładni szlachetni wasale,
Mieszkają Dziki, Wilki i Łosie rogale.
Nad głowami Sokoły i Orłowie dzicy,
Żyjący z pańskich stołów dworscy zausznicy.
Te pary zwierząt główne i patryjarchalne,
Ukryte w jądrze puszczy, światu niewidzialne,
Dzieci swe ślą dla osad za granicę lasu,
A sami we stolicy używają wczasu;
Nie giną nigdy bronią sieczną ani palną,
Lecz starzy umierają śmiercią naturalną.
Mają też i swój cmentarz, kędy bliscy śmierci,
Ptaki składają pióra, czworonogi sierci:
Niedźwiedź, gdy zjadłszy zęby, strawy nie przeżuwa,
Jeleń zgrzybiały, gdy już ledwie nogi suwa,
Zając sędziwy, gdy mu już krew w żyłach krzepnie,
Kruk, gdy już posiwieje, sokół, gdy oślepnie,
Orzeł, gdy mu dziób stary tak się w kabłąk skrzywi,
Że zamknięty na wieki już gardła nie żywi,
Idą na cmentarz. Nawet mniejszy zwierz, raniony
Lub chory, bieży umrzeć w swe ojczyste strony.
Stąd to w miejscach dostępnych, kędy człowiek gości,
Nie znajdują się nigdy martwych zwierząt kości.
Słychać, że tam w stolicy między zwierzętami
Dobre są obyczaje, bo rządzą się sami;
Jeszcze cywilizacją ludzką nie popsuci,
Nie znają praw własności, która świat nasz kłóci,
Nie znają pojedynków ni wojennej sztuki.
Jak ojce żyły w raju, tak dziś żyją wnuki,
Dzikie i swojskie razem, w miłości i zgodzie,
Nigdy jeden drugiego nie kąsa ni bodzie.
Nawet gdyby tam człowiek wpadł, chociaż niezbrojny,
Toby środkiem bestyi przechodził spokojny;
One by nań patrzyły tym wzrokiem zdziwienia,
Jakim w owym ostatnim szóstym dniu stworzenia
Ojce ich pierwsze, co się w ogrójcu gnieździły,
Patrzyły na Adama, nim się z nim skłóciły.
Szczęściem, człowiek nie zbłądzi do tego ostępu,
Bo Trud, i Trwoga, i Śmierć bronią mu przystępu.

    Czasem tylko w pogoni zaciekłe ogary,
Wpadłszy niebacznie między bagna, mchy i jary,
Wnętrznej ich okropności rażone widokiem,
Uciekają skowycząc z obłąkanym wzrokiem;
I długo potem ręką pana już głaskane,
Drżą jeszcze u nóg jego strachem opętane.
Te puszcz stołeczne, ludziom nieznane tajniki,
W języku swoim strzelcy zowią: *mateczniki*.

    Głupi niedźwiedziu! gdybyś w mateczniku siedział,
Nigdy by się o tobie Wojski nie dowiedział;
Ale czyli pasieki zwabiła cię wonność,
Czy uczułeś do owsa dojrzałego skłonność,
Wyszedłeś na brzeg puszczy, gdzie się las przerzedził,
I tam zaraz leśniczy bytność twą wyśledził,
I zaraz obsaczniki, chytre nasłał szpiegi,
By poznać, gdzie popasasz i gdzie masz noclegi.
Teraz Wojski z obławą, już od matecznika
Postawiwszy szeregi, odwrót ci zamyka.

    Tadeusz się dowiedział, że niemało czasu
Już przeszło, jak ogary wpadły w otchłań lasu.

Cicho. Próżno myśliwi natężają ucha;
Próżno jak najciekawszej mowy każdy słucha
Milczenia, długo w miejscu nieruchomy czeka:
Tylko muzyka puszczy gra do nich z daleka.
Psy nurtują po puszczy, jak pod morzem nurki,
A strzelcy, obróciwszy do lasu dwururki,
Patrzą Wojskiego. Ukląkł, ziemię uchem pyta;
Jako w twarzy lekarza wzrok przyjaciół czyta
Wyrok życia lub zgonu miłej im osoby,
Tak strzelcy, ufni w sztuki Wojskiego sposoby,
Topili w nim spojrzenia nadziei i trwogi.
«Jest! jest!» — wyrzekł półgłosem, zerwał się na nogi.
On słyszał! Oni jeszcze słuchali; nareszcie
Słyszą: jeden pies wrzasnął, potem dwa, dwadzieście,
Wszystkie razem ogary rozpierzchnioną zgrają
Doławiają się, wrzeszczą, wpadły na trop, grają,
Ujadają. Już nie jest to powolne granie
Psów goniących zająca, lisa albo łanie;
Lecz wciąż wrzask krótki, częsty, ucinany, zjadły;
To nie na ślad daleki ogary napadły:
Na oko gonią. Nagle ustał krzyk pogoni,
Doszli zwierza. Wrzask znowu, skowyt: zwierz się broni
I zapewne kaleczy; śród ogarów grania
Słychać coraz to częściej jęk psiego konania.

    Strzelcy stali i każdy ze strzelbą gotową
Wygiął się jak łuk naprzód z wciśnioną w las głową.
Nie mogą dłużej czekać! Już ze stanowiska
Jeden za drugim zmyka i w puszczę się wciska,
Chcą pierwsi spotkać źwierza: choć Wojski ostrzegał,
Choć Wojski stanowiska na koniu obiegał,
Krzycząc, że czy kto prostym chłopem, czy paniczem,
Jeżeli z miejsca zejdzie, dostanie w grzbiet smyczem!
Nie było rady! Wszyscy pomimo zakazu
W las pobiegli. Trzy strzelby huknęły od razu;
Potem wciąż kanonada, aż głośniej nad strzały
Ryknął niedźwiedź i echem napełnił las cały.
Ryk okropny, boleści, wściekłości, rozpaczy;
Za nim wrzask psów, krzyk strzelców, trąby dojeżdżaczy
Grzmiały ze środka puszczy. Strzelcy — ci w las śpieszą,
Tamci kurki odwodzą, a wszyscy się cieszą;
Jeden Wojski w żałości, krzyczy, że chybiono.
Strzelcy i obławnicy poszli jedną stroną
Na przełaj źwierza, między ostępem i puszczą,
A niedźwiedź, odstraszony psów i ludzi tłuszczą,
Zwrócił się nazad w miejsca mniej pilnie strzeżone
Ku polom, skąd już zeszły strzelcy rozstawione,
Gdzie tylko pozostali z mnogich łowczych szyków
Wojski, Tadeusz, Hrabia, z kilką obławników.

    Tu las był rzadszy. Słychać z głębi ryk, trzask łomu;
Aż z gęstwy, jak z chmur, wypadł niedźwiedź na kształt gromu;
Wkoło psy gonią, straszą, rwą; on wstał na nogi
Tylne i spojrzał wkoło, rykiem strasząc wrogi,
I przednimi łapami to drzewa korzenie,
To pniaki osmalone, to wrosłe kamienie
Rwał, waląc w psów i w ludzi, aż wyłamał drzewo.
Kręcąc nim jak maczugą na prawo, na lewo,
Runął wprost na ostatnich strażników obławy:
Hrabię i Tadeusza. Oni bez obawy
Stoją w kroku, na źwierza wytknęli flint rury,
Jako dwa konduktory w łono ciemnej chmury;
Aż oba jednym razem pociągnęli kurki
(Niedoświadczeni!), razem zagrzmiały dwururki:
Chybili. Niedźwiedź skoczył; oni tuż utkwiony
Oszczep jeden chwycili czterema ramiony,
Wydzierali go sobie. Spojrzą, aż tu z pyska
Wielkiego, czerwonego dwa rzędy kłów błyska,
I łapa z pazurami już się na łby spuszcza;
Pobledli, w tył skoczyli i, gdzie rzednie puszcza,
Zmykali. Zwierz za nimi wspiął się, już pazury
Zahaczał, chybił, podbiegł, wspiął się znów do góry
I czarną łapą sięgał Hrabiego włos płowy.
Zdarłby mu czaszkę z mozgów jak kapelusz z głowy,
Gdy Asesor z Rejentem wyskoczyli z boków,
A Gerwazy biegł z przodu o jakie sto kroków,
Z nim Robak, choć bez strzelby — i trzej w jednej chwili
Jak gdyby na komendę razem wystrzelili.
Niedźwiedź wyskoczył w górę jak kot przed chartami
I głową na dół runął, i czterma łapami
Przewróciwszy się młyńcem, cielska krwawe brzemię
Waląc tuż pod Hrabiego, zbił go z nóg na ziemię.
Jeszcze ryczał, chciał jeszcze powstać, gdy nań wsiadły
Rozjuszona Strapczyna i Sprawnik zajadły.

    Natenczas Wojski chwycił na taśmie przypięty
Swój róg bawoli, długi, cętkowany, kręty
Jak wąż boa, oburącz do ust go przycisnął,
Wzdął policzki jak banię, w oczach krwią zabłysnął,
Zasunął wpół powieki, wciągnął w głąb pół brzucha
I do płuc wysłał z niego cały zapas ducha,
I zagrał: róg jak wicher wirowatym dechem,
Niesie w puszczę muzykę i podwaja echem.
Umilkli strzelcy, stali szczwacze zadziwieni
Mocą, czystością, dziwną harmoniją pieni.
Starzec cały kunszt, którym niegdyś w lasach słynął,
Jeszcze raz przed uszami myśliwców rozwinął;
Napełnił wnet, ożywił knieje i dąbrowy,
Jakby psiarnię w nie wpuścił i rozpoczął łowy.
Bo w graniu była łowów historyja krótka:
Zrazu odzew dźwięczący, rześki — to pobudka;
Potem jęki po jękach skomlą — to psów granie;
A gdzieniegdzie ton twardszy jak grzmot — to strzelanie.

    Tu przerwał, lecz róg trzymał; wszystkim się zdawało,
Że Wojski wciąż gra jeszcze, a to echo grało.

    Zadął znowu. Myśliłbyś, że róg kształty zmieniał
I że w ustach Wojskiego to grubiał, to cieniał,
Udając głosy zwierząt: to raz w wilczą szyję
Przeciągając się, długo, przeraźliwie wyje;
Znowu jakby w niedźwiedzie rozwarłszy się gardło,
Ryknął; potem beczenie żubra wiatr rozdarło.

    Tu przerwał, lecz róg trzymał; wszystkim się zdawało,
Że Wojski wciąż gra jeszcze, a to echo grało.
Wysłuchawszy rogowej arcydzieło sztuki,
Powtarzały je dęby dębom, bukom buki.

    Dmie znowu. Jakby w rogu były setne rogi,
Słychać zmieszane wrzaski szczwania, gniewu, trwogi,
Strzelców, psiarni i zwierząt; aż Wojski do góry
Podniósł róg i tryumfu hymn uderzył w chmury.

    Tu przerwał, lecz róg trzymał; wszystkim się zdawało,
Że Wojski wciąż gra jeszcze, a to echo grało.
Ile drzew, tyle rogów znalazło się w boru,
Jedne drugim pieśń niosą jak z choru do choru.
I szła muzyka coraz szersza, coraz dalsza,
Coraz cichsza i coraz czystsza, doskonalsza,
Aż znikła gdzieś daleko, gdzieś na niebios progu!

    Wojski obiedwie ręce odjąwszy od rogu
Rozkrzyżował; róg opadł, na pasie rzemiennym
Chwiał się. Wojski z obliczem nabrzmiałym, promiennym,
Z oczyma wzniesionymi, stał jakby natchniony,
Łowiąc uchem ostatnie znikające tony.
A tymczasem zagrzmiało tysiące oklasków,
Tysiące powińszowań i wiwatnych wrzasków.

    Uciszono się z wolna i oczy gawiedzi
Zwróciły się na wielki, świeży trup niedźwiedzi.
Leżał krwią opryskany, kulami przeszyty,
Piersiami w gęszczę trawy wplątany i wbity;
Rozprzestrzenił szeroko przednie krzyżem łapy,
Dyszał jeszcze, wylewał strumień krwi przez chrapy,
Otwierał jeszcze oczy, lecz głowy nie ruszy;
Pijawki Podkomorzego dzierżą go pod uszy,
Z lewej strony Strapczyna, a z prawej zawisał
Sprawnik i dusząc gardziel krew czarną wysysał.

    Za czym Wojski rozkazał kij żelazny włożyć
Psom między zęby i tak paszczęki roztworzyć.
Kolbami przewrócono na wznak zwierza zwłoki
I znów trzykrotny wiwat uderzył w obłoki.

    «A co? — krzyknął Asesor, kręcąc strzelby rurą —
A co? fuzyjka moja? górą nasi, górą!
A co? fuzyjka moja? niewielka ptaszyna,
A jak się popisała? To jej nie nowina:
Nie puści ona na wiatr żadnego ładunku.
Od książęcia Sanguszki mam ją w podarunku».
Tu pokazywał strzelbę przedziwnej roboty,
Choć maleńką, i zaczął wyliczać jej cnoty.
«Ja biegłem — przerwał Rejent, otarłszy pot z czoła —
Biegłem tuż za niedźwiedziem; a pan Wojski woła:
»Stój na miejscu!« Jak tam stać? Niedźwiedź w pole wali,
Rwąc z kopyta jak zając coraz daléj, daléj;
Aż mi ducha nie stało, dobiec ni nadziei,
Aż spojrzę w prawo: sadzi, a tu rzadko w kniei,
Jak też wziąłem na oko: postójże, marucha,
Pomyśliłem, i basta: ot, leży bez ducha!
Tęga strzelba, prawdziwa to Sagalasówka,
Napis: *Sagalas London à Bałabanówka…*
(Sławny tam mieszka ślusarz Polak, który robił
Polskie strzelby, ale je po angielsku zdobił)».

    «Jak to — parsknął Asesor — do kroćset niedźwiedzi!
To to niby pan zabił? Co też to Pan bredzi?»
«Słuchaj no — odparł Rejent — tu, panie, nie śledztwo,
Tu obława, tu wszystkich weźmiem na świadectwo…»

    Więc kłótnia między zgrają wszczęła się zawzięta:
Ci stronę Asesora, ci brali Rejenta.
O Gerwazym nie wspomniał nikt, bo wszyscy biegli
Z boków i, co się z przodu działo, nie postrzegli.
Wojski głos zabrał: «Teraz jest przynajmniej za co;
Bo to, panowie, nie jest ów szarak ladaco,
To niedźwiedź; tu już nie żal poszukać odwetu,
Czy szerpentyną, czyli nawet z pistoletu.
Spór wasz trudno pogodzić, więc dawnym zwyczajem,
Na pojedynek nasze pozwolenie dajem.
Pamiętam, za mych czasów żyło dwóch sąsiadów,
Oba ludzie uczciwi, szlachta z prapradziadów,
Mieszkali po dwóch stronach nad rzeką Wilejką,
Jeden zwał się Domejko, a drugi Dowejko.
Do niedźwiedzicy oba razem wystrzelili:
Kto zabił, trudno dociec; strasznie się kłócili
I przysięgli strzelać się przez niedźwiedzią skórę:
To mi to po szlachecku, prawie rura w rurę.
Pojedynek ten wiele narobił hałasu;
Pieśni o nim śpiewano za owego czasu.
Ja byłem sekundantem; jak się wszystko działo,
Opowiem od początku historyję całą…»

    Nim Wojski zaczął mówić, Gerwazy spór zgodził.
On niedźwiedzia z uwagą dokoła obchodził,
Nareszcie dobył tasak, rozciął pysk na dwoje
I w tylcu głowy, mózgu rozkroiwszy słoje,
Znalazł kulę, wydobył, suknią ochędożył,
Przymierzył do ładunku, do flinty przyłożył,
A potem dłoń podnosząc i kulę na dłoni:
«Panowie — rzekł — ta kula nie jest z waszej broni,
Ona z tej Horeszkowskiej wyszła jednorurki
(Tu podniósł flintę starą, obwiązaną w sznurki),
Lecz nie ja wystrzeliłem. O, trzeba tam było
Odwagi; straszno wspomnieć, w oczach mi się ćmiło!
Bo prosto biegli ku mnie oba paniczowie,
A niedźwiedź z tyłu już, już na Hrabiego głowie,
Ostatniego z Horeszków!… chociaż po kądzieli.
»Jezus Maria!« krzyknąłem i Pańscy anieli
Zesłali mi na pomoc księdza bernardyna.
On nas wszystkich zawstydził; oj, dzielny księżyna!
Gdym drżał, gdym się do cyngla dotknąć nie ośmielił,
On mi z rąk flintę wyrwał, wycelił, wystrzelił:
Między dwie głowy strzelić! sto kroków! nie chybić!
I w sam środek paszczęki! tak mu zęby wybić!
Panowie! długo żyję: jednego widziałem
Człowieka, co mógł takim popisać się strzałem.
Ów głośny niegdyś u nas z tylu pojedynków,
Ów, co korki kobietom wystrzelał z patynków,
Ów łotr nad łotry, sławny w czasy wiekopomne,
Ów Jacek, vulgo Wąsal — nazwiska nie wspomnę…
Ale mu nie czas teraz dojeżdżać niedźwiedzi;
Pewnie po same wąsy hultaj w piekle siedzi.
Chwała księdzu! dwom ludziom on życie ocalił —
Może i trzem: Gerwazy nie będzie się chwalił,
Ale gdyby ostatnie z krwi Horeszków dziecię
Wpadło w bestyi paszczę, nie byłbym na świecie,
I moje by tam stare pogryzł niedźwiedź kości;
Pójdź, księże, wypijemy zdrowie jegomości».

    Próżno szukano księdza; wiedzą tylko tyle,
Że po zabiciu źwierza zjawił się na chwilę,
Podskoczył ku Hrabiemu i Tadeuszowi,
A widząc, że obadwa cali są i zdrowi,
Podniósł ku niebu oczy, cicho pacierz zmówił
I pobiegł w pole szybko, jakby go kto łowił.

    Tymczasem na Wojskiego rozkaz pęki wrzosu,
Suche chrusty i pniaki rzucono do stosu.
Bucha ogień, wyrasta szara sosna dymu,
I rozszerza się w górze na kształt baldakimu.
Nad płomieniem oszczepy złożono w koziołki,
Na grotach zawieszono brzuchate kociołki;
Z wozów niosą jarzyny, mąki i pieczyste,
I chleb.

                        Sędzia otworzył puzderko zamczyste,
W którym rzędami flaszek białe sterczą głowy;
Wybiera z nich największy kufel kryształowy
(Dostał go Sędzia w darze od księdza Robaka):
Wódka to gdańska, napój miły dla Polaka.
«Niech żyje — krzyknął Sędzia w górę wznosząc flaszę —
Miasto Gdańsk, niegdyś nasze, będzie znowu nasze!»
I lał srebrzysty likwor w kolej, aż na końcu
Zaczęło złoto kapać i błyskać na słońcu.

    W kociołkach bigos grzano. W słowach wydać trudno
Bigosu smak przedziwny, kolor i woń cudną;
Słów tylko brzęk usłyszy i rymów porządek,
Ale treści ich miejski nie pojmie żołądek.
Aby cenić litewskie pieśni i potrawy,
Trzeba mieć zdrowie, na wsi żyć, wracać z obławy.

    Przecież i bez tych przypraw potrawą nie lada
Jest bigos, bo się z jarzyn dobrych sztucznie składa.
Bierze się doń siekana, kwaszona kapusta,
Która, wedle przysłowia, sama idzie w usta;
Zamknięta w kotle, łonem wilgotnym okrywa
Wyszukanego cząstki najlepsze mięsiwa;
I praży się, aż ogień wszystkie z niej wyciśnie
Soki żywne, aż z brzegów naczynia war pryśnie
I powietrze dokoła zionie aromatem.

    Bigos już gotów. Strzelcy z trzykrotnym wiwatem,
Zbrojni łyżkami, biegą i bodą naczynie;
Miedź grzmi, dym bucha, bigos jak kamfora ginie;
Zniknął, uleciał; tylko w czeluściach saganów
Wre para jak w kraterze zagasłych wulkanów.

    Kiedy się już do woli napili, najedli,
Źwierza na wóz złożyli, sami na koń siedli,
Radzi wszyscy, rozmowni, oprócz Asesora
I Rejenta; ci byli gniewliwsi niż wczora,
Kłócąc się o zalety, ten swej Sanguszkówki,
A ten bałabanowskiej swej Sagalasówki.
Hrabia też i Tadeusz jadą nieweseli,
Wstydząc się, że chybili i że się cofnęli:
Bo na Litwie, kto źwierza wypuści z obławy,
Długo musi pracować, nim poprawi sławy.

    Hrabia mówił, że pierwszy do oszczepu godził,
I że spotkaniu z źwierzem Tadeusz przeszkodził;
Tadeusz utrzymywał, że będąc silniejszy
I do robienia ciężkim oszczepem zręczniejszy,
Chciał wyręczyć Hrabiego: tak sobie niekiedy
Przemawiali śród gwaru i wrzasku czeredy.

    Wojski jechał pośrodku; staruszek szanowny,
Wesoły był nadzwyczaj i bardzo rozmowny.
Chcąc kłótników zabawić i do zgody dowieść,
Kończył im o Doweyce i Domeyce powieść:
«Asesorze, jeżeli chciałem, byś z Rejentem
Pojedynkował, nie myśl, że jestem zawziętym
Na krew ludzką; broń Boże! Chciałem was zabawić,
Chciałem wam komedyję niby to wyprawić,
Wznowić koncept, który ja lat temu czterdzieście
Wymyśliłem — przedziwny! Wy młodzi jesteście,
Nie pamiętacie o nim; lecz za moich czasów,
Głośny był od tej puszczy do poleskich lasów.

    Domeyki i Doweyki wszystkie sprzeciwieństwa
Pochodziły, rzecz dziwna, z nazwisk podobieństwa
Bardzo niewygodnego. Bo gdy w czas sejmików,
Przyjaciele Doweyki skarbili stronników,
Szepnął ktoś do szlachcica: »Daj kreskę Doweyce«.
A ten, nie dosłyszawszy, dał kreskę Domeyce.
Gdy na uczcie wniósł zdrowie marszałek Rupejko:
»Wiwat Doweyko!« — drudzy krzyknęli: »Domeyko!«
A kto siedział pośrodku, nie trafił do ładu,
Zwłaszcza przy niewyraźnej mowie w czas obiadu.

    Gorzej było. Raz w Wilnie jakiś szlachcic pjany
Bił się w szable z Domeyką i dostał dwie rany;
Potem ów szlachcic, z Wilna wracając do domu,
Dziwnym trafem z Doweyką zjechał się u promu.
Gdy więc na jednym promie płynęli Wilejką,
Pyta sąsiada, kto on? odpowie: Doweyko —
Nie czekając, dobywa rapier spod kirejki:
Czach, czach! i za Domeykę podciął wąs Doweyki.

    Wreszcie, jak na dobitkę, trzeba jeszcze było,
Żeby na polowaniu tak się wydarzyło,
Że stali blisko siebie oba imiennicy,
I do jednej strzelili razem niedźwiedzicy.
Prawda, że po ich strzale upadła bez duchu;
Ale już pierwej niosła z dziesiątek kul w brzuchu.
Strzelby z jednym kalibrem miało wiele osób:
Kto zabił niedźwiedzicę? dojdźże! jaki sposób?

    Tu już krzyknęli: »Dosyć! Trzeba raz rzecz skończyć,
Bóg nas czy diabeł złączył, trzeba się rozłączyć;
Dwóch nas jak dwóch słońc pono zanadto na świecie!«
A więc do szerpentynek i stają na mecie.
Oba szanowni ludzie; co ich szlachta godzą,
To oni na się jeszcze zapalczywiej godzą.
Zmienili broń: od szabel szło na pistolety;
Stają, krzyczym, że nadto przybliżyli mety;
Oni na złość, przysięgli przez niedźwiedzią skórę
Strzelać się: śmierć niechybna! prawie rura w rurę.
Oba tęgo strzelali — »Sekunduj, Hreczecha!«
»Zgoda — rzekłem — niech zaraz dół wykopie klecha:
Bo taki spór nie może skończyć się na niczym;
Lecz bijcie się szlacheckim trybem, nie rzeźniczym.
Dosyć już mety zbliżać, widzę, żeście zuchy;
Chcecie strzelać się, rury oparłszy na brzuchy?
Ja nie pozwolę. Zgoda, że na pistolety;
Lecz strzelać się nie z dalszej ani z bliższej mety,
Jak przez skórę niedźwiedzią. Ja rękami memi
Jako sekundant skórę rozciągnę na ziemi,
I ja sam was ustawię: Waść po jednej stronie
Stanie na końcu pyska, a Waść na ogonie«.
»Zgoda!« — wrzaśli; czas? — jutro; miejsce? — karczma Usza.
Rozjechali się. Ja zaś do Wirgilijusza…»

    Tu Wojskiemu przerwał krzyk: «Wyczha!» Tuż spod koni
Smyknął szarak; już Kusy, już go Sokół goni.
Psy wzięto na obławę wiedząc, że z powrotem
Na polu łatwo można napotkać się z kotem;
Bez smyczy szły przy koniach; gdy kota spostrzegły,
Wprzód nim strzelcy poszczuli, już za nim pobiegły.
Rejent też i Asesor chcieli końmi natrzeć;
Lecz Wojski wstrzymał krzycząc: «Wara! stać i patrzeć!
Nikomu krokiem ruszyć z miejsca nie dozwolę;
Stąd widzim wszyscy dobrze, zając idzie w pole».
W istocie, kot czuł z tyłu myśliwych i psiarnie,
Rwał w pole, słuchy wytknął jak dwa różki sarnie,
Sam szarzał się nad rolą długi, wyciągnięty,
Skoki pod nim sterczały jakby cztery pręty,
Rzekłbyś, że ich nie rusza, tylko ziemię trąca
Po wierzchu, jak jaskółka wodę całująca.
Pył za nim, psy za pyłem; z daleka się zdało,
Że zając, psy i charty jedne tworzą ciało:
Jakby jakaś przez pole suwała się żmija,
Kot jak głowa, pył z tyłu jakby modra szyja,
A psami jak podwójnym ogonem wywija.

    Rejent, Asesor patrzą, otworzyli usta,
Dech wstrzymali. Wtem Rejent pobladnął jak chusta,
Zbladł i Asesor; widzą… fatalnie się dzieje:
Owa żmija im dalej, tym bardziej dłużeje,
Już rwie się wpół, już znikła owa szyja pyłu,
Głowa już blisko lasu, ogony, gdzie z tyłu!
Głowa niknie; raz jeszcze jakby kto kutasem
Mignął: w las wpadła; ogon urwał się pod lasem.

    Biedne psy, ogłupiałe, biegały pod gajem,
Zdawały się naradzać, oskarżać nawzajem.
Wreszcie wracają, z wolna skacząc przez zagony,
Spuściły uszy, tulą do brzucha ogony
I przybiegłszy, ze wstydu nie śmieją wznieść oczu,
I zamiast iść do panów, stały na uboczu.

    Rejent spuścił ku piersiom zasępione czoło,
Asesor rzucał okiem, ale niewesoło;
Potem zaczęli oba słuchaczom wywodzić:
Jak ich charty bez smycza nie nawykły chodzić,
Jak kot znienacka wypadł, jak źle był poszczuty
Na roli, gdzie psom chyba trzeba by wdziać buty,
Tak pełno wszędzie głazów i ostrych kamieni…

    Mądrze rzecz wyłuszczali szczwacze doświadczeni;
Myśliwi z tych mów wiele mogliby korzystać,
Lecz nie słuchali pilnie. Ci zaczęli świstać,
Ci śmiać się w głos, ci, mając niedźwiedzia w pamięci,
Gadali o nim, świeżą obławą zajęci.

    Wojski ledwie raz okiem za zającem rzucił;
Widząc, że uciekł, głowę obojętnie zwrócił
I kończył rzecz przerwaną: «Na czym więc stanąłem?
Aha! na tym, że obu za słowo ująłem,
Iż będą strzelali się przez niedźwiedzią skórę…
Szlachta w krzyk: »To śmierć pewna! Prawie rura w rurę!«
A ja w śmiech. Bo mnie uczył mój przyjaciel Maro,
Że skóra zwierza nie jest lada jaką miarą.
Wszak wiecie waćpanowie, jak królowa Dydo
Przypłynęła do Libów i tam z wielką biédą
Wytargowała sobie taki ziemi kawał,
Który by się wołową skórą nakryć dawał:
Na tym kawałku ziemi stanęła Kartago!
Więc ja to sobie w nocy rozbieram z uwagą.

    Ledwie dniało, już z jednej strony taradejką
Jedzie Doweyko, z drugiej na koniu Domeyko.
Patrzą, aż tu przez rzekę leży most kosmaty,
Pas ze skóry niedźwiedziej, porzniętej na szmaty.
Postawiłem Doweykę na źwierza ogonie
Z jednej strony, Domeykę zaś po drugiej stronie:
»Pukajcie teraz — rzekłem — choć przez całe życie,
Lecz póty was nie spuszczę, aż się pogodzicie«.
Oni w złość; a tu szlachta kładnie się na ziemi
Od śmiechu, a ja z księdzem słowy poważnemi
Nuż im z Ewangelii, z statutów dowodzić;
Nie ma rady: śmieli się i musieli zgodzić.

    Spór ich potem w dozgonną przyjaźń się zamienił,
I Doweyko się z siostrą Domeyki ożenił;
Domeyko pojął siostrę szwagra, Doweykównę,
Podzielili majątek na dwie części równe,
A w miejscu, gdzie się zdarzył tak dziwny przypadek,
Pobudowawszy karczmę, nazwali Niedźwiadek».




Księga piąta



Kłótnia

Plany myśliwskie Telimeny — Ogrodniczka wybiera się na wielki świat i słucha nauk opiekunki — Strzelcy wracają — Wielkie zadziwienie Tadeusza — Spotkanie się powtórne w Świątyni dumania i zgoda ułatwiona za pośrednictwem mrówek — U stołu wytacza się rzecz o łowach — Powieść Wojskiego o Rejtanie i księciu Denassów, przerwana — Zagajenie układów między stronami, także przerwane — Zjawisko z kluczem — Kłótnia — Hrabia z Gerwazym odbywają radę wojenną.

    Wojski, chlubnie skończywszy łowy, wraca z boru,
A Telimena w głębi samotnego dworu
Zaczyna polowanie. Wprawdzie nieruchoma,
Siedzi z założonymi na piersiach rękoma,
Lecz myślą goni źwierzów dwóch; szuka sposobu,
Jak by razem obsaczyć i ułowić obu:
Hrabię i Tadeusza. Hrabia panicz młody,
Wielkiego domu dziedzic, powabnej urody,
Już trochę zakochany: cóż? może się zmienić!
Potem, czy szczerze kocha? czy się zechce żenić?
Z kobietą kilku laty starszą! niebogatą!
Czy mu krewni pozwolą? co świat powie na to?

    Telimena, tak myśląc, z sofy się podniosła
I stanęła na palcach: rzekłbyś, że podrosła;
Odkryła nieco piersi, wygięła się bokiem,
I sama siebie pilnym obejrzała okiem,
I znowu zapytała o radę zwierciadła;
Po chwili wzrok spuściła, westchnęła i siadła.

    Hrabia pan! zmienni w gustach są ludzie majętni!
Hrabia blondyn… blondyni nie są zbyt namiętni!
A Tadeusz? prostaczek! poczciwy chłopczyna!
Prawie dziecko! raz pierwszy kochać się zaczyna!
Pilnowany, niełacno zerwie pierwsze związki;
Przy tym dla Telimeny ma już obowiązki…
Mężczyźni, póki młodzi, chociaż w myślach zmienni,
W uczuciach są od dziadów stalsi, bo sumienni.
Długo serce młodzieńca, proste i dziewicze,
Chowa wdzięczność za pierwsze miłości słodycze!
Ono rozkosz i wita, i żegna z weselem,
Jak skromną ucztę, którą dzielim z przyjacielem.
Tylko stary pjanica, gdy już spali trzewa,
Brzydzi się trunkiem, którym nazbyt się zalewa.
Wszystko to Telimena dokładnie wiedziała,
Bo i rozum, i wielkie doświadczenie miała.

    Lecz co powiedzą ludzie?… Można im zejść z oczu,
W inne strony wyjechać, mieszkać na uboczu
Lub, co lepsza, wynieść się całkiem z okolicy,
Na przykład zrobić małą podróż do stolicy,
Młodego chłopca na świat wielki wyprowadzić,
Kroki jego kierować, pomagać mu, radzić,
Serce mu kształcić, mieć w nim przyjaciela, brata,
Nareszcie — użyć świata póki służą lata!…

    Tak myśląc, po alkowie śmiało i wesoło
Przeszła się kilka razy. Znów spuściła czoło.

    Warto by też pomyślić o Hrabiego losie…
Czyby się nie udało podsunąć mu Zosię?
Niebogata: lecz za to urodzeniem równa,
Z domu senatorskiego, jest dygnitarzówna.
Jeżeliby do skutku przyszło ożenienie,
Telimena w ich domu miałaby schronienie
Na przyszłość; krewna Zosi i Hrabiego swatka,
Dla młodego małżeństwa byłaby jak matka.

    Po tej z sobą odbytej, stanowczej naradzie,
Woła przez okno Zosię, bawiącą się w sadzie.

    Zosia w porannym stroju i z głową odkrytą
Stała, trzymając w ręku podniesione sito;
Do nóg jej biegło ptastwo. Stąd kury szurpate
Toczą się kłębkiem; stamtąd kogutki czubate,
Wstrząsając koralowe na głowach szyszaki
I wiosłując skrzydłami przez bruzdy i krzaki,
Szeroko wyciągają ostrożaste pięty;
Za nimi z wolna indyk sunie się odęty
Sarkając na gderanie swej krzykliwej żony;
Ówdzie pawie jak tratwy długimi ogony
Sterują się po łące, a gdzieniegdzie z góry
Upada jak kiść śniegu gołąb srebrnopióry.
W pośrodku zielonego okręgu murawy,
Ściska się okrąg ptastwa, krzykliwy, ruchawy,
Opasany gołębi sznurem, na kształt wstęgi
Białej, środkiem pstrokaty w gwiazdy, w cętki, w pręgi.
Tu dzioby bursztynowe, tam czubki z korali
Wznoszą się z gęstwi pierza jak ryby spod fali,
Wysuwają się szyje i w ruchach łagodnych
Chwieją się ciągle na kształt tulipanów wodnych;
Tysiące oczu jak gwiazd błyskają ku Zosi.

    Ona w środku wysoko nad ptastwem się wznosi;
Sama biała i w długą bieliznę ubrana
Kręci się, jak bijąca śród kwiatów fontanna;
Czerpie z sita i sypie na skrzydła i głowy,
Ręką jak perły białą, gęsty grad perłowy
Krup jęczmiennych. To ziarno godne pańskich stołów,
Robi się dla zaprawy litewskich rosołów;
Zosia je wykradając z szafy ochmistrzyni
Dla swego drobiu, szkodę w gospodarstwie czyni.

    Usłyszała wołanie: «Zosiu!» To głos cioci!
Sypnęła razem ptastwu ostatek łakoci,
A sama kręcąc sito, jako tanecznica
Bębenek, i w takt bijąc, swawolna dziewica
Jęła skakać przez pawie, gołębie i kury:
Zmieszane ptastwo tłumnie furknęło do góry.
Zosia, stopami ledwie dotykając ziemi,
Zdawała się najwyżej bujać między niemi;
Przodem gołębie białe, które w biegu płoszy,
Leciały jak przed wozem bogini rozkoszy.

    Zosia przez okno z krzykiem do alkowy wpadła,
I na kolanach ciotki zadyszana siadła;
Telimena, całując i głaszcząc pod brodę,
Z radością zważa dziecka żywość i urodę
(Bo prawdziwie kochała swą wychowanicę).
Ale znowu poważnie nastroiła lice,
Wstała i przechodząc się wszerz i wzdłuż alkowy,
Dzierżąc palec przy ustach, tymi rzekła słowy:

    «Kochana Zosiu, już też całkiem zapominasz
I na stan, i na wiek twój: wszak to dziś zaczynasz
Rok czternasty. Czas rzucić indyki i kurki;
Fi! to godna zabawka dygnitarskiej córki!
I z umurzaną dziatwą chłopską już do woli
Napieściłaś się! Zosiu, patrząc serce boli:
Opaliłaś okropnie płeć, czysta Cyganka,
A chodzisz i ruszasz się jak parafijanka.
Już ja temu wszystkiemu na przyszłość zaradzę;
Od dziś zacznę, dziś ciebie na świat wyprowadzę,
Do salonu, do gości — gości mamy siła;
Patrzajżeż, ażebyś mnie wstydu nie zrobiła».

    Zosia skoczyła z miejsca i klasnęła w dłonie,
I ciotce zawisnąwszy oburącz na łonie,
Płakała i śmiała się na przemian z radości.
«Ach ciociu, już tak dawno nie widziałam gości!
Od czasu, jak tu żyję z kury i indyki,
Jeden gość, co widziałam, to był gołąb dziki.
Już mi troszeczkę nudno tak siedzieć w alkowie;
Pan Sędzia nawet mówi, że to źle na zdrowie».

    «Sędzia! — przerwała ciotka — ciągle mi dokuczał
Żeby cię na świat wywieść, ciągle pod nos mruczał
Że już jesteś dorosła: sam nie wie, co plecie,
Dziaduś, nigdy na wielkim niebywały świecie.
Ja wiem lepiej, jak długo trzeba się sposobić
Panience, by wyszedłszy na świat efekt zrobić.
Wiedz Zosiu, że kto rośnie na widoku ludzi,
Choć piękny, choć rozumny, efektów nie wzbudzi,
Gdy go wszyscy przywykną widzieć od maleńka;
Lecz niechaj ukształcona, dorosła panienka,
Nagle ni stąd, ni zowąd przed światem zabłyśnie,
Wtenczas każdy się do niej przez ciekawość ciśnie,
Wszystkie jej ruchy, rzuty oczu jej uważa,
Słowa jej podsłuchiwa i drugim powtarza;
A kiedy wejdzie w modę raz młoda osoba,
Każdy ją chwalić musi, choć i nie podoba.
Znaleźć się, spodziewam się, że umiesz: w stolicy
Urosłaś; choć dwa lata mieszkasz w okolicy,
Nie zapomniałaś jeszcze całkiem Petersburka.
No, Zosiu, toaletę rób, dostań tam z biurka,
Nagotowane znajdziesz wszystko do ubrania.
Spiesz się, bo lada chwila wrócą z polowania».

    Wezwano pokojowę i służącą dziewkę,
W naczynie srebrne wody wylano konewkę.
Zosia, jak wróbel w piasku, trzepioce się, myje
Z pomocą sługi ręce, oblicze i szyję.
Telimena otwiera petersburskie składy,
Dobywa flaszki perfum, słoiki pomady,
Pokrapia Zosię wkoło wyborną perfumą,
(Woń napełniła izbę) włos namaszcza gumą.
Zosia kładnie pończoszki białe, ażurowe,
I trzewiki warszawskie białe, atłasowe.
Tymczasem pokojowa sznurowała stanik,
Potem rzuciła na gors pannie pudermanik;
Zaczęto przypieczone zbierać papiloty,
Pukle, że nazbyt krótkie, uwito w dwa sploty,
Zostawując na czole i skroniach włos gładki;
Pokojowa zaś świeżo zebrane bławatki
Uwiązawszy w plecionkę daje Telimenie,
Ta ją do głowy Zosi przyszpila uczenie,
Z prawej strony na lewo: kwiat od bladych włosów
Odbijał bardzo pięknie, jak od zboża kłosów!
Zdjęto puderman, całe ubranie gotowe.
Zosia białą sukienkę wrzuciła przez głowę,
Chusteczkę batystową białą w ręku zwija,
I tak cała wygląda biała jak lilija.

    Poprawiwszy raz jeszcze i włosów, i stroju,
Kazano jej wzdłuż i wszerz przejść się po pokoju.
Telimena uważa znawczyni oczyma,
Musztruje siostrzenicę, gniewa się i zżyma;
Aż na dygnienie Zosi krzyknęła z rozpaczy:
«Ja nieszczęśliwa! Zosiu, widzisz co to znaczy
Żyć z gęśmi, z pastuchami! Tak nogi rozszerzasz
Jak chłopiec, okiem w prawo i w lewo uderzasz,
Czysta rozwódka!… Dygnij, patrz, jaka niezwinna!»
«Ach ciociu — rzekła smutnie Zosia — cóż ja winna!
Ciotka mnie zamykała; nie było z kim tańczyć,
Lubiłam z nudy ptastwo paść i dzieci niańczyć.
Ale poczekaj ciociu, niech no się pobawię
Trochę z ludźmi, obaczysz, jak się ja poprawię».

    «Już — rzekła ciotka — z dwojga złego, lepiej z ptastwem,
Niż z tym, co u nas dotąd gościło plugastwem;
Przypomnij tylko sobie, kto tu u nas bywał:
Pleban, co pacierz mruczał lub w warcaby grywał,
I palestra z fajkami! To mi kawalery!
Nabrałabyś się od nich pięknej manijery.
Teraz to pokazać się jest przynajmniej komu,
Mamy przecież uczciwe towarzystwo w domu.
Uważaj dobrze, Zosiu, jest tu Hrabia młody,
Pan dobrze wychowany, krewny wojewody,
Pamiętaj być mu grzeczną».

                        Słychać rżenie koni
I gwar myśliwców; już są pod bramą: to oni!
Wziąwszy Zosię pod rękę pobiegła do sali.
Myśliwi na pokoje jeszcze nie wchadzali;
Musieli po komnatach odmieniać swą odzież,
Nie chcąc wniść do dam w kurtkach. Pierwsza wpadła młodzież,
Pan Tadeusz i Hrabia, co żywo przebrani.

    Telimena sprawuje obowiązki pani,
Wita wchodzących, sadza, rozmową zabawia,
I siostrzenicę wszystkim z kolei przedstawia:
Naprzód Tadeuszowi, jako krewną bliską.
Zosia grzecznie dygnęła, on skłonił się nisko,
Chciał coś do niej przemówić, już usta otworzył:
Ale spojrzawszy w oczy Zosi, tak się strwożył,
Że stojąc niemy przed nią, to płonął, to bladnął;
Co było w jego sercu, on sam nie odgadnął.
Uczuł się nieszczęśliwym bardzo — poznał Zosię!
Po wzroście i po włosach światłych, i po głosie;
Tę kibić i tę główkę widział na parkanie,
Ten wdzięczny głos zbudził go dziś na polowanie.

    Aż Wojski Tadeusza wyrwał z zamięszania;
Widząc, że bladnie i że na nogach się słania,
Radził mu odejść do swej izby dla spoczynku.
Tadeusz stanął w kącie, wsparł się na kominku,
Nic nie mówiąc — szerokie, obłędne źrenice
Obracał to na ciotkę, to na siostrzenicę.
Dostrzegła Telimena, iż pierwsze spojrzenie
Zosi tak wielkie na nim zrobiło wrażenie;
Nie odgadła wszystkiego, przecież pomięszana
Bawi gości, a z oczu nie spuszcza młodziana.
Wreszcie czas upatrzywszy ku niemu podbiega:
Czy zdrów? dlaczego smutny? pyta się, nalega,
Napomyka o Zosi, zaczyna z nim żarty;
Tadeusz nieruchomy, na łokciu oparty,
Nic nie gadając marszczył brwi i usta krzywił:
Tym bardziej Telimenę pomięszał i zdziwił.
Zmieniła więc natychmiast twarz i ton rozmowy,
Powstała zagniewana, i ostrymi słowy
Poczęła nań przymówki sypać i wyrzuty.
Porwał się i Tadeusz jak żądłem ukłuty,
Spojrzał krzywo, nie mówiąc ani słowa, splunął,
Krzesło nogą odepchnął i z pokoju runął,
Trzasnąwszy drzwi za sobą. Szczęściem, że tej sceny
Nikt z gości nie uważał oprócz Telimeny.

    Wyleciawszy przez bramę, biegł prosto na pole.
Jak szczupak, gdy mu oścień skróś piersi przekole,
Pluska się i nurtuje, myśląc że uciecze,
Ale wszędzie żelazo i sznur z sobą wlecze:
Tak i Tadeusz ciągnął za sobą zgryzoty,
Suwając się przez rowy i skacząc przez płoty,
Bez celu i bez drogi; aż niemało czasu
Nabłąkawszy się, w końcu wszedł w głębinę lasu
I trafił, czy umyślnie, czyli też przypadkiem,
Na wzgórek, co był wczora szczęścia jego świadkiem,
Gdzie dostał ów bilecik, zadatek kochania,
Miejsce, jak wiemy, zwane *Świątynią dumania*.

    Gdy okiem wkoło rzuca, postrzega: to ona!
Telimena, samotna, w myślach pogrążona,
Od wczorajszej postacią i strojem odmienna,
W bieliźnie, na kamieniu, sama jak kamienna;
Twarz schyloną w otwarte utuliła dłonie,
Choć nie słyszysz szlochania, znać, że we łzach tonie.

    Daremnie broniło się serce Tadeusza;
Ulitował się, uczuł że go żal porusza.
Długo poglądał niemy, ukryty za drzewem,
Na koniec westchnął i rzekł sam do siebie z gniewem:
«Głupi! cóż ona winna, że się ja pomylił?»
Więc z wolna głowę ku niej zza drzewa wychylił —
Gdy nagle Telimena zrywa się z siedzenia,
Rzuca się w prawo, w lewo, skacze skróś strumienia,
Rozkrzyżowana, z włosem rozpuszczonym, blada,
Pędzi w las, podskakuje, przyklęka, upada,
I nie mogąc już powstać, kręci się po darni;
Widać z jej ruchów, w jakiej strasznej jest męczarni:
Chwyta się za pierś, szyję, za stopy, kolana.
Skoczył Tadeusz myśląc, że jest pomieszana
Lub ma wielką chorobę. Lecz z innej przyczyny
Pochodziły te ruchy.

                        U bliskiej brzeziny
Było wielkie mrowisko. Owad gospodarny
Snuł się wkoło po trawie, ruchawy i czarny.
Nie wiedzieć, czy z potrzeby czy z upodobania,
Lubił szczególnie zwiedzać *Świątynię dumania*;
Od stołecznego wzgórka aż po źródła brzegi
Wydeptał drogę, którą wiódł swoje szeregi.
Nieszczęściem, Telimena siedziała śród drożki:
Mrówki, znęcone blaskiem bieluchnej pończoszki,
Wbiegły, gęsto zaczęły łaskotać i kąsać,
Telimena musiała uciekać, otrząsać,
Na koniec na murawie siąść i owad łowić.

    Nie mógł jej swej pomocy Tadeusz odmówić:
Oczyszczając sukienkę, aż do nóg się zniżył,
Usta trafem ku skroniom Telimeny zbliżył —
W tak przyjaznej postawie, choć nic nie mówili
O rannych kłótniach swoich, przecież się zgodzili;
I nie wiedzieć, jak długo trwałaby rozmowa,
Gdyby ich nie przebudził dzwonek z Soplicowa —
Hasło wieczerzy.

                        Pora powracać do domu,
Zwłaszcza że słychać było opodal trzask łomu.
Może szukają? razem wracać nie wypada;
Więc Telimena w prawo pod ogród się skrada,
A Tadeusz na lewo biegł do wielkiej drogi.
Oboje w tym odwrocie mieli nieco trwogi:
Telimenie zdało się, że raz spoza krzaka
Błysła zakapturzona, chuda twarz Robaka;
Tadeusz widział dobrze, jak mu raz i drugi
Pokazał się na lewo cień biały i długi,
Co to było, nie wiedział, ale miał przeczucie,
Że to był Hrabia w długim, angielskim surducie.

    Wieczerzano w zamczysku. Uparty Protazy,
Nie dbając na wyraźne Sędziego zakazy,
W niebytność państwa znowu do zamku szturmował,
I kredens doń (jak mówi) zaintromitował.

    Goście weszli w porządku i stanęli kołem;
Podkomorzy najwyższe brał miejsce za stołem:
Z wieku mu i z urzędu ten zaszczyt należy,
Idąc kłaniał się damom, starcom i młodzieży;
Kwestarz nie był u stołu; miejsce bernardyna,
Po prawej stronie męża, ma Podkomorzyna,
Sędzia, kiedy już gości jak trzeba ustawił,
Żegnając po łacinie, stół pobłogosławił.
Mężczyznom dano wódkę; za czym wszyscy siedli,
I chłodnik zabielany milcząc żwawo jedli.

    Po chłodniku szły raki, kurczęta, szparagi,
W towarzystwie kielichów węgrzyna, malagi.
Jedzą, piją, a milczą wszyscy. Nigdy pono,
Od czasu jako mury zamku podźwigniono,
Który uraczał hojnie tylu szlachty bratów,
Tyle wesołych słyszał i odbił wiwatów,
Nie pamiętano takiej posępnej wieczerzy;
Tylko pukanie korków i brzęki talerzy,
Odbijała zamkowa sień wielka i pusta:
Rzekłbyś, iż zły duch gościom zasznurował usta.

    Mnogie były powody milczenia. Myśliwi
Powrócili z ostępu dosyć gadatliwi,
Lecz gdy zapał ochłonął, myśląc nad obławą,
Postrzegają, że wyszli z niej z niewielką sławą:
Trzebaż było, ażeby jeden kaptur popi,
Wyrwawszy się Bóg wie skąd, jak Filip z konopi,
Przepisał wszystkich strzelców powiatu? O wstydzie!
Cóż o tym będą gadać w Oszmianie i Lidzie,
Które od wieków walczą z tutejszym powiatem
O pierwszeństwo w strzelectwie? Myślili więc nad tem.

    Zaś Asesor i Rejent, prócz wspólnych niechęci,
Świeżą hańbę swych chartów mieli na pamięci.
W oczach im stoi niecny kot: skoki wyciąga,
I omykiem spod gaju kiwając urąga,
I tym omykiem ćwiczy po sercach jak biczem…
Siedzieli z pochylonym ku misie obliczem.
Asesor nowe jeszcze miał powody żalów,
Patrząc na Telimenę i na swych rywalów.

    Do Tadeusza siedzi Telimena bokiem,
Pomięszana, zaledwie śmie nań rzucić okiem;
Chciała zasępionego Hrabiego zabawić,
Wyzwać w dłuższą rozmowę, w lepszy humor wprawić;
Bo Hrabia dziwnie kwaśny powrócił z przechadzki
A raczej, jako myślił Tadeusz, z zasadzki.
Słuchając Telimeny, czoło podniósł hardo,
Brwi zmarszczył, spojrzał na nią ledwie nie z pogardą;
Potem przysiadł się, jak mógł najbliżej, do Zosi,
Nalewa jej do szklanki, talerze przynosi,
Prawi tysiąc grzeczności, kłania się, uśmiécha,
Czasem oczy wywraca i głęboko wzdycha.
Widać przecież, pomimo tak zręczne łudzenie,
Że umizgał się tylko na złość Telimenie:
Bo głowę odwracając, niby nieumyślnie,
Coraz ku Telimenie groźnym okiem błyśnie.

    Telimena nie mogła pojąć, co to znaczy;
Ruszywszy ramionami, myśliła: dziwaczy!
Wreszcie nowym zalotom Hrabiego dość rada,
Zwróciła się do swego drugiego sąsiada.

    Tadeusz też posępny, nic nie jadł, nic nie pił,
Zdawał się słuchać rozmów, oczy w talerz wlepił;
Telimena mu leje wino, on się gniewa
Na natrętność; pytany o zdrowie — poziewa.
Ma za złe (tak się zmienił jednego wieczora),
Że Telimena zbytnie do zalotów skora;
Gorszy się, że jej suknia tak wcięta głęboko,
Nieskromnie — a dopiero, kiedy podniósł oko!
Aż przeląkł się; bystrzejsze teraz miał źrenice.
Ledwie spojrzał w rumiane Telimeny lice,
Odkrył od razu wielką, straszną tajemnicę —
Przebóg! naróżowana!

                        Czy róż w złym gatunku,
Czy jakoś na obliczu przetarł się z trafunku:
Gdzieniegdzie zrzedniał, na wskroś grubszą płeć odsłania…
Może to sam Tadeusz, w *Świątyni dumania*,
Rozmawiając za blisko, omusknął z bielidła
Karmin lżejszy od pyłków motylego skrzydła;
Telimena wracała nazbyt śpieszno z lasu,
I poprawić kolory swe nie miała czasu:
Około ust szczególnie widne były piegi.
Nuż oczy Tadeusza, jako chytre szpiegi,
Odkrywszy jedną zdradę, poczną w kolej zwiedzać
Resztę wdzięków i wszędzie jakiś fałsz wyśledzać:
Dwóch zębów brakuje w ustach; na czole, na skroni
Zmarszczki; tysiąc zmarszczków pod brodą się chroni!

    Niestety! Czuł Tadeusz, jak jest niepotrzebnie
Rzecz piękną nazbyt ściśle zważać; jak haniebnie,
Być szpiegiem swej kochanki; nawet jak szkaradnie,
Odmieniać smak i serce — lecz któż sercem władnie?
Darmo chce brak miłości zastąpić sumnieniem,
Chłód duszy ogrzać znowu jej wzroku promieniem:
Już ten wzrok, jako księżyc światły a bez ciepła,
Błyskał po wierzchu duszy, która do dna krzepła.
Takie robiąc sam w sobie wyrzuty i skargi,
Pochylił w talerz głowę, milczał i gryzł wargi.

    Tymczasem zły duch nową pokusą go wabi,
Podsłuchiwać, co Zosia mówiła do Hrabi.
Dziewczyna, uprzejmością Hrabiego ujęta,
Zrazu rumieniła się, spuściwszy oczęta,
Potem śmiać się zaczęli, w końcu rozmawiali
O jakimś niespodzianym w ogrodzie spotkaniu,
O jakimś po łopuchach i grzędach stąpaniu,
Tadeusz, wyciągnąwszy co najdłużej uszy,
Połykał gorzkie słowa i przetrawiał w duszy.
Okropną miał biesiadę. Jak w ogrodzie żmija
Dwoistym żądłem zioło zatrute wypija,
Potem skręci się w kłębek i na drodze legnie,
Grożąc stopie, co na nią nieostrożnie biegnie:
Tak Tadeusz, opiły trucizną zazdrości,
Zdawał się obojętny, a pękał ze złości.

    W najweselszym zebraniu, niech się kilku gniewa,
Zaraz się ich ponurość na resztę rozlewa:
Strzelcy dawniej milczeli; druga stołu strona
Umilkła, Tadeusza żółcią zarażona.

    Nawet pan Podkomorzy nadzwyczaj ponury,
Nie miał ochoty gadać, widząc swoje córy,
Posażne i nadobne panny, w wieku kwiecie,
Zdaniem wszystkich najpierwsze partyje w powiecie,
Milczące, zaniedbane od milczącej młodzi.
Gościnnego Sędziego również to obchodzi;
Wojski zaś, uważając że tak wszyscy milczą,
Nazywał tę wieczerzę nie polską, lecz wilczą.

    Hreczecha na milczenie miał słuch bardzo czuły.
Sam gawęda, i lubił niezmiernie gaduły.
Nie dziw! Ze szlachtą strawił życie na biesiadach,
Na polowaniach, zjazdach, sejmikowych radach:
Przywykł, żeby mu zawsze coś bębniło w uchu,
Nawet wtenczas, gdy milczał lub z placką za muchą
Skradał się, lub zamknąwszy oczy siadał marzyć;
W dzień szukał rozmów, w nocy musiano mu gwarzyć
Pacierze różańcowe albo gadać bajki.
Stąd też nieprzyjacielem zabitym był fajki,
Wymyślonej od Niemców, by nas zcudzoziemczyć;
Mawiał: Polskę oniemić, jest to Polskę zniemczyć.
Starzec, wiek przegwarzywszy, chciał spoczywać w gwarze;
Milczenie go budziło ze snu: tak młynarze,
Uśpieni kół turkotem, ledwie staną osie,
Budzą się krzycząc z trwogą: «A słowo stało się…»

    Wojski ukłonem dawał znak Podkomorzemu,
A ręką od ust lekko skinął ku Sędziemu,
Prosząc o głos. Panowie na ten ukłon niemy
Odkłonili się oba, co znaczy: prosiemy.
Wojski zagaił.

                        «Śmiałbym upraszać młodzieży,
Ażeby po staremu bawić u wieczerzy,
Nie milczeć i żuć: czy my ojce kapucyni?
Kto milczy między szlachtą, to właśnie tak czyni,
Jako myśliwiec, który nabój rdzawi w strzelbie.
Dlatego ja rozmowność naszych przodków wielbię:
Po łowach szli do stołu, nie tylko by jadać,
Ale aby nawzajem mogli się wygadać,
Co każdy miał na sercu; nagany, pochwały
Strzelców i obławników, ogary, wystrzały
Wywoływano na plac; powstawała wrzawa,
Miła uchu myśliwców jak druga obława.
Wiem, wiem, o co wam idzie. Ta czarnych trosk chmura
Pono z Robakowego wzniosła się kaptura!
Wstydzicie się swych pudeł! Niech was wstyd nie pali:
Znałem myśliwych lepszych od was, a chybiali;
Trafiać, chybiać, poprawiać, to kolej strzelecka.
Ja sam, chociaż ze strzelbą włóczę się od dziecka,
Chybiałem; chybiał sławny ów strzelec Tułoszczyk,
Nawet nie zawsze trafiał pan Rejtan nieboszczyk.
O Rejtanie opowiem później. Co się tycze
Wypuszczenia z obławy, że oba panicze
Zwierzowi jak należy kroku nie dostali,
Choć mieli oszczep w ręku: tego nikt nie chwali
Ani gani. Bo zmykać, mając nabój w rurze,
Znaczyło po staremu być tchórzem nad tchórze;
Toż wystrzelić na oślep (jak to robi wielu),
Nie przypuściwszy źwierza, nie wziąwszy do celu,
Jest rzecz haniebna; ale kto dobrze wymierzy,
Kto przypuści do siebie źwierza jak należy,
Jeśli chybił, cofnąć się może bez sromoty,
Albo walczyć oszczepem — lecz z własnej ochoty,
A nie z musu: gdyż oszczep strzelcom poruczony
Nie dla natarcia, ale tylko dla obrony.
Tak było po staremu. A więc mnie zawierzcie,
I waszej rejterady do serca nie bierzcie,
Kochany Tadeuszku i wielmożny grafie;
Ilekroć zaś wspomnicie o dzisiejszym trafie,
Wspomnijcie też starego Wojskiego przestrogę:
Nigdy jeden drugiemu nie zachodzić w drogę,
Nigdy we dwóch nie strzelać do jednej źwierzyny».

    Właśnie Wojski wymawiał to słowo: *źwierzyny*,
Gdy Asesor półgębkiem podszepnął: *dziewczyny*;
«Brawo!» krzyknęła młodzież, powstał szmer i śmiechy;
Powtarzano z kolei przestrogę Hreczechy,
Mianowicie ostatnie słowo; ci *źwierzyny*,
A drudzy, w głos śmiejąc się, krzyczeli: *dziewczyny*.
Rejent szepnął: *kobiety*, Asesor: *kokiety*,
Utkwiwszy w Telimenie oczy jak sztylety.

    Nie myślił wcale Wojski przymawiać nikomu,
Ani uważał, co tam szepczą po kryjomu;
Rad bardzo, że mógł damy i młodzież rozśmieszyć,
Zwrócił się ku myśliwcom, chcąc i tych pocieszyć;
I zaczął, nalewając sobie kielich wina:

    «Nadaremnie oczyma szukam bernardyna;
Chciałbym mu opowiedzieć wypadek ciekawy,
Podobny do zdarzenia dzisiejszej obławy.
Klucznik mówił, że tylko znał jednego człeka,
Co tak celnie jak Robak mógł strzelić z daleka;
Ja zaś znałem drugiego: równie trafnym strzałem
Ocalił on dwóch panów; sam ja to widziałem,
Kiedy do nalibockich zaciągnęli lasów
Tadeusz Rejtan poseł i książę Denassów.
Nie zazdrościli sławie szlachcica panowie;
Owszem, u stołu pierwsi wnieśli jego zdrowie,
Nadawali mu wielkich prezentów bez liku,
I skórę zabitego dzika. O tym dziku
I o strzale, powiem wam jak naoczny świadek:
Bo to był dzisiejszemu podobny przypadek,
A zdarzył się największym strzelcom za mych czasów,
Posłowi Rejtanowi i księciu Denassów».

    A wtem ozwał się Sędzia nalewając czaszę:
«Piję zdrowie Robaka, Wojski, w ręce wasze!
Jeśli datkiem nie możem kwestarza zbogacić,
Postaramy się przecież za proch mu zapłacić:
Uręczamy, że niedźwiedź zabity dziś w boru
Przez dwa lata wystarczy na kuchnię klasztoru.
Lecz skóry księdzu nie dam: lub gwałtem zabiorę,
Albo ją mnich ustąpić musi przez pokorę,
Albo ją kupię choćby dziesiątkiem soboli.
Skórą tą rozrządzimy wedle naszej woli:
Pierwszy wieniec i sławę już wziął sługa boży;
Skórę jaśnie wielmożny pan nasz Podkomorzy
Temu da, kto na drugą nagrodę zasłużył».

    Podkomorzy pogładził czoło i brwi zmrużył;
Strzelcy zaczęli szemrać, każdy coś powiadał:
Tamten jak źwierza znalazł, ten jak ranę zadał,
Tamten psiarnię zawołał, ów źwierza nawrócił
Znowu w ostęp. Asesor z Rejentem się kłócił,
Jeden wielbiąc przymioty swojej Sanguszkówki,
Drugi bałabanowskiej swej Sagalasówki.

    «Sędzio sąsiedzie — wreszcie wyrzekł Podkomorzy —
Pierwszą nagrodę słusznie zyskał sługa boży;
Lecz niełacno rozsądzić, kto jest po nim drugi,
Bo wszyscy zdają mi się mieć równe zasługi,
Wszyscy równi zręcznością, biegłością i męstwem.
Przecież dwóch dziś odznaczył los niebezpieczeństwem.
Dwaj byli niedźwiedziego najbliżsi pazura:
Tadeusz i pan Hrabia; im należy skóra.
Pan Tadeusz ustąpi (jestem tego pewny),
Jako młodszy i jako gospodarza krewny;
Więc spolia opima weźmiesz, mości Hrabia:
Niech ten łup twą strzelecką komnatę ozdabia,
Niechaj pamiątką będzie dzisiejszej zabawy,
Godłem szczęścia łowczego, bodźcem przyszłej sławy».

    Umilknął wesół, myśląc, że Hrabię ucieszył;
Nie wiedział, jak boleśnie serce jego przeszył.
Bo Hrabia, na strzeleckiej komnaty wspomnienie,
Mimowolnie wzrok podniósł: a te łby jelenie,
Te gałęziste rogi, jakby las wawrzynów
Zasiany ręką ojców na wieńce dla synów,
Te rzędami portretów zdobione filary,
Ten w sklepieniu błyszczący herb Półkozic stary,
Ozwały się doń zewsząd głosami przeszłości.
Zbudził się z marzeń, wspomniał gdzie, u kogo gości:
Dziedzic Horeszków, gościem śród swych własnych progów,
Biesiadnikiem Sopliców, swych odwiecznych wrogów!
A przy tym zawiść, którą czuł dla Tadeusza,
Tym mocniej Hrabię przeciw Soplicom porusza.

    Rzekł więc z gorzkim uśmiechem: «Mój domek zbyt mały,
Nie ma godnego miejsca na dar tak wspaniały;
Niech lepiej niedźwiedź czeka pośród tych rogaczy,
Aż mi go Sędzia razem z zamkiem oddać raczy».

    Podkomorzy zgadując, na co się zanosi,
Zadzwonił w tabakierkę złotą, o głos prosi.
«Godzieneś pochwał — rzecze — Hrabio, mój sąsiedzie,
Że dbasz o interesa nawet przy obiedzie,
Nie tak jak modni wieku twojego panicze,
Żyjący bez rachunku. Ja tuszę i życzę
Zgodą zakończyć moje sądy podkomorskie.
Dotąd jedyna trudność jest o fundum dworskie:
Mam już projekt zamiany, fundum wynagrodzić
Ziemią, w sposób następny…» Tu zaczął wywodzić
Porządnie (jak zwykł zawsze) plan przyszłej zamiany.
Już był w połowie rzeczy: gdy ruch niespodziany
Wszczął się na końcu stoła. Jedni coś postrzegli,
Wskazują palcem; drudzy oczyma tam biegli,
Aż wreszcie wszystkie głowy, jak kłosy schylone
Wstecznym wiatrem, w przeciwną zwróciły się stronę
W kąt.

                        Z kąta, kędy wisiał portret nieboszczyka,
Ostatniego z rodziny Horeszków Stolnika,
Z małych drzwiczek, ukrytych pomiędzy filary,
Wysunęła się cicho postać, na kształt mary:
Gerwazy; poznano go po wzroście, po licach,
Po srebrzystych na żółtej kurcie Półkozicach.
Stąpał jako słup prosto, niemy i surowy,
Nie zdjąwszy czapki, nawet nie schyliwszy głowy;
W ręku trzymał błyszczący klucz jakby puginał,
Odemknął szafę i w niej coś kręcić zaczynał.

    Stały w dwóch kątach sieni, wsparte o filary,
Dwa kurantowe, w szafach zamknięte zegary;
Dziwaki stare, dawno ze słońcem w niezgodzie,
Południe wskazywały często o zachodzie.
Gerwazy nie przybrał się machiny naprawić,
Ale bez nakręcenia nie chciał jej zostawić:
Dręczył kluczem zegary każdego wieczora;
Właśnie teraz przypadła nakręcania pora.
Gdy Podkomorzy sprawą zajmował uwagę
Stron interesowanych, on pociągnął wagę:
Zgrzytnęły wyszczerbionym zębem koła rdzawe,
Wzdrygnął się Podkomorzy i przerwał rozprawę.
«Bracie — rzekł — odłóż nieco twą pilną robotę»
I kończył plan zamiany. Lecz Klucznik na psotę
Jeszcze silniej pociągnął drugiego ciężaru;
I wnet gil, który siedział na wierzchu zegaru,
Trzepiocąc skrzydłem zaczął ciąć kurantów nuty.
Ptak sztucznie wyrobiony, szkoda, że zepsuty,
Ząjąkał się i piszczał, im dalej, tym gorzéj.
Goście w śmiech; musiał przerwać znowu Podkomorzy.
«Mości Kluczniku — krzyknął — lub raczej puszczyku,
Jeśli dziób twój szanujesz, dość mi tego krzyku».

    Ale Gerwazy groźbą wcale się nie strwożył;
Prawą rękę poważnie na zegar położył,
A lewą wziął się pod bok. Tak oburącz wsparty,
«Podkomorzeńku! — krzyknął — wolne pańskie żarty,
Wróbel mniejszy niż puszczyk, a na swoich wiorach
Śmielszy jest aniżeli puszczyk w cudzych dworach:
Co Klucznik to nie puszczyk; kto w cudze poddasze
Nocą włazi, ten puszczyk, i ja go wystraszę».
«Za drzwi z nim!» Podkomorzy krzyknął.

                        «Panie Hrabia! —
Zawołał Klucznik — widzisz pan, co się wyrabia.
Czy nie dosyć się jeszcze pański honor plami,
Że pan jadasz i pijasz z tymi Soplicami;
Trzebaż jeszcze, aby mnie, zamku urzędnika,
Gerwazego Rembajłę, Horeszków Klucznika,
Lżyć w domu panów moich? i panże to zniesie!»
Wtem Protazy zawołał trzykroć: «Uciszcie się!
Na ustęp! Ja, Protazy Baltazar Brzechalski,
Dwojga imion, generał niegdyś trybunalski,
Vulgo Woźny, woźnieńską obdukcyją robię
I wizyją formalną, zamawiając sobie
Urodzonych tu wszystkich obecnych świadectwo,
I pana Asesora wzywając na śledztwo,
Z powodu wielmożnego Sędziego Soplicy:
O inkursyją, to jest o najazd granicy,
Gwałt zamku, w którym Sędzia dotąd prawnie włada,
Czego dowodem jawnym jest, że w zamku jada».
«Brzechaczu! — wrzasnął Klucznik — ja cię wnet nauczę!»
I dobywszy zza pasa swe żelazne klucze,
Okręcił wkoło głowy, puścił z całej mocy.
Pęk żelaza wyleciał jako kamień z procy,
Pewnie łeb Protazemu rozbiłby na ćwierci;
Szczęściem, schylił się Woźny i wydarł się śmierci.

    Porwali się z miejsc wszyscy; chwilę była głucha
Cichość, aż Sędzia krzyknął: «W dyby tego zucha!
Hola, chłopcy!» — i czeladź rzuciła się żwawo
Ciasnym przejściem pomiędzy ścianami i ławą.
Lecz Hrabia krzesłem w środku zagrodził im drogę
I na tym szańcu słabym utwierdziwszy nogę,
«Wara! — zawołał — Sędzio! nie wolno nikomu
Krzywdzić sługę mojego w moim własnym domu:
Kto ma na starca skargę, niech mi ją przełoży».

    Zyzem w oczy Hrabiemu spojrzał Podkomorzy:
«Bez waścinej pomocy ukarać potrafię
Zuchwałego szlachetkę; a waść, mości grafie,
Przed dekretem ten zamek za wcześnie przywłaszczasz:
Nie wać tu jesteś panem, nie wać nas ugaszczasz.
Siedź cicho, jakeś siedział; jeśli siwej głowy
Nie czcisz, to szanuj pierwszy urząd powiatowy».

    «Co mi? — odmruknął Hrabia — dość już tej gawędy;
Nudźcie drugich waszymi względy i urzędy!
Dość już głupstwa zrobiłem, wdając się z waćpaństwem
W pijatyki, które się kończą grubijaństwem;
Zdacie mi sprawę z mego honoru obrazy.
Do widzenia po trzeźwu; pójdź za mną, Gerwazy!»

    Nigdy się odpowiedzi takiej nie spodziewał
Podkomorzy. Właśnie swój kieliszek nalewał;
Gdy zuchwalstwem Hrabiego rażony jak gromem,
Oparłszy się o kielich butlem nieruchomym,
Głowę wyciągnął na bok i ucha przyłożył,
Oczy rozwarł szeroko, usta wpół otworzył;
Milczał, lecz kielich w ręku tak potężnie cisnął,
Że szkło dźwięknąwszy pękło, płyn w oczy mu prysnął.
Rzekłbyś, że z winem ognia w duszę się nalało:
Tak oblicze spłonęło, tak oko pałało.
Zerwał się mówić; pierwsze słowo niewyraźnie
Mleł w ustach; aż przez zęby wyleciało: «Błaźnie!
Grafiątko! ja cię! Tomasz, karabelę! Ja tu
Nauczę ciebie mores, błaźnie, daj go katu!
Względy, urzędy nudzą, uszko delikatne!
Ja cię tu zaraz po tych zauszniczkach płatnę.
Fora za drzwi! Do korda! Tomasz, karabelę!»

    Wtem do Podkomorzego skoczą przyjaciele;
Sędzia porwał mu rękę: «Stój pan, to rzecz nasza,
Mnie tu naprzód wyzwano. Protazy, pałasza!
Puszczę go w taniec jako niedźwiadka na kiju».
Lecz Tadeusz Sędziego wstrzymał: «Panie stryju,
Wielmożny Podkomorzy, czyż się państwu godzi
Wdawać się z tym fircykiem; czy tu nie ma młodzi?
Na mnie to zdajcie: ja go należycie skarcę.
A waszeć, panie śmiałku, co wyzywasz starce,
Obaczym, czyli jesteś tak strasznym rycerzem:
Rozprawimy się jutro, plac i broń wybierzem;
Dziś uchodź, pókiś cały».

                        Dobra była rada:
Klucznik i Hrabia wpadli w obroty nie lada.
Przy wyższym końcu stoła wrzał tylko krzyk wielki,
Ale z ostrego końca latały butelki
Koło Hrabiego głowy. Strwożone kobiety
W prośby, w płacz; Telimena, krzyknąwszy: «Niestety!»
Wzniosła oczy, powstała, i padła zemdlona,
I przechyliwszy szyję przez Hrabi ramiona,
Na pierś jego złożyła swe piersi łabędzie.
Hrabia, choć zagniewany, wstrzymał się w zapędzie,
Zaczął cucić, ocierać.

                        Tymczasem Gerwazy,
Wystawiony na stołków i butelek razy,
Już zachwiał się, już czeladź zakasawszy pięście
Rzucała się nań zewsząd hurmem: gdy na szczęście
Zosia, widząc szturm, skoczy, i litością zdjęta
Zasłania starca, na krzyż rozpiąwszy rączęta.
Wstrzymali się; Gerwazy z wolna ustępował,
Zniknął z oczu, szukano, gdzie się pod stół schował:
Gdy nagle, z drugiej strony, wyszedł jak spod ziemi,
Podniósłszy w górę ławę ramiony silnemi,
Okręcił się jak wiatrak, oczyścił pół sieni,
Wziął Hrabię; i tak oba, ławą zasłonieni,
Cofali się ku drzwiczkom; już dochodzą progów:
Gerwazy stanął, jeszcze raz spojrzał na wrogów.
Dumał chwilę, niepewny, czy cofać się zbrojnie,
Czyli z nowym orężem szukać szczęścia w wojnie:
Obrał drugie. Już ławę jak taran murowy
W tył dźwignął dla zamachu; już ugiąwszy głowy,
Z wypiętą na przód piersią, z podniesioną nogą,
Miał wpaść… ujrzał Wojskiego, uczuł w sercu trwogę.

    Wojski, cicho siedzący z przymrużonym okiem,
Zdawał się pogrążony w dumaniu głębokiem.
Dopiero, gdy się Hrabia z Podkomorzym skłócił:
I Sędziemu pogroził, Wojski głowę zwrócił,
Zażył dwakroć tabaki i przetarł powieki.
Chociaż Wojski Sędziemu był krewny daleki,
Ale w gościnnym jego domu zamieszkały,
O zdrowie przyjaciela był niezmiernie dbały.
Przypatrywał się zatem z ciekawością walce;
Wyciągnął z lekka na stół rękę, dłoń i palce,
Położył nóż na dłoni, trzonkiem do paznokcia
Indeksu, a żelazem zwrócony do łokcia;
Potem rękę w tył nieco wychyloną kiwał,
Niby bawiąc się: lecz się w Hrabiego wpatrywał.

    Sztuka rzucania nożów, straszna w ręcznej bitwie,
Już była zaniedbana podówczas na Litwie,
Znajoma tylko starym; Klucznik jej próbował
Nieraz w zwadach karczemnych, Wojski w niej celował:
Widać z zamachu ręki, że silnie uderzy,
A z oczu łacno zgadnąć, że w Hrabiego mierzy
(Ostatniego z Horeszków, chociaż po kądzieli),
Mniej baczni młodzi ruchów starca nie pojęli:
Gerwazy zbladnął, ławą Hrabiego zakłada,
Cofa się ku drzwiom. «Łapaj!» krzyknęła gromada.

    Jako wilk, obskoczony znienacka przy ścierwie,
Rzuca się oślep w zgraję, co mu ucztę przerwie;
Już goni, ma ją szarpać: wtem śród psiego wrzasku
Trzasło ciche półkurcze; wilk zna je po trzasku,
Śledzi okiem, postrzega, że z tyłu, za charty,
Myśliwiec wpół schylony, na kolanie wsparty,
Rurą ku niemu wije i już cyngla tyka.
Wilk uszy spuszcza, ogon podtuliwszy, zmyka;
Psiarnia z tryumfującym rzuca się hałasem
I skubie go po kudłach; zwierz zwraca się czasem,
Spojrzy, klapnie paszczęką i białych kłów zgrzytem
Ledwie pogrozi; psiarnia pierzcha ze skowytem:
Tak i Gerwazy z groźną cofał się postawą,
Wstrzymując napastników oczyma i ławą,
Aż razem z Hrabią wpadli w głąb ciemnej framugi.

    «Łapaj!» krzykniono znowu. Tryumf był nie długi:
Bo nad głowami tłumu Klucznik niespodzianie
Ukazał się na chórze, przy starym organie,
I z trzaskiem jął wyrywać ołowiane rury.
Wielką by klęskę zadał, uderzając z góry:
Ale już goście tłumnie wychodzili z sieni;
Nie śmieli kroku dostać słudzy potrwożeni
I chwytając naczynia w ślad panów uciekli,
Nawet nakrycia z częścią sprzętów się wyrzekli.

    Któż ostatni, nie dbając na groźby i razy,
Ustąpił z placu bitwy? Brzechalski Protazy.
On, za krzesłem Sędziego stojąc niewzruszenie,
Ciągnął woźnieńskim głosem swoje oświadczenie,
Aż skończył i z pustego zszedł pobojowiska,
Kędy zostały trupy, ranni i zwaliska.

    W ludziach straty nie było. Ale wszystkie ławy
Miały zwichnione nogi; stół także kulawy,
Obnażony z obrusa, poległ na talerzach
Zlanych winem, jak rycerz na krwawych puklerzach,
Między licznymi kurcząt i jendyków ciały,
W których piersi widelce świeżo wbite tkwiały.

    Po chwili w Horeszkowskim samotnym budynku
Wszystko do zwyczajnego wracało spoczynku.
Mrok zgęstniał; reszty pańskiej wspaniałej biesiady
Leżą, podobne uczcie nocnej, gdzie na Dziady
Zgromadzać się zaklęte mają nieboszczyki.
Już na poddaszu trzykroć krzyknęły puszczyki
Jak guślarze: zdają się witać wschód miesiąca,
Którego postać oknem spadła na stół drżąca,
Niby dusza czyscowa; z podziemu, przez dziury,
Wyskakiwały na kształt potępieńców szczury:
Gryzą, piją; czasami w kącie zapomniana,
Puknie na toast duchom butelka szampana.

    Ale na drugim piętrze, w izbie, którą zwano,
Choć była bez zwierciadeł, salą zwierciadlaną
Stał Hrabia na krużganku zwróconym ku bramie,
Chłodził się wiatrem, surdut wdział na jedno ramię,
Drugi rękaw i poły u szyi sfałdował
I pierś surdutem, jakby płaszczem udrapował.
Gerwazy chodził kroki wielkimi po sali;
Obadwa zamyśleni, do siebie gadali:
«Pistolety — rzekł Hrabia — lub gdy chcą pałasze».
«Zamek — rzekł Klucznik — i wieś, oboje to nasze».
«Stryja, synowca — wołał Hrabia — całe plemię
Wyzywaj!» «Zamek — wołał Klucznik — wieś i ziemie
Zabieraj pan». To mówiąc, zwrócił się do Hrabi:
«Jeśli pan chce mieć pokój, niech wszystko zagrabi.
Po co proces, mopanku! sprawa jak dzień czysta:
Zamek w ręku Horeszków był przez lat czterysta;
Część gruntów oderwano w czasie Targowicy,
I jak pan wie, oddano władaniu Soplicy.
Nie tylko tę część, wszystko zabrać im należy,
Za koszta procesowe, za karę grabieży.
Mówiłem panu zawsze: procesów zaniechać;
Mówiłem panu zawsze: najechać, zajechać!
Tak było po dawnemu: kto raz grunt posiądzie,
Ten dziedzic; wygraj w polu, a wygrasz i w sądzie.
Co się tycze dawniejszych z Soplicami sprzeczek:
Jest na to od procesu lepszy Scyzoryczek;
A jeśli Maciej w pomoc da mi swą Rózeczkę,
To my we dwóch, Sopliców tych porzniem na sieczkę».

    «Brawo! — rzekł Hrabia — plan twój, gotycko-sarmacki
Podoba się mi lepiej niż spór adwokacki.
Wiesz co? na całej Litwie narobim hałasu
Wyprawą niesłychaną od dawnego czasu.
I sami się zabawim. Dwa lata tu siedzę,
Jakąż bitwę widziałem? z chłopami o miedzę!
Nasza wyprawa przecież krwi rozlanie wróży.
Odbyłem taką jedną w czasie mych podróży.
Gdym w Sycylii bawił u pewnego księcia,
Rozbójnicy porwali w górach jego zięcia,
I okupu od krewnych żądali zuchwale;
My, zebrawszy naprędce sługi i wasale,
Wpadliśmy; ja dwóch zbójców ręką mą zabiłem,
Pierwszy wleciałem w tabor, więźnia uwolniłem.
Ach, mój Gerwazy! jaki to był tryumfalny,
Jaki piękny nasz powrót, rycersko-feudalny!
Lud z kwiatami spotykał nas; córka książęcia,
Wdzięczna zbawcy, ze łzami padła w me objęcia.
Gdym przybył do Palermo, wiedziano z gazety,
Palcami wskazywały mię wszystkie kobiety;
Nawet wydrukowano o całym zdarzeniu
Romans, gdzie wymieniony jestem po imieniu.
Romans ma tytuł: Polak, czyli tajemnice
Zamku Birbante-rokka. Czy są tu ciemnice
W tym zamku?» «Są — rzekł Klucznik — ogromne piwnice,
Ale puste! bo wino wypili Soplice».
«Dżokejów — dodał Hrabia — uzbroić we dworze,
Z włości wezwać wasalów!» «Lokajów? broń Boże! —
Przerwał Gerwazy. Czy to zajazd jest hultajstwem?
Kto widział zajazd robić z chłopstwem i z lokajstwem?
Mój panie, na zajazdach nie znacie się wcale!
Wąsalów, co innego: zdadzą się wąsale;
Nie we włości ich szukać, ale po zaściankach,
W Dobrzynie, w Rzezikowie, w Ciętyczach, w Rąbankach,
Szlachta odwieczna, w której krew rycerska płynie,
Wszyscy przychylni panów Horeszków rodzinie,
Wszyscy nieprzyjaciele zabici Sopliców!
Stamtąd zbiorę ze trzystu wąsatych szlachciców;
To rzecz moja. Pan niechaj do pałacu wraca
I wyśpi się, bo jutro będzie wielka praca;
Pan spać lubi, już późno, drugi kur już pieje.
Ja tu będę pilnować zamku, aż rozdnieje,
A ze słoneczkiem stanę w Dobrzyńskim zaścianku».

    Na te słowa pan Hrabia ustąpił z krużganku;
Ale nim odszedł, spojrzał przez otwór strzelnicy,
I widząc świateł mnóstwo w domostwie Soplicy:
«Iluminujcie! — krzyknął — jutro o tej porze
Będzie jasno w tym zamku, ciemno w waszym dworze!»

    Gerwazy siadł na ziemi, oparł się o ścianę,
I pochylił ku piersiom czoło zadumane.
Światłość miesięczna padła na wierzch głowy łysy,
Gerwazy po nim kryślił palcem różne rysy;
Widać, że przyszłych wypraw snuł plany wojenne.
Ciążą mu coraz bardziej powieki brzemienne,
Bezwładną kiwnął szyją, czuł, że go sen bierze,
Zaczął wedle zwyczaju wieczorne pacierze.
Lecz między Ojczenaszem i Zdrowaś Maryją,
Dziwne stanęły mary, tłoczą się i wiją:
Klucznik widzi Horeszki, swoje dawne pany;
Ci niosą karabele, drudzy buzdygany,
Każdy groźnie spoziera i pokręca wąsa,
Składa się karabelą, buzdyganem wstrząsa;
Za nimi jeden cichy, posępny cień mignął,
Z krwawą na piersi plamą. Gerwazy się wzdrygnął,
Poznał Stolnika; zaczął wkoło siebie żegnać,
I ażeby tym pewniej straszne sny rozegnać,
Odmawiał litaniją o czyscowych duszach.
Znowu wzrok mu skleił się, zadzwoniło w uszach —
Widzi tłum szlachty konnej, błyszczą karabele:
Zajazd! zajazd Korelicz i Rymsza na czele!
I ogląda sam siebie, jak na koniu siwym,
Z podniesionym nad głową rapierem straszliwym
Leci; rozpięta na wiatr szumi taratatka,
Z lewego ucha spadła w tył konfederatka;
Leci, jezdnych i pieszych po drodze obala,
I na koniec Soplicę w stodole podpala.
Wtem ciężka marzeniami na pierś spadła głowa,
I tak usnął ostatni Klucznik Horeszkowa.




Księga szósta



Zaścianek

Pierwsze ruchy wojenne zajazdu — Wyprawa Protazego — Robak z panem Sędzią radzą o rzeczy publicznej — Dalszy ciąg wyprawy Protazego bezskutecznej — Ustęp o konopiach — Zaścianek szlachecki Dobrzyn — Opisanie domostwa i osoby Maćka Dobrzyńskiego.

    Nieznacznie z wilgotnego wykradał się mroku
Świt bez rumieńca, wiodąc dzień bez światła w oku.
Dawno wszedł dzień, a jeszcze ledwie jest widomy:
Mgła wisiała nad ziemią, jak strzecha ze słomy
Nad ubogą Litwina chatką; w stronie wschodu,
Widać z bielszego nieco na niebie obwodu
Że słońce wstało, tędy ma zstąpić na ziemię;
Lecz idzie niewesoło i po drodze drzemie.

    Za przykładem niebieskim, wszystko się spóźniło
Na ziemi. Bydło późno na paszę ruszyło
I zdybało zające przy późnym śniadaniu.
One zwykły do gajów wracać o świtaniu;
Dziś, okryte tumanem, te mokrzycę chrupią,
Te jamki w roli kopiąc, parami się kupią,
I na wolnym powietrzu myślą użyć wczasu;
Ale przed bydłem muszą powracać do lasu.

    I w lasach cisza. Ptaszek zbudzony nie śpiewa;
Otrząsnął pierze z rosy, tuli się do drzewa,
Głowę wciska w ramiona, oczy znowu mruży
I czeka słońca. Kędyś, u brzegów kałuży,
Klekce bocian. Na kopach siedzą wrony zmokłe,
Rozdziawiwszy się ciągną gawędy rozwlokłe;
Obrzydłe gospodarzom jako wróżby słoty.
Gospodarze już dawno wyszli do roboty.

    Już zaczęły żniwiarki swą piosnkę zwyczajną,
Jak dzień słotny ponurą, tęskną, jednostajną,
Tym smutniejszą, że dźwięk jej w mgłę bez echa wsiąka.
Chrząsnęły sierpy w zbożu, ozwała się łąka,
Rząd kosiarzy otawę siekących wciąż brząka,
Pogwizdując piosenkę; z końcem każdej zwrotki
Stają, ostrzą żelezca i w takt kują w młotki.
Ludzi we mgle nie widać: tylko sierpy, kosy
I pieśni brzmią, jak muzyk niewidzialnych głosy.

    W środku, na snopie zboża Ekonom usiadłszy
Nudzi się, kręci głową, roboty nie patrzy,
Pogląda na gościniec, na drogi rozstajne,
Kędy działy się jakieś rzeczy nadzwyczajne.

    Na gościńcu i drogach od samego ranka
Panuje ruch niezwykły. Stąd chłopska furmanka
Skrzypi, lecąc jak poczta; stąd szlachecka bryka
Cwałem tarkoce, drugą i trzecią spotyka;
Z lewej drogi posłaniec jak kuryjer goni,
Z prawej przebiegło w zawód kilkanaście koni:
Wszyscy śpieszą, ku różnym kierują się stronom.
Co to ma znaczyć? Powstał ze snopa Ekonom,
Chciał przypatrzyć się, spytać; długo stał nad drogą,
Daremnie wołał, nie mógł zatrzymać nikogo
Ni poznać we mgle. Jezdni migają jak duchy;
Tylko słychać raz po raz tętent kopyt głuchy
I, co dziwniejsza jeszcze, szczękanie pałaszy:
Bardzo to Ekonoma i cieszy, i straszy.
Bo choć na Litwie było naonczas spokojnie,
Dawno już wieści głuche biegały o wojnie,
O Francuzach, Dąbrowskim, o Napoleonie.
Miałyżby wojnę wróżyć ci jeźdźcy? te bronie?
Ekonom pobiegł wszystko Sędziemu powiedzieć,
Spodziewając się i sam czegoś się dowiedzieć.

    W Soplicowie domowi i goście, po kłótni
Wczorajszej, wstali z siebie nieradzi i smutni.
Próżno Wojszczanka damy na kabałę sprasza,
Mężczyznom próżno karty dają do mariasza:
Nie chcą bawić się, ni grać, siedzą, cicho w kątkach,
Mężczyźni palą lulki, kobiety przy prątkach;
Nawet śpią muchy.

                        Wojski, rzuciwszy łopatkę,
Znudzony ciszą, idzie pomiędzy czeladkę;
Woli w kuchennej słuchać ochmistrzyni krzyków,
Gróźb i razów kucharza, hałasu kuchcików:
Aż go powoli wprawił w przyjemne marzenie,
Ruch jednostajny rożnów kręcących pieczenie.

    Sędzia od rana pisał, zamknąwszy się w izbie;
Woźny od rana czekał pod oknem na przyzbie.
Sędzia, skończywszy pozew, Protazego wzywa,
Skargę przeciw Hrabiemu głośno odczytywa:
O skrzywdzenie honoru, zelżywe wyrazy,
Zaś przeciw Gerwazemu o gwałty i razy;
Obudwu, o przechwałki, o koszta z powodu
Procesu, ciągnie w rejestr taktowy do grodu.
Pozew dziś trzeba wręczyć ustnie, oczywisto,
Nim zajdzie słońce. Woźny z miną uroczystą
Wyciągnął słuch i rękę, skoro pozew zoczył;
Stał poważnie, a rad by z radości podskoczył.
Na samą myśl procesu czuł, że się odmłodził:
Wspomniał na dawne lata, gdy z pozwami chodził
Po guzy, ale razem po zapłaty hojne.
Tak żołnierz, który strawił życie tocząc wojnę,
A na starość w szpitalach spoczywa kaleki:
Skoro usłyszy trąbę lub bęben daleki,
Chwyta się z łoża, krzyczy przez sen: «Bij Moskala!»
I na drewnianej nodze skacze ze szpitala,
Tak prędko, że go ledwie może złowić młodzież.

    Protazy śpieszył włożyć swą woźnieńską odzież.
Przecież żupana ani kontusza nie kładzie:
One służą ku wielkiej sądowej paradzie;
Na podróż ma strój inny: szerokie rajtuzy
I kurtkę, której poły podpięte na guzy
Można zakasać albo spuścić na kolana;
Czapka z uszami, sznurkiem u wierzchu związana,
Wznosi się na pogodę, spuszcza się przed słotą.
Tak ubrany wziął pałkę i ruszył piechotą;
Bo woźni przed procesem, jak szpiegi przed bojem,
Muszą kryć się pod różną postacią i strojem.

    Dobrze zrobił Protazy, że w drogę pośpieszył,
Bo niedługo by swoim pozwem się nacieszył:
W Soplicowie zmieniano kampanii plany.
Do Sędziego wpadł nagle Robak zadumany,
I rzekł: «Sędzio, to bieda nam z tą panią ciotką,
Z tą panią Telimeną, kokietką i trzpiotką!
Kiedy Zosia została dzieckiem w biednym stanie,
Jacek ją Telimenie dał na wychowanie,
Słysząc, że jest osoba dobra, świat znająca:
A postrzegam, że ona coś tu nam zamąca,
Intryguje i pono Tadeuszka wabi:
Śledzę ją; albo może bierze się do Hrabi;
Może do obu razem. Obmyślmy więc środki,
Jak się jej pozbyć: bo stąd mogą urość plotki,
Zły przykład i pomiędzy młokosami zwady,
Które mogą pomieszać twe prawne układy».
«Układy? — krzyknął Sędzia z niezwykłym zapałem —
Z układów kwita, już je skończyłem, zerwałem».
«A to co? — przerwał Robak — gdzie rozum, gdzie głowa?
Co tu mi wasze bajesz, jaka burda nowa?»
«Nie z mej winy — rzekł Sędzia — proces to wyjaśni:
Hrabia pyszałek, głupiec, był przyczyną waśni,
I Gerwazy łotr. Lecz to do sądu należy.
Szkoda, żeś nie był, księże, w zamku na wieczerzy,
Poświadczyłbyś, jak Hrabia srodze mnie obraził».
«Po coś waść — krzyknął Robak — do tych ruin łaził?
Wiesz, jak zamku nie cierpię; odtąd moja noga
Tam nie postanie. Znowu kłótnia! kara Boga!
Jakże tam było? powiedz; trzeba tę rzecz zatrzeć.
Już mię znudziło wreszcie na tyle głupstw patrzeć:
Ważniejsze ja mam sprawy niż godzić pieniaczy;
Ale jeszcze raz zgodzę». «Zgodzić? Cóż to znaczy!
A idźże mi waść wreszcie z tą zgodą do licha! —
Przerwał Sędzia, tupnąwszy nogą — patrzcie mnicha!
Że go przyjmuję grzecznie, chce mnie za nos wodzić!
Wiedz wasze, że Soplice nie zwykli się godzić:
Gdy pozwą, muszą wygrać; nieraz w ich imieniu
Trwał proces, aż wygrali w szóstym pokoleniu.
Dosyć zrobiłem głupstwa z porady waszeci,
Zwołując podkomorskie sądy po raz trzeci.
Od dzisiaj nie ma zgody, nie ma, nie ma, nie ma! —
I krzycząc chodził, tupał nogami obiema —
Prócz tego za wczorajszy niegrzeczny uczynek
Musi mnie deprekować, albo pojedynek!»
«Ale Sędzio, cóż będzie, jak się Jacek dowie?
Wszak on umrze z rozpaczy! Czyliż Soplicowie
Nie narobili jeszcze w tym zamku dość złego?
Bracie! wspominać nie chcę wypadku strasznego…
Wiesz także, że część gruntów od zamku dziedzica
Zabrała i Soplicom dała Targowica…
Jacek, za grzech żałując, musiał był ślubować
Pod absolucją, dobra te restytuować:
Wziął więc Zosię, Horeszków dziedziczkę ubogą,
Hodować, wychowanie jej opłacał drogo;
Chciał ją Tadeuszkowi swojemu wyswatać
I tak dwa poróżnione domy znowu zbratać,
I dziedziczce bez wstydu ustąpić grabieży…»
«Lecz cóż to? — krzyknął Sędzia — co do mnie należy?
Ja się nie znałem, nawet nie widziałem z Jackiem;
Ledwiem słyszał o jego życiu hajdamackiem,
Siedząc wtenczas retorem w jezuickiej szkole,
Potem u Wojewody służąc za pacholę.
Dano mi dobra, wziąłem; kazał przyjąć Zosię,
Przyjąłem, hodowałem, myślę o jej losie:
Dość mnie nudzi ta cała historyja babia!
A potem, czegóż jeszcze wlazł mi tu ten Hrabia?
Z jakim prawem do zamku? Wszak wiesz przyjacielu,
On Horeszkom dziesiąta woda na kisielu!
I ma mnie lżyć? a ja go zapraszać do zgody!»
«Bracie! — rzekł ksiądz — ważne są do tego powody.
Pamiętasz, że Jacek chciał do wojska słać syna,
Potem w Litwie zostawił: cóż w tym za przyczyna?
Oto w domu ojczyźnie potrzebniejszy będzie.
Słyszałeś pewnie, o czym już gadają wszędzie,
O czym ja wiadomostki przynosiłem nieraz:
Teraz czas już powiedzieć wszystko, czas już teraz!
Ważne rzeczy, mój bracie! Wojna tuż nad nami!
Wojna o Polskę! bracie! Będziem Polakami!
Wojna niechybna! Kiedy z poselstwem tajemnem
Tu biegłem, wojsk forpoczty już stały nad Niemnem;
Napoleon już zbiera armiję ogromną,
Jakiej człowiek nie widział i dzieje nie pomną;
Obok Francuzów ciągnie polskie wojsko całe,
Nasz Józef, nasz Dąbrowski, nasze orły białe!
Już są w drodze; na pierwszy znak Napoleona
Przejdą Niemen i — bracie! Ojczyzna wskrzeszona!»

    Sędzia, słuchając, z wolna okulary składał
I, wpatrując się mocno w księdza, nic nie gadał,
Westchnął głęboko, w oczach łzy się zakręciły…
Wreszcie porwał za szyję księdza z całej siły,
«Mój Robaku! — wołając — czy to tylko prawda?
Mój Robaku! — powtarzał — czy to tylko prawda?
Ileż razy zwodzono! Pamiętasz? gadali:
Napoleon już idzie! i my już czekali!
Gadano: już w Koronie, już Prusaka pobił,
Wkracza do nas! A on! co? pokój w Tylży zrobił!
Czy tylko prawda? Czy ty nie zwodzisz sam siebie?»
«Prawda — zawołał Robak — jak Pan Bóg na niebie!»
«Błogosławioneż niechaj będą usta, które
To zwiastują! — rzekł Sędzia — wznosząc ręce w górę.
Nie pożałujesz twego poselstwa Robaku,
Nie pożałuje klasztor: dwieście owiec z braku
Daję na klasztor. Księże, tyś się wczoraj palił
Do mojego kasztanka i gniadosza chwalił:
Dziś, zaraz w tym kwestarskim wozie pójdą oba;
Dziś proś mnie, o co zechcesz, co ci się podoba,
Nie odmówię!… Lecz o tym interesie całym
Z Hrabią, daj pokój: skrzywdził mnie, już zapozwałem;
Czyż wypada?»

                        Załamał ręce ksiądz zdziwiony.
Wlepiwszy oczy w Sędzię, ruszywszy ramiony,
Rzekł : «To gdy Napoleon wolność Litwie niesie,
Gdy świat drży cały, to ty myślisz o procesie?
I jeszczeż po tym wszystkim, com tobie powiedział,
Będziesz spokojnie, ręce założywszy, siedział,
Gdy działać trzeba!» «Działać? Cóż?» Sędzia zapytał.
«Jeszcześ — rzekł Robak — z oczu moich nie wyczytał?
Jeszcze serce nic tobie nie gada? Ach bracie!
Jeśli Soplicowskiej krwi kroplę w żyłach macie,
Uważ tylko: Francuzi uderzają z przodu…
A gdyby z tyłu zrobić powstanie narodu?
Co myślisz? Niech no Pogoń zarży, niech na Żmudzi
Niedźwiedź ryknie! Ach, gdyby jakie tysiąc ludzi,
Gdyby choć pięćset z tyłu na Moskwę natarło,
Powstanie jako pożar wkoło rozpostarło,
Gdybyśmy my, nabrawszy Moskwie harmat, znaków,
Zwycięzcy szli powitać wybawców rodaków?…
Ciągniemy! Napoleon, widząc nasze lance,
Pyta, co to za wojsko; my krzyczym: »Powstańce,
Najjaśniejszy Cesarzu! Litwa ochotnicy!«
Pyta: pod czyją wodzą? — »Sędziego Soplicy!«
Ach, któż by potem pisnąć śmiał o Targowicy?…
Bracie, póki Ponarom stać, Niemnowi płynąć,
Póty w Litwie Sopliców imieniowi słynąć;
Wnuków, prawnuków będzie Jagiełłów stolica
Wskazywać palcem, mówiąc: oto jest Soplica,
Z tych Sopliców, co pierwsi zrobili powstanie!»

    A na to Sędzia: «Mniejsza o ludzkie gadanie;
Nigdy nie dbałem bardzo o pochwały świata:
Bóg świadkiem, żem niewinien grzechów mego brata;
W politykę jam nigdy bardzo się nie wdawał,
Urzędując i orząc mojej ziemi kawał.
Lecz jestem szlachcic, rad bym plamę domu zmazać;
Jestem Polak, dla kraju rad bym coś dokazać,
Choć duszę oddać. W szablę nie byłem zbyt tęgi;
Wszakże, bierali ludzie i ode mnie cięgi,
Wie świat, że w czasie polskich ostatnich sejmików
Wyzwałem i zraniłem dwóch braci Buzwików,
Którzy… Ale to mniejsza. Jakże wasze myśli?
Czy potrzeba, żebyśmy zaraz w pole wyszli?
Strzelców zebrać, rzecz łatwa; prochu mam dostatek;
W plebanii u księdza jest kilka armatek;
Przypominam, iż Jankiel mówił, iż u siebie
Ma groty do lanc, że je mogę wziąć w potrzebie;
Te groty przywiózł w pakach gotowych z Królewca
Pod sekretem; weźmiem je, zaraz zrobim drzewca;
Szabel nam nie zabraknie; szlachta na koń wsiędzie,
Ja z synowcem na czele, i — jakoś to będzie!»

    «O polska krwi! — zawołał Bernardyn wzruszony,
Z otwartymi skoczywszy na Sędzię ramiony —
Prawe dziecię Sopliców! Tobie Bóg przeznacza
Oczyścić grzechy brata twojego tułacza!
Zawszem ciebie szanował; ale od tej chwili
Kocham cię, jak gdybyśmy bracią sobie byli!…
Przygotujemy wszystko; lecz wyjść nie czas jeszcze:
Ja sam wyznaczę miejsce i czas wam obwieszczę.
Wiem, że car wysiał gońców do Napoleona
Prosić o pokój; wojna nie jest ogłoszona:
Lecz książę Józef słyszał od pana Biniona,
Francuza, co należy do cesarskiej rady,
Że się na niczym skończą wszystkie te układy,
Że będzie wojna. Książę wysłał mnie na zwiady,
Z rozkazem, żeby byli Litwini gotowi
Dowieść przychodzącemu Napoleonowi,
Że chcą złączyć się znowu z siostrą swą, Koroną,
I żądają, ażeby Polskę przywrócono.
Tymczasem, bracie, z Hrabią trzeba przyjść do zgody.
Jest to dziwak, fantastyk trochę, ale młody,
Poczciwy, dobry Polak: potrzebny nam taki.
W rewolucyjach bardzo potrzebne dziwaki:
Wiem z doświadczenia; nawet głupi się przydadzą,
Byle tylko poczciwi i pod mądrych władzą.
Hrabia pan, ma u szlachty wielkie zachowanie,
Cały powiat ruszy się, jeśli on powstanie;
Znając jego majątek, każdy szlachcic powie:
Musi to być rzecz pewna, gdy z nią są panowie.
Biegę do niego zaraz…» «Niech się pierwszy zgłosi —
Rzekł Sędzia — niech przyjedzie tu, niech mnie przeprosi;
Wszak jestem starszy wiekiem, jestem na urzędzie!
Co się tycze procesu, sąd arbitrów będzie…»
Bernardyn trzasnął drzwiami. «No, szczęśliwa droga!»
Rzekł Sędzia.

                        Ksiądz wpadł w powóz stojący u proga,
Tnie biczem konie, łechce lejcami po bokach;
Furknęła kałamaszka, ginie w mgły obłokach;
Tylko kiedy niekiedy kaptur mnicha bury
Wznosi się nad tumany jako sęp nad chmury.

    Woźny już dawniej wyszedł ku domowi Hrabi.
Jak lis bywalec, gdy go woń słoniny wabi,
Bieży ku niej, a strzelców zna fortele skryte,
Bieży, staje, przysiada coraz, wznosi kitę
I wiatr nią jak wachlarzem ku swym nozdrzom tuli,
Pyta wiatru, czy strzelcy jadła nie zatruli:
Protazy zeszedł z drogi i wzdłuż sianożęci
Krąży około domu; pałkę w ręku kręci,
Udaje, że obaczył kędyś bydło w szkodzie.
Tak zręcznie lawirując, stanął przy ogrodzie;
Schylił się, bieży, rzekłbyś iż derkacza tropi:
Aż nagle skoczył przez płot i wpadł do konopi.

    W tej zielonej, pachnącej i gęstej krzewinie
Koło domu jest pewny przytułek źwierzynie
I ludziom. Nieraz zając zdybany w kapuście
Skacze skryć się w konopiach bezpieczniej niż w chruście:
Bo go dla gęstwi ziela ani chart nie zgoni,
Ani ogar wywietrzy dla zbyt tęgiej woni.
W konopiach człowiek dworski, uchodząc kańczuka
Lub pięści, siedzi cicho, aż się pan wyfuka.
I nawet często zbiegli od rekruta chłopi,
Gdy ich rząd śledzi w lasach, siedzą śród konopi.
I stąd to w czasie bitew, zajazdów, tradowań,
Obie strony nie szczędzą wielkich usiłowań,
Ażeby stanowisko zająć konopiane,
Które z przodu ciągnie się aż pod dworską ścianę,
A z tyłu, pospolicie stykając się z chmielem,
Kryje atak i odwrót przed nieprzyjacielem.

    Protazy, choć człek śmiały, uczuł nieco strachu:
Bo przypomniał z samego rośliny zapachu
Różne swoje dawniejsze woźnieńskie przypadki,
Jedne po drugich, biorąc konopie na świadki:
Jako raz zapozwany szlachcic z Telsz, Dzindolet,
Rozkazał mu, oparłszy o piersi pistolet,
Wleźć pod stół i ów pozew psim głosem odszczekać,
Że Woźny musiał co tchu w konopie uciekać.
Jak później Wołodkowicz, pan dumny, zuchwały,
Co rozpędzał sejmiki, gwałcił trybunały,
Przyjąwszy urzędowy pozew, zdarł na sztuki,
I postawiwszy przy drzwiach z kijami hajduki,
Sam nad Woźnego głową trzymał goły rapier,
Krzycząc: «Albo cię zetnę, albo zjedz twój papier!»
Woźny niby jeść zaczął, jak człowiek roztropny,
Aż skradłszy się do okna, wpadł w ogród konopny.

    Wprawdzie już wtenczas w Litwie nie było zwyczajem
Opędzać się od pozwów szablą lub nahajem,
I ledwie Woźny czasem usłyszał łajanie:
Ale Protazy o tej obyczajów zmianie
Wiedzieć nie mógł, bo dawno już pozwów nie naszał.
Choć zawsze gotów, choć się Sędziemu sam wpraszał,
Sędzia dotąd, przez winny wzgląd na lata stare,
Odmawiał jego prośbom; dziś przyjął ofiarę,
Dla naglącej potrzeby.

                        Woźny patrzy, czuwa:
Cicho wszędzie; w konopie z wolna ręce wsuwa,
I rozchylając gęstwę badylów, w jarzynie
Jako rybak pod wodą nurkujący płynie;
Wzniósł głowę: cicho wszędzie; do okien się skrada:
Cicho wszędzie; przez okna głąb pałacu bada:
Pusto wszędzie; na ganek wchodzi nie bez strachu,
Odmyka klamkę i pusto jak w zaklętym gmachu;
Dobywa pozew, czyta głośno oświadczenie.
A wtem usłyszał turkot, uczuł serca drżenie,
Chciał uciec… gdy ode drzwi zaszła mu osoba:
Szczęściem znajoma! Robak! Zdziwili się oba.

    Widno, że Hrabia kędyś ruszył z całym dworem,
I bardzo śpieszył, bo drzwi zostawił otworem.
Widać, że się uzbrajał: leżały dwururki
I sztućce na podłodze, dalej sztenfle, kurki,
I narzędzia ślusarskie, którymi rynsztunki
Poprawiano; proch, papier: robiono ładunki.
Czy Hrabia z całym dworem wyjechał na łowy?
Ale po cóż broń ręczna? Tu szabla bez głowy
Zardzewiała, tam leży szpada bez temlaku:
Zapewne wybierano oręż z tego braku,
I poruszono nawet stare broni składy.
Robak obejrzał pilnie rusznice i szpady,
A potem do folwarku wybrał się na zwiady,
Szukając sług, żeby się rozpytać o Hrabię.
W pustym folwarku ledwie wynalazł dwie babie,
Od których słyszy, że pan i dworska drużyna
Ruszyli tłumnie, zbrojnie, drogą do Dobrzyna.

    Słynie szeroko w Litwie Dobrzyński zaścianek
Męstwem swoich szlachciców, pięknością szlachcianek.
Niegdyś możny i ludny: bo gdy król Jan Trzeci
Obwołał pospolite ruszenie przez wici,
Chorąży województwa z samego Dobrzyna
Przywiódł mu sześćset zbrojnej szlachty. Dziś rodzina
Zmniejszona, zubożała. Dawniej w pańskich dworach
Lub wojsku, na zajazdach, sejmikowych zborach,
Zwykli byli Dobrzyńscy żyć o łatwym chlebie:
Teraz, zmuszeni sami pracować na siebie
Jako zaciężne chłopstwo! tylko że siermięgi
Nie noszą, lecz kapoty białe w czarne pręgi,
A w niedzielę kontusze. Strój także szlachcianek
Najuboższych różni się od chłopskich katanek:
Zwykle chodzą w drylichach albo perkaliczkach,
Bydło pasą nie w łapciach z kory, lecz w trzewiczkach,
I żną zboże, a nawet przędzą w rękawiczkach.

    Różnili się Dobrzyńscy między Litwą bracią
Językiem swoim, tudzież wzrostem i postacią.
Czysta krew lacka, wszyscy mieli czarne włosy,
Wysokie czoła, czarne oczy, orle nosy;
Z Dobrzyńskiej ziemi ród swój starożytny wiedli,
A choć od lat czterystu na Litwie osiedli,
Zachowali mazurską mowę i zwyczaje.
Jeśli który z nich dziecku imię na chrzcie daje,
Zawsze zwykł za patrona brać koronijasza;
Świętego Bartłomieja albo Matyjasza:
Tak Syn Macieja zawżdy zwał się Bartłomiejem,
A znowu Bartłomieja syn zwał się Maciejem:
Kobiety wszystkie chrzczono Kachny lub Maryny.
By rozeznać się wpośród takiej mieszaniny,
Brali różne przydomki od jakiej zalety
Lub wady, tak mężczyźni jako i kobiety.
Mężczyznom czasem kilka dawano przydomków,
Na znak pogardy albo szacunku spółziomków;
Czasem jedenże szlachcic inaczej w Dobrzynie,
A pod innym nazwiskiem u sąsiadów słynie;
Dobrzyńskich naśladując, inna szlachta bliska
Brała również przydomki, zwane *imioniska*.
Teraz ich każda prawie używa rodzina,
A rzadki wie, iż mają początek z Dobrzyna,
I były tam potrzebne: kiedy w reszcie kraju
Głupim naśladownictwem weszły do zwyczaju.

    Więc Matyjasz Dobrzyński, który stał na czele
Całej rodziny, zwan był *Kurkiem na kościele*;
Potem, z siedemset dziewięćdziesiąt czwartym rokiem
Odmieniwszy przydomek, ochrzcił się *Zabokiem*;
Toż *Królikiem* Dobrzyńscy mianują go sami,
A Litwini nazwali *Maćkiem nad Maćkami*.

    Jak on nad Dobrzyńskimi, dom jego nad siołem
Panował, stojąc między karczmą i kościołem.
Widać rzadko zwiedzany, mieszka w nim hołota:
Bo brama sterczy bez wrót, ogrody bez płota,
Niezasiane, na grzędach już porosły brzozki;
Przecież ten folwark zdał się być stolicą wioski,
Iż kształtniejszy od innych chat, bardziej rozległy,
I prawą stronę, gdzie jest świetlica, miał z cegły.
Obok lamus, spichrz, gumno, obora i stajnie,
Wszystko w kupie, jak bywa u szlachty zwyczajnie;
Wszystko nadzwyczaj stare, zgniłe. Domu dachy
Świeciły się, jak gdyby od zielonej blachy,
Od mchu i trawy, która buja jak na łące.
Po strzechach gumien niby ogrody wiszące
Różnych roślin, pokrzywa i krokos czerwony,
Żółta dziewanna, szczyru barwiste ogony.
Gniazda ptastwa różnego, w strychach gołębniki,
W oknach gniazda jaskółcze, u progu króliki
Białe skaczą i ryją w niedeptanej darni.
Słowem: dwór na kształt klatki albo królikarni.

    A dawniej był obronny! Pełno wszędzie śladów,
Że wielkich i że częstych doznawał napadów.
Pod bramą dotąd w trawie, jak dziecięca głowa,
Wielka leżała kula żelazna działowa
Od czasów szwedzkich; niegdyś skrzydło wrót otwarte
Bywało o tę kulę jak o głaz oparte.
Na dziedzińcu, spomiędzy piołunu i chwastu,
Wznoszą się stare szczęty krzyżów kilkunastu
Na ziemi nieświęconej: znać, że tu chowano
Poległych śmiercią nagłą i niespodziewaną.
Kto by uważał z bliska lamus, spichrz i chatę,
Ujrzy ściany od ziemi do szczytu pstrokate
Niby rojem owadów czarnych: w każdej plamie
Siedzi we środku kula jak trzmiel w ziemnej jamie.

    U drzwi domostwa wszystkie klamki, ćwieki, haki
Albo ucięte, albo noszą szabel znaki:
Pewnie tu probowano hartu zygmuntówek,
Którymi można śmiało ćwieki obciąć z główek,
Lub hak przerżnąć, w brzeszczocie nie zrobiwszy szczerby.
Nade drzwiami, Dobrzyńskich widne były herby;
Lecz armaturę — serów zasłoniły półki
I zasklepiły gęsto gniazdami jaskółki.

    Wewnątrz samego domu, w stajni i wozowni,
Pełno znajdziesz rynsztunków, jak w starej zbrojowni.
Pod dachem wiszą cztery ogromne szyszaki,
Ozdoby czół marsowych: dziś Wenery ptaki,
Gołębie, w nich gruchając karmią swe pisklęta.
W stajni kolczuga wielka nad żłobem rozpięta
I pierścieniasty pancerz służą za drabinę,
W którą chłopiec zarzuca źrebcom dzięcielinę.
W kuchni kilka rapierów kucharka bezbożna
Odhartowała, kładąc je w piec zamiast rożna;
Buńczukiem, łupem z Wiednia, otrzepywa żarna:
Słowem, wygnała Marsa Ceres gospodarna
I panuje z Pomoną, Florą i Wertumnem
Nad Dobrzyńskiego domem, stodołą i gumnem.
Ale dziś muszą znowu ustąpić boginie:
Mars powraca.

                        O świcie zjawił się w Dobrzynie
Konny posłaniec; biega od chaty do chaty,
Budzi jak na pańszczyznę. Wstają szlachta braty,
Napełniają się ciżbą zaścianku ulice,
Słychać krzyk w karczmie, widać w plebanii świéce.
Biega; jeden drugiego pyta co to znaczy,
Starzy składają radę, młódź konie kulbaczy,
Kobiety zatrzymują, chłopcy się szamocą,
Rwą się biec, bić się, ale nie wiedzą z kim, o co?
Muszą chcąc nie chcąc zostać. W mieszkaniu plebana
Trwa rada długa, tłumna, strasznie zamieszana;
Aż nie mogąc zdań zgodzić, na koniec stanowi
Przełożyć całą sprawę ojcu Maciejowi.

    Siedemdziesiąt dwa lat liczył Maciej, starzec dziarski
Niskiego wzrostu, dawny konfederat barski.
Pamiętają i swoi, i nieprzyjaciele
Jego damaskowaną krzywą karabelę,
Którą piki i sztyki rzezał na kształt sieczki,
I której żartem skromne dał imię *Rózeczki*.
Z konfederata stał się stronnikiem królewskim,
I trzymał z Tyzenhauzem, podskarbim litewskim;
Lecz gdy król w Targowicy przyjął uczestnictwo,
Maciej opuścił znowu królewskie stronnictwo.
I stąd to, że przechodził partyi tak wiele,
Nazywany był dawniej *Kurkiem na kościele*:
Że jak kurek za wiatrem chorągiewkę zwracał.
Przyczynę zmian tak częstych na próżno byś macał:
Może Maciej zbyt wojnę lubił; zwyciężony
W jednej stronie, znów bitwy szukał z drugiej strony?
Może, bystry polityk, duch czasu zbadywał,
I tam szedł, gdzie ojczyzny dobro upatrywał?
Kto wie! To pewna, że go nigdy nie uwiodły
Ani chęć osobistej chwały, ni zysk podły,
I że nigdy z moskiewską partyją nie trzymał;
Na sam widok Moskala pienił się i zżymał.
By nie spotkać Moskala, po kraju zaborze
Siedział w domu jak niedźwiedź, gdy ssie łapę w borze.

    Ostatni raz wojował, poszedłszy z Ogińskim
Do Wilna, gdzie służyli oba pod Jasińskim,
I tam z *Rózeczką* cudów dokazał odwagi.
Wiadomo, że sam jeden skoczył z wałów Pragi
Bronić pana Pocieja, który odbieżany
Na placu boju, dostał dwadzieścia trzy rany.
Myślano długo w Litwie, że obu zabito:
Wrócili oba, każdy pokłuty jak sito.
Pan Pociej, zacny człowiek, chciał zaraz po wojnie
Obrońcę Dobrzyńskiego wynagrodzić hojnie;
Dawał mu folwark pięciu dymów w dożywocie
I wyznaczył mu rocznie tysiąc złotych w złocie.
Lecz Dobrzyński odpisał: «Niech Pociej Macieja
A nie Maciej Pocieja ma za dobrodzieja».
Odmówił więc folwarku i nie przyjął płacy;
Sam wróciwszy do domu, żył z własnej rąk pracy,
Sprawując ule dla pszczół, lekarstwa dla bydła,
Szląc na targ kuropatwy, które łowił w sidła
I polując na źwierza.

                        Było dość w Dobrzynie
Starych ludzi roztropnych, którzy po łacinie
Umieli i w palestrze ćwiczyli się z młodu;
Było dość majętniejszych: a z całego rodu
Maciek prostak ubogi był najwięcej czczony,
Nie tylko jako rębacz *Rózeczką* wsławiony,
Lecz jako człek mądrego i pewnego zdania,
Znający dzieje kraju, rodziny podania.
Zarówno świadom prawa jak i gospodarstwa,
Wiedział także sekreta strzelców i lekarstwa;
Przyznawano mu nawet (czemu pleban przeczy)
Wiadomość nadzwyczajnych i nadludzkich rzeczy.
To pewna, że powietrza zmiany zna dokładnie,
I częściej niż kalendarz gospodarski zgadnie.
Nie dziw tedy, że czy to siejbę rozpoczynać,
Czy wiciny wyprawiać, czy zboże zażynać,
Czy procesować, czyli zawierać układy:
Nie działo się w Dobrzynie nic bez Maćka rady.
Wpływu takiego starzec bynajmniej nie szukał;
Owszem, chciał się go pozbyć, klientów swych fukał,
I najczęściej wypychał milczkiem za drzwi domu.
Rady rzadko udzielał i nie lada komu;
Ledwie w niezmiernie ważnych sporach lub umowach
Pytany, wyrzekł zdanie i w niewielu słowach.
Myślano, że dzisiejszej podejmie się sprawy
I stanie swą osobą na czele wyprawy;
Bo bijatykę lubił niezmiernie za młodu
I był nieprzyjacielem moskiewskiego rodu.

    Właśnie staruszek chodził po samotnym dworze,
Nucąc piosenkę: *Kiedy ranne wstają zorze*,
Rad, że się wypogadza. Mgła nie szła do góry,
Jak się dziać zwykło, kiedy zbierają się chmury,
Ale coraz spadała. Wiatr rozwinął dłonie
I mgłę muskał, wygładzał, rozścielał na błonie;
Tymczasem słonko z góry tysiącem promieni
Tło przetyka, pośrebrza, wyzłaca, rumieni.
Jak para mistrzów w Słucku lity pas wyrabia:
Dziewica siedząc w dole krośny ujedwabia
I tło ręką wygładza, tymczasem tkacz z góry
Zrzuca jej nitki srebra, złota i purpury,
Tworząc barwy i kwiaty: tak dziś ziemię całą
Wiatr tumanami osnuł, a słońce dzierzgało.

    Maciej ogrzał się słońcem, zakończył pacierze,
I już się do swojego gospodarstwa bierze.
Wyniósł traw, liścia; usiadł przed domem i świsnął:
Na ten świst rój królików spod ziemi wytrysnął.
Jako narcyzy nagle wykwitłe nad trawę,
Bielą się długie słuchy; pod nimi jaskrawe
Przeświecają się oczki jak krwawe rubiny,
Gęsto wszyte w aksamit zielonej darniny.
Już króliki na łapkach stają; każdy słucha,
Patrzy; na koniec cała trzódka białopucha
Bieży do starca liśćmi kapusty znęcona,
Do nóg mu, na kolana skacze, na ramiona.
On, sam biały jak królik, lubi ich gromadzić
Wkoło siebie i ręką ciepły ich puch gładzić;
A drugą ręką z czapki proso w trawę miota
Dla wróblów: spada z dachów krzykliwa hołota.

    Gdy się staruszek bawił widokiem biesiady,
Nagle króliki znikły w ziemi, a gromady
Wróblów na dach uciekły przed gośćmi nowymi,
Którzy szli do folwarku krokami prędkiemi.
Byli to z plebanii przez szlachty gromadę
Posłowie wyprawieni do Maćka po radę.
Z dala witając starca niskimi ukłony
Rzekli: «Niech będzie Jezus Chrystus pochwalony»
«Na wieki wieków, amen» starzec odpowiedział,
A gdy się o ważności poselstwa dowiedział,
Prosi do chaty. Weszli, zasiadają ławę;
Pierwszy z posłów stał w środku i jął zdawać sprawę.

    Tymczasem szlachty coraz gęściej przybywało:
Dobrzyńscy prawie wszyscy, sąsiadów niemało
Z okolicznych zaścianków, zbrojni i bezbronni,
W kałamaszkach i bryczkach, i piesi, i konni.
Stawią wozy, podjezdki do brzezinek wiążą,
Ciekawi skutku narad koło domu krążą;
Już izbę napełnili, kupią się do sieni,
Inni słuchają, w okna głowami wciśnieni.




Księga siódma



Rada

Zbawienne rady Bartka zwanego Prusak — Głos żołnierski Maćka Chrzciciela — Głos polityczny pana Buchmana — Jankiel radzi ku zgodzie, którą Scyzoryk rozcina — Rzecz Gerwazego, z której okazują się wielkie skutki wymowy sejmowej — Protestacja starego Maćka — Nagłe przybycie posiłków wojennych zrywa naradę — Hejże na Soplicę!

    Z kolei Bartek poseł rzecz swą wyprowadzał.
Ten, że często na strugach do Królewca chadzał,
Nazwany był Prusakiem od swych spółrodaków:
Przez żart, bo nienawidził okropnie Prusaków,
Choć lubił o nich gadać. Człek podeszły w lata,
W podróżach swych dalekich wiele zwiedził świata;
Gazet pilny czytelnik, polityki świadom,
W niebytność Maćka zwykle przewodził obradom.
Ten tak rzecz kończył:

                        «Nie jest to, panie Macieju,
Bracie mój, a nas wszystkich Ojcze Dobrodzieju,
Nie jest to marna pomoc. Ja bym na Francuzów
Spuścił się w czasie wojny, jak na czterech tuzów:
Lud bitny, a od czasów pana Tadeusza
Kościuszki, świat takiego nie miał genijusza
Wojennego, jak wielki cesarz Bonaparte.
Pamiętam, kiedy przeszli Francuzi przez Wartę;
Bawiłem za granicą wtenczas, w roku pańskim
Tysiącznym osimsetnym szóstym; właśnie z Gdańskiem
Handlowałem, a krewnych mam wiele w Poznańskiem.
Jeździłem ich odwiedzić; więc z panem Józefem
Grabowskim, który teraz jest rejmentu szefem,
A podówczas żył na wsi blisko Obiezierza,
Polowaliśmy sobie na małego źwierza.
Był pokój w Wielkopolszcze, jak teraz na Litwie;
Wtem nagle rozeszła się wieść o strasznej bitwie.
Przybiegł do nas posłaniec od pana Towdena:
Grabowski list przeczytał, krzyknął: «Jena! Jena!
Zbito Prusaków na łeb, na szyję, wygrana!»
Ja, z konia zsiadłszy, zaraz padłem na kolana,
Dziękując Panu Bogu… Do miasta jedziemy,
Niby dla interesu, niby nic nie wiemy:
Aż tu widzimy wszystkie landraty, hofraty,
Komisarze i wszystkie podobne psubraty
Kłaniają się nam nisko; każdy drży, blednieje,
Jako owad prusaczy, gdy wrzątkiem kto zleje.
My śmiejąc się, trąc ręce, prosim uniżenie
O nowinki? pytamy, co słychać o Jenie?
Tu ich strach zdjął; dziwią się, że o klęsce owej
Już wiemy; krzyczą Niemcy: «Achary Got! o wej!»
Spuściwszy nos, do domów, z domów dalej w nogi —
O, to był rwetes! Wszystkie wielkopolskie drogi
Pełne uciekających. Niemczyska jak mrowie
Pełzną, ciągną pojazdy, które lud tam zowie
Wageny i fornalki; mężczyźni, kobiety,
Z fajkami, z imbryczkami, wleką pudła, bety;
Drapią jak mogą. A my milczkiem wchodzim w radę:
Hejże na koń, pomieszać Niemcom rejteradę!
Nuż landratom tłuc w karki, z hofratów drzeć schaby,
A herów oficerów łowić za harcaby!
A jenerał Dąbrowski wpada do Poznania
I cesarski przynosi rozkaz: do powstania!
W tydzień jeden tak lud nasz Prusaków wychłostał
I wygnał, na lekarstwo Niemca byś nie dostał!
Gdyby się tak obrócić i gracko, i raźnie,
I u nas w Litwie sprawić Moskwie taką łaźnię?
He, co myślisz Macieju? Jeśli z Bonapartem
Moskwa drze koty, to on wojuje nie żartem:
Bohater pierwszy w świecie, a wojsk ma bez liku!
He, cóż myślisz Macieju, nasz ojcze Króliku?»

    Skończył. Czekają wszyscy Macieja wyroku.
Maciej głowy nie ruszył ani podniósł wzroku,
Tylko ręką kilkakroć uderzył po boku,
Jak gdyby szabli szukał (od zaboru kraju
Szabli nie nosił; przecież z dawnego zwyczaju,
Na wspomnienie Moskala, zawsze rękę zwracał
Na lewy bok: zapewne Rózeczki swej macał;
I stąd był nazywany powszechnie *Zabokiem*).
Już wzniósł głowę; słuchają w milczeniu głębokiem.
Maciej oczekiwanie powszechne omylił,
Nachmurzył brwi i znowu głowę na pierś schylił.
Na koniec odezwał się, z wolna każde słowo
Wymawiając z przyciskiem, a w takt kiwał głową.

    «Cicho! skądże ta cała nowina pochodzi?
Jak daleko Francuzi? kto nimi dowodzi?
Czy już wojnę zaczęli z Moskwą? gdzie i o co?
Którędy mają ciągnąć? z jaką idą mocą?
Wiele piechoty, jazdy? Kto wie, niechaj gada!»

    Milczała patrząc na się kolejno gromada.
«Radziłbym — rzecze Prusak — czekać bernardyna
Robaka, bo od niego pochodzi nowina;
Tymczasem posłać pewnych szpiegów nad granicę,
I po cichu uzbrajać całą okolicę,
A tymczasem ostrożnie całą rzecz prowadzić,
Aby Moskalom naszych zamiarów nie zdradzić».

    «He! czekać? szczekać? zwlekać?» przerwał Maciej drugi
Ochrzczony Kropicielem, od wielkiej maczugi,
Którą zwał Kropidełkiem. Miał ją dziś przy sobie;
Stanął za nią, na gałce zwiesił ręce obie,
Na ręku oparł brodę, krzycząc: «Czekać! zwlekać!
Sejmikować! Hem, trem, brem, a potem uciekać!
Ja w Prusach nie bywałem; rozum królewiecki
Dobry dla Prus, a u mnie jest rozum szlachecki.
To wiem: że kto chce bić się, niech Kropidło chwyta;
Kto umierać, ten księdza niech woła, i kwita!
Ja chcę żyć, bić! Bernardyn po co? czy my żaki?
Co mi tam Robak: otóż, my będziem robaki,
I dalej Moskwę toczyć! Trem, brem, szpiegi, wzwiady;
Wiecie wy, co to znaczy? Oto, że wy dziady,
Niedołęgi! He, bracia, to wyżła rzecz tropić,
Bernardyńska kwestować, a moja rzecz: kropić;
Kropić, kropić i kwita!» Tu maczugę głasnął,
Za nim cały tłum szlachty «Kropić, kropić!» wrzasnął.

    Poparł stronę Chrzciciela, Bartek zwan Brzytewka
Od szabli cienkiej, tudzież Maciej, zwan Konewka
Od sztućca który naszał, z gardłem tak szerokiem,
Że zeń jak z konwi tuzin kulek lał potokiem.
Oba krzyczeli: «Wiwat Chrzciciel z kropidełkiem!»
Prusak chciał mówić, ale zgłuszono go zgiełkiem
I śmiechem; «Precz — wołano — precz Prusaki tchórze!
Kto tchórz, niech w bernardyńskim chowa się kapturze!»

    Wtem znowu głowę z wolna podniósł Maciej stary,
I zaczęły cokolwiek uciszać się gwary:
«Nie drwijcie — rzekł — z Robaka; znam go, to ćwik klecha,
Ten robaczek większego od was zgryzł orzecha.
Raz go tylko widziałem: ledwiem okiem rzucił,
Poznałem co za ptaszek; ksiądz oczy odwrócił,
Lękając się, żebym go nie zaczął spowiadać;
Ale to rzecz nie moja, wiele o tym gadać!
On tu nie przyjdzie; próżno wzywać bernardyna.
Jeśli od niego wyszła ta cała nowina,
To kto wie, w jakim celu: bo to bies księżyna!
Jeśli prócz tej nowiny nic więcej nie wiecie:
Więc po coście tu przyszli? i czego wy chcecie?»

    «Wojny!» krzyknęli. — «Jakiej?» spytał. — Zawołali:
«Wojny z Moskalem! Bić się! Hejże na Moskali!»

    Prusak wciąż wołał, a głos coraz wyżej wznosił;
Aż posłuchanie częścią ukłonem wyprosił,
Częścią zdobył swą mową krzykliwą i cienką.
«I ja chcę bić się — wołał tłukąc się w pierś ręką —
Choć kropidła nie noszę, drągiem od wiciny
Sprawiłem raz Prusakom czterem dobre chrzciny,
Którzy mię po pjanemu chcieli w Preglu topić».
«Toś zuch Bartku — rzekł Chrzciciel — dobrze! kropić, kropić!»
«Ależ, najsłodszy Jezu! trzeba pierwej wiedzieć
Z kim wojna? o co? trzeba to światu powiedzieć —
Wołał Prusak — bo jakże lud ruszy za nami?
Gdzie pójdzie, kiedy gdzie iść, my nie wiemy sami?
Bracia szlachta! Panowie! potrzeba rozsądku!
Dobrodzieje! potrzeba ładu i porządku!
Chcecie wojny, więc zróbmy konfederacyją;
Obmyślmy, gdzie zawiązać i pod laską czyją?
Tak było w Wielkopolszcze: widzim rejteradę
Niemiecką: cóż my robim? wchodzim tajnie w radę,
Uzbrajamy i szlachtę, i włościan gromadę;
Gotowi, Dąbrowskiego czekamy rozkazu;
Na koniec, hejże na koń! powstajem od razu!»

    «Proszę o głos!» zawołał pan komisarz z Klecka,
Człowiek młody, przystojny, ubrany z niemiecka.
Zwał się Buchman, lecz Polak był, w Polsce się rodził;
Nie wiedzieć pewnie, czyli ze szlachty pochodził,
Lecz o to nie pytano; i wszyscy Buchmana
Szacowali, iż służył u wielkiego pana,
Był dobry patryjota i pełen nauki,
Z ksiąg obcych wyuczył się gospodarstwa sztuki,
I dóbr administracją prowadził porządnie;
O polityce także wnioskował rozsądnie,
Pięknie pisać i gładko umiał się wysławiać.
Zatem umilkli wszyscy, kiedy jął rozprawiać:
«Proszę o głos!» powtórzył, po dwakroć odchrząknął,
Ukłonił się i usty dźwięcznymi tak brząknął:

    «Preopinanci moi w swych głosach wymownych
Dotknęli wszystkich punktów stanowczych i głownych,
Dyskusyją na wyższe wznieśli stanowisko;
Mnie tylko pozostaje, w jedno zjąć ognisko
Rzucone trafne myśli i rozumowania:
Mam nadzieję w ten sposób sprzeczne zgodzić zdania.
Dwie części w dyskusyji całej uważałem;
Podział już jest zrobiony, idę tym podziałem.
Naprzód: dlaczego mamy przedsiębrać powstanie?
W jakim duchu? to pierwsze żywotne pytanie;
Drugie, rewolucyjnej władzy się dotycze:
Podział jest trafny, tylko przewrócić go życzę.
Naprzód zacząć od władzy: skoro pojmiem władzę,
Z niej powstania istotę, duch, cel, wyprowadzę.
Co do władzy więc — kiedy oczyma przebiegam
Dzieje całej ludzkości, i cóż w nich spostrzegam?
Oto, ród ludzki dziki, w lasach rozpierzchniony,
Skupia się, zbiera, łączy dla wspólnej obrony,
Obmyśla ją; i to jest najpierwsza obrada.
Potem każdy wolności własnej cząstkę składa
Dla dobra powszechnego: to pierwsza ustawa,
Z której jako ze źródła płyną wszystkie prawa.
Widzimy tedy, że rząd umową się tworzy,
Nie pochodząc, jak mylnie sądzę, z woli Bożej.
Owoż, rząd na kontrakcie oparłszy społecznym,
Podział władzy już tylko jest skutkiem koniecznym».

    «Otóż są i kontrakty! Kijowskie czy mińskie? —
Rzekł stary Maciej — owoż i rządy babińskie!
Panie Buchman, czy Bóg nam chciał cara narzucić,
Czy diabeł, ja z waszmością nie będę się kłócić:
Panie Buchman, gadaj Waść, jakby cara zrzucić».

    «Tu sęk — krzyknął Kropiciel — gdybym mógł podskoczyć
Do tronu i Kropidłem, plusk, raz cara zmoczyć:
To już by on nie wrócił, ni kijowskim traktem,
Ni mińskim, ni za żadnym Buchmana kontraktem;
Aniby go wskrzesili z mocy bożej popi,
Ni z mocy Belzebuba — ten mi zuch, kto kropi.
Panie Buchman, waścina rzecz bardzo wymowna,
Ale wymowa szum, drum: kropić! to rzecz główna».

    «To, to, to!» pisnął, ręce trąc, Bartek Brzytewka,
Od Chrzciciela do Maćka biegając jak cewka
Od jednej strony krosien przerzucana w drugą:
«Tylko ty, Maćku z Rózgą, ty, Maćku z maczugą;
Tylko zgódźcie się: dalbóg, pobijem na druzgi
Moskala; Brzytew idzie pod komendę Rózgi».

    «Komenda — przerwał Chrzciciel — dobra ku paradzie;
U nas była komenda w kowieńskiej brygadzie
Krótka a węzłowata: strasz, sam się nie strachaj;
Bij, nie daj się; postępuj często, gęsto machaj:
Szach, mach!» «To — pisnął Brzytwa — to mi regulament!
Po co tu pisać akta, po co psuć atrament?
Konfederacji trzeba? o to cała sprzeczka?
Jest Marszałek nasz Maciej, a laska Rózeczka».
«Niech żyje — krzyknął Chrzciciel — Kurek na Kościele!»
Szlachta odpowiedziała. «Wiwant Kropiciele!»

    Ale w kątach szmer powstał, choć w środku tłumiony;
Widać, że się rozdziela rada na dwie strony.
Buchman krzyknął: «Ja zgody nigdy nie pochwalam!
To mój system!» Ktoś drugi wrzasnął: «Nie pozwalam!»
Inni z kątów wtórują. Nareszcie głos gruby
Ozwał się przybyłego szlachcica Skołuby:

    «Cóż to, Państwo Dobrzyńscy! A to co się święci?
A my, czy to będziemy z pod prawa wyjęci?
Kiedy nas zapraszano z naszego zaścianku,
A zapraszał nas klucznik Rębajło Mopanku,
Mówiono nam, że wielkie rzeczy dziać się miały,
Że tu nie o Dobrzyńskich, lecz o powiat cały,
O całą szlachtę idzie; toż i Robak bąkał,
Choć nigdy nie dokończył i zawsze się jąkał,
I ciemno się tłumaczył. Wreszcie, koniec końców,
My zjechali, sąsiadów zwołali przez gońców.
Nie sami tu panowie Dobrzyńscy jesteście;
Z różnych innych zaścianków jest tu nas ze dwieście:
Wszyscy więc radźmy. Jeśli potrzeba marszałka,
Głosujmy wszyscy; równa u każdego gałka.
Niech żyje równość!»

                        Zatem dwaj Terajewicze
I czterej Stypułkowscy i trzej Mickiewicze,
Krzyknęli: «Wiwat równość!» stając za Skołubą.
Tymczasem Buchman wołał: «Zgoda będzie zgubą!»
Kropiciel krzyczał: «Bez was obejdziem się sami;
Niech żyje nasz marszałek, Maciek nad Maćkami!
Hej do laski!» Dobrzyńscy krzyczą: «Zapraszamy!»
A obca szlachta woła w głos: «Nie pozwalamy!»
Rozstrycha się tłum na dwie kupy rozdzielony,
I kiwając głowami w dwie przeciwne strony,
Tamci: «Nie pozwalamy!» — ci krzyczą: «Prosiemy!»

    Maciek stary w pośrodku jeden siedział niemy,
I jedna głowa jego była nieruchoma.
Przeciw niemu stał Chrzciciel zwieszony rękoma
Na maczudze, a głową na końcu maczugi
Wspartą kręcił, jak tykwą wbitą, na kij długi,
I na przemiany to w tył, to się naprzód kiwał,
I ustawicznie «Kropić, kropić!» wykrzykiwał.
Wzdłuż izby zaś przebiegał Brzytewka ruchawy
Ciągle od Kropiciela do Macieja ławy.
Konewka zaś powoli wszerz izbę przechodził
Od Dobrzyńskich do szlachty: niby to ich godził;
Jeden wciąż wołał «Golić» a drugi «Zalewać!»
Maciek milczał; lecz widno, że się zaczął gniewać./

    Ćwierć godziny wrzał hałas, gdy nad tłum wrzeszczący,
Ze środka głów, wyskoczył w góre słup błyszczący:
Był to rapier sążnistej długości, szeroki
Na całą piędź, a sieczny na obadwa boki,
Widocznie miecz teutoński z norymberskiej stali
Ukuty: wszyscy milcząc na broń poglądali.
Kto ją podniósł? nie widać; lecz zaraz zgadniono:
«To Scyzoryk! niech żyje Scyzoryk! — krzykniono —
Wiwat Scyzoryk, klejnot Rębajłów zaścianku!
Wiwat Rębajło, Szczerbiec, Półkozic, Mopanku!»

    Wnet Gerwazy (to on był) przez tłum się przecisnął
Na środek izby, wkoło Scyzorykiem błysnął;
Potem w dół chyląc ostrze na znak powitania
Przed Maćkiem, rzekł: «Rózeczce Scyzoryk się kłania.
Bracia szlachta, Dobrzyńscy! Ja nie będę radził
Nic a nic; powiem tylko, po com was zgromadził:
A co robić, jak robić, decydujcie sami.
Wiecie, słuch dawno chodzi między zaściankami,
Że się na wielkie rzeczy zanosi na świecie;
Ksiądz Robak o tym gadał: wszakże wszyscy wiecie?»
«Wiemy!» krzyknęli — «Dobrze. Owoż mądrej głowie —
Ciągnął mówca, spojrzawszy bystro — dość dwie słowie.
Nieprawdaż?» «Prawda» rzekli. «Gdy cesarz francuski —
Rzekł Klucznik — stąd przyciąga, a stamtąd car ruski:
Więc wojna; car z cesarzem, królowie z królami
Pójdą za łby, jak zwykle między monarchami.
A nam czy siedzieć cicho? Gdy wielki wielkiego
Będzie dusić: my duśmy mniejszych, każdy swego.
Z góry i z dołu, wielcy wielkich, małych mali,
Jak zaczniem ciąć, tak całe szelmostwo się zwali,
I tak zakwitnie szczęście i Rzeczpospolita.
Nieprawdaż?» «Prawda — rzekli — jakby z książki czyta».
«Prawda — powtórzył Chrzciciel — krop a krop i kwita».
«Ja zawsze gotów golić» ozwał się Brzytewka;
«Tylko zgódźcie się — prosił uprzejmie Konewka —
Chrzcicielu i Macieju, pod czyją iść wodzą?»
Ale mu przerwał Buchman: «Niech się głupi godzą,
Dyskusyje publicznej sprawie nie zaszkodzą.
Proszę milczeć, słuchamy, sprawa na tym zyska;
Pan Klucznik ją z nowego zważa stanowiska».

    «Owszem — zawołał Klucznik — u mnie po staremu,
O wielkich rzeczach myśleć należy wielkiemu:
Jest na to cesarz, będzie król, senat, posłowie.
Takie rzeczy, mopanku, robią się w Krakowie
Lub w Warszawie, nie u nas, w zaścianku, w Dobrzynie;
Aktów konfederackich nie piszą w kominie
Kredą, nie na wicinie, lecz na pergaminie.
Nie nam to pisać akta; ma Polska pisarzy
Koronnych i litewskich, tak robili starzy;
Moja rzecz Scyzorykiem wyrzynać». «Kropidłem
Pluskać» dodał Kropiciel. «I wykalać Szydłem»
Krzyknął Bartek Szydełko, dobywszy swej szpadki.

    «Wszystkich was — kończył Klucznik — biorę tu na świadki,
Czy Robak nie powiadał, że wprzód nim przyjmiecie
W dom wasz Napoleona, trzeba wymieść śmiecie?
Słyszeliście to wszyscy: a czy rozumiecie?
Któż jest śmieciem powiatu? Kto zdradziecko zabił
Najlepszego z Polaków, kto go okradł, zgrabił?
I jeszcze chce ostatki wydrzeć z rąk dziedzica?
Któż to? Mamże wam gadać?» «A już ci Soplica —
Przerwał Konewka — to łotr» «Oj, to ciemiężyciel»
Pisnął Brzytewka — «Więc go kropić!» dodał Chrzciciel;
«Jeśli zdrajca — rzekł Buchman — więc na szubienicę!»
«Hejże! — krzyknęli wszyscy — hejże na Soplicę!»

    Lecz Prusak śmiał podjąć się Sędziego obrony,
I wołał z wzniesionymi ku szlachcie ramiony:
«Panowie Bracia! aj! aj! a na boskie rany!
Co znowu? Panie Klucznik, czy waść opętany?
Czy o tym była mowa? Że ktoś miał wariata
Banitę bratem: to co, karać go za brata?
To mi po chrześcijańsku! Są tu w tym konszachty
Hrabiego; żeby Sędzia był ciężki dla szlachty,
Nieprawda! dalibógże! To wy tylko sami
Pozywacie go, a on zgody szuka z wami,
Ustępuje ze swego, jeszcze grzywny płaci.
Ma proces z Hrabią: cóż stąd? obadwa bogaci;
Niechaj pan drze się z panem: cóż to do nas, braci?
Pan Sędzia ciemiężyciel! On pierwszy zabraniał,
Ażeby się chłop przed nim do ziemi nie kłaniał,
Mówiąc, że to grzech. Nieraz u niego gromada
Chłopska, ja sam widziałem, do stołu z nim siada;
Płacił za włość podatki: a nie tak jest w Klecku,
Choć tam waść, panie Buchman, rządzisz po niemiecku.
Sędzia zdrajca! My się z nim od infimy znamy:
Poczciwe było dziecko i dziś taki samy;
Polskę kocha nad wszystko, polskie obyczaje
Chowa, modom moskiewskim przystępu nie daje.
Ilekroć z Prus powracam, chcąc zmyć się z niemczyzny,
Wpadam do Soplicowa jak w centrum polszczyzny;
Tam się człowiek napije, nadysze ojczyzny!
Dalbóg Dobrzyńscy! ja wasz brat, ale Sędziego
Nie pozwolę pokrzywdzić; nie będzie nic z tego.
Nie tak, panowie bracia, w Wielkopolszcze było:
Co za duch! co za zgoda! aż przypomnieć miło!
Nikt tam podobną fraszką nie śmiał rady mieszać».
«To nie fraszka — zawołał Klucznik — łotrów wieszać!»

    Szmer wzmagał się. Wtem Jankiel posłuchania prosił,
Na ławę wskoczył, stanął i nad głowy wznosił
Brodę jak wiechę, co mu aż do pasa wisi.
Prawą ręką zdjął z wolna z głowy kołpak lisi;
Lewą ręką jarmułkę zruszoną poprawił,
Potem lewicę za pas zatknął i tak prawił,
Kołpakiem lisim w kolej kłaniając się nisko:

    «Nu, panowie Dobrzyńscy! Ja sobie Żydzisko;
Mnie Sędzia ni brat, ni swat; szanuję Sopliców
Jak panów bardzo dobrych i moich dziedziców;
Szanuję też Dobrzyńskich, Bartków i Maciejów,
Jako dobrych sąsiadów, panów dobrodziejów;
A mówię tak: jeżeli państwo chcą gwałt zrobić
Sędziemu, to bardzo źle. Możecie się pobić,
Zabić — a asesory? a sprawnik? a turma?
Bo w wiosce u Soplicy jest żołnierzy hurma,
Wszystko jegry! Asesor w domu: tylko świśnie,
Tak wraz przymaszerują, stoją jak umyślnie.
A co będzie? A jeśli czekacie Francuza,
To Francuz jest daleko jeszcze, droga duża.
Ja Żyd, o wojnach nie wiem, a byłem w Bielicy,
I widziałem tam Żydków od samej granicy;
Słychać, że Francuz stoi nad rzeką Łososną,
A wojna jeśli będzie, to chyba aż wiosną.
Nu, mówię tak: czekajcie; wszak dwór Soplicowa
Nie budka kramna, co się rozbierze, w wóz schowa
I pojedzie: dwór jak stał, do wiosny stać będzie;
A pan Sędzia, to nie jest Żydek na arendzie:
Nie uciecze, to jego można znaleźć wiosną.
A teraz rozejdźcie się, a nie gadać głośno
O tym, co było; bo to gadać, to daremno!
A czyja łaska panów Szlachty, proszę ze mną.
Moja Siora powiła małego Jankielka:
Ja dziś traktuję wszystkich, a muzyka wielka!
Każę przynieść kozice, basetlę, dwie skrzypiec,
A pan Maciek Dobrodziej lubi stary lipiec
I nowego mazurka: mam nowe mazurki,
A wyuczyłem śpiewać fein moje bachurki».

    Wymowa lubionego powszechnie Jankiela
Trafiała do serc. Powstał krzyk, oklask wesela,
Szmer przyzwolenia nawet za domem się szerzył:
Gdy Gerwazy w Jankiela Scyzorykiem zmierzył.
Żyd skoczył, wpadł w tłum; Klucznik wołał: «Precz stąd, Żydzie!
Nie tkaj palców między drzwi, nie o ciebie idzie!
Panie Prusak! że waszeć Sędziowską handlujesz
Parą wicin mizernych: to już zań gardłujesz?
Zapomniałeś mopanku, że ojciec waszecin
Spławiał do Prus dwadzieścia Horeszkowskich wicin?
Stąd się zbogacił i on, i jego rodzina,
Ba, nawet wszyscy, ilu was tu jest z Dobrzyna.
Bo pamiętacie starzy, słyszeliście młodzi,
Że Stolnik był was wszystkich ojciec i dobrodziéj:
Kogoż on komisarzem słał do swych dóbr pińskich?
Dobrzyńskiego! Rachmistrzów kogo miał? Dobrzyńskich!
Marszałkostwa, kredensu nie zwierzał nikomu,
Tylko Dobrzyńskim: pełno Dobrzyńskich miał w domu!
On forytował wasze w trybunałach sprawy,
On wyrabiał u króla dla was chleb łaskawy,
Dzieci wasze kopami pomieszczał w konwikcie
Pijarskim, na swym koszcie, odzieży i wikcie;
Dorosłych promowował także swym nakładem:
A dlaczego to robił? że wam był sąsiadem!
Dziś Soplica kopcami tyka waszych granic:
Cóż kiedy wam dobrego zrobił on?»

                        «Nic a nic! —
Przerwał Konewka — bo to wyrosło z szlachciury,
A jak dmie się, phu, phu, phu, jak nos drze do góry!
Pamiętacie, prosiłem na córki wesele;
Poję, nie chce pić, mówi: »Nie piję tak wiele
Jak wy szlachta; wy szlachta ciągniecie jak bąki«.
Ot magnat! delikacik z marymonckiej mąki!
Nie pił; leliśmy w gardło, krzyczał: »Gwałt się dzieje!«
Czekajno, niech no ja mu z Konewki naleję».

    «Filut — zawołał Chrzciciel — oj, i ja go kropnę
Za swoje. Mój syn, było to dziecko roztropne,
Teraz tak zgłupiał, że go nazywają Sakiem;
A z przyczyny Sędziego został głupcem takim.
Mówiłem: po co tobie leźć do Soplicowa?
Jeżeli cię tam złowię, niech cię Bóg uchowa!
On znowu smyk do Zosi, dybie przez konopie:
Złowiłem go, a zatem za uszy i kropię;
A on beczy i beczy jak maleńkie chłopię:
»Ojcze, choć zabij, muszę tam iść«, a wciąż szlocha —
»Co tobie?« a on mówi, że tę Zosię kocha!
Chciałby popatrzyć na nią! Żal mi nieboraka,
Mówię Sędziemu: »Sędzio, daj Zosię dla Saka!«
On mówi: »Jeszcze mała, czekaj ze trzy lata,
Jak sama zechce«. Łotr! łże, już ją komuś swata:
Słyszałem. Już ja się tam na wesele wkręcę;
Ja im łoże małżeńskie kropidłem poświęcę».

    «I taki łotr — zawołał Klucznik — ma panować?
I dawnych panów, lepszych od siebie, rujnować?
A Horeszków i pamięć i imię zaginie!
Gdzież jest wdzięczność na świecie? Nie ma jej w Dobrzynie!
Bracia! chcecie bój z ruskim wieść imperatorem,
A boicie się wojny z Soplicowskim dworem?
Strach wam turmy! Czyż to ja wzywam na rozboje?
Broń Boże! Szlachta Bracia! ja przy prawie stoję.
Wszak Hrabia wygrał, zyskał dekretów niemało:
Tylko je egzekwować! Tak dawniej bywało:
Trybunał pisał dekret; szlachta wypełniała,
A szczególniej Dobrzyńscy, i stąd wasza chwała
Urosła w Litwie! Wszakże to Dobrzyńscy sami
Bili się na zajezdzie myskim z Moskalami,
Których przywiódł jenerał ruski Wojniłowicz
I łotr, przyjaciel jego, pan Wołk z Łogomowicz.
Pamiętacie, jak Wołka wzięliśmy w niewolę,
Jak chcieliśmy go wieszać na belce w stodole,
Iż był tyran dla chłopstwa a sługa Moskali;
Ale się chłopi głupi nad nim zlitowali!
(Upiec go muszę kiedyś na tym Scyzoryku.)
Nie wspomnę innych wielkich zajazdów bez liku,
Z których wyszliśmy zawsze, jak szlachcie przystało,
I z zyskiem i aplauzem powszechnym i z chwałą!
Po cóż o tym wspominać? Dziś darmo pan Hrabia,
Sąsiad wasz, sprawę toczy, dekrety wyrabia:
Już nikt z was pomóc nie chce biednemu sierocie!
Dziedzic Stolnika tego, który żywił krocie,
Dziś nie ma przyjaciela, oprócz mnie, Klucznika,
I ot tego wiernego mego Scyzoryka!»

    «I Kropidła — rzekł Chrzciciel — Gdzie ty Gerwazeńku,
Tam i ja; póki ręka, póki plusk plask w ręku.
Co dwaj to dwaj! Dalibóg mój Gerwazy! ty miecz,
Ja mam Kropidło; dalbóg! ja kropię, a ty siecz:
I tak szach mach, plusk i plask; oni niech gawędzą!»

    «Toć i Bartka — rzekł Brzytwa — bracia nie odpędzą;
Już co wy namydlicie, to ja wszystko zgolę».
«I ja — przydał Konewka — z wami ruszyć wolę,
Gdy ich nie można zgodzić na obiór marszałka;
Co mi tam głosy, gałki! U mnie insza gałka.
— Tu wydobył z kieszeni garść kul, dzwonił nimi —
Ot gałki! — krzyknął — w Sędzię gałkami wszystkimi!»
«Do was — wołał Skołuba — do was się łączymy!»
«Gdzie wy — krzyknęła szlachta — gdzie wy, to tam i my!
Niech żyją Horeszkowie! wiwant Półkozice!
Wiwat Klucznik Rębajło! Hejże na Soplicę!»

    I tak wszystkich pociągnął wymowny Gerwazy;
Bo wszyscy ku Sędziemu mieli swe urazy,
Jak zwyczajnie w sąsiedztwie: to o szkodę skargi,
To o wyręby, to o granice zatargi.
Jednych gniew, drugich tylko podburzała zawiść
Bogactw Sędziego — wszystkich zgodziła nienawiść.
Cisną się do Klucznika, podnoszą do góry
Szable, pałki. —

                        Aż Maciek, dotychczas ponury,
Nieruchomy, wstał z ławy i wolnymi kroki
Wyszedł na środek izby i podparł się w boki;
I spojrzawszy przed siebie, i kiwając głową,
Zabrał głos, wymawiając z wolna każde słowo,
Z przestankiem i przyciskiem: «A głupi! a głupi!
A głupi wy! Na kim się mleło, na was skrupi!…
To póki o wskrzeszeniu Polski była rada,
O dobru pospolitym, głupi, u was zwada?
Nie można było, głupi, ani się rozmówić,
Głupi, ani porządku, ani postanowić
Wodza nad wami, głupi! A niech no kto podda
Osobiste urazy, głupi, u was zgoda!
Precz stąd! Bo jakom Maciek, was, do milijonów
Kroćset kroci tysięcy fur, beczek, furgonów,
Diabłów!!!!…»

                        Ucichli wszyscy jak rażeni gromem;
Ale razem straszliwy powstał krzyk za domem:
«Wiwat Hrabia!» On wjeżdżał na folwark Maciejów,
Sam zbrojny, za nim zbrojnych dziesięciu dżokejów.
Hrabia siedział na dzielnym koniu, w czarnym stroju;
Na sukni orzechowy płaszcz włoskiego kroju,
Szeroki, bez rękawów, jak wielka opona,
Spięty klamrą u szyi, spadał przez ramiona;
Kapelusz miał okrągły z piórem, w ręku szpadę.
Okręcił się i szpadą powitał gromadę.

    «Wiwat Hrabia! — krzyknęli — z nim żyć i umierać!»
Szlachta zaczęła z chaty przez okna wyzierać,
I za Klucznikiem coraz ku drzwiom się napierać.
Klucznik wyszedł, a za nim tłum przeze drzwi runął,
Maciek resztę wypędził, drzwi zamknął, zasunął,
I przez okno wyjrzawszy, raz jeszcze rzekł: «Głupi!»

    A tymczasem się szlachta do Hrabiego kupi
Idą w karczmę. Gerwazy wspomniał dawne czasy:
Kazał sobie trzy podać od kontuszów pasy,
Na nich ze sklepu karczmy beczki wydobywa
Trzy: jedną miodu, drugą wódki, trzecią piwa.
Wyjął goździe, wnet z szumem trysnęły trzy strugi,
Jeden biały jak srebro, krwawnikowy drugi,
Trzeci żółty; troistą grają w górze tęczą,
A spadając w sto kubków, we sto szklanek brzęczą.
Wre szlachta. Tamci piją, ci Hrabiemu życzą
Lat setnych, wszyscy: «Hejże na Soplicę!» krzyczą.

    Jankiel wymknął się milczkiem, oklep. Prusak, równie
Niesłuchany, choć jeszcze rozprawiał wymównie,
Chciał zmykać: szlachta w pogoń, wołając, że zdradził.
Mickiewicz stał z daleka; ni krzyczał, ni radził,
Ale z miny poznano, że coś złego knuje:
Więc do kordów, i hejże! On się rejteruje,
Odcina się, już ranny; przyparty do płotów:
Gdy mu skoczył na odsiecz Zan i trzech Czeczotów.
Za czym rozjęto szlachtę. Ale w tym rozruchu,
Dwóch było ciętych w ręce; ktoś dostał po uchu;
Reszta wsiadała na koń. —

                        Hrabia i Gerwazy
Porządkują, rozdają oręże, rozkazy.
W końcu, wszyscy przez długą zaścianku ulicę
Puścili się w cwał krzycząc: «Hejże na Soplicę!»




Księga ósma



Zajazd

Astronomia Wojskiego — Uwaga Podkomorzego nad kometami — Tajemnicza scena w pokoju Sędziego — Tadeusz, chcąc zręcznie wyplątać się, wpada w wielkie kłopoty — Nowa Dydo — Zajazd — Ostatnia woźnieńska protestacja — Hrabia zdobywa Soplicowo — Szturm i rzeź — Gerwazy piwniczym — Uczta zajazdowa.

    Przed burzą bywa chwila cicha i ponura,
Kiedy, nad głowy ludzi przyleciawszy, chmura
Stanie i grożąc twarzą, dech wiatrów zatrzyma,
Milczy, obiega ziemię błyskawic oczyma,
Znacząc te miejsca, gdzie wnet ciśnie grom po gromie:
Tej ciszy chwila była w Soplicowskim domie.
Myśliłbyś, że przeczucie nadzwyczajnych zdarzeń
Ścięło usta i wzniosło duchy w kraje marzeń.

    Po wieczerzy i Sędzia, i goście ze dworu
Wychodzą na dziedziniec używać wieczoru;
Zasiadają na przyzbach wysłanych murawą.
Całe grono z posępną i cichą postawą
Pogląda w niebo, które zdawało się zniżać,
Ścieśniać i coraz bardziej ku ziemi przybliżać,
Aż oboje, skrywszy się pod zasłonę ciemną
Jak kochankowie, wszczęli rozmowę tajemną,
Tłumacząc swe uczucia w westchnieniach tłumionych,
Szeptach, szmerach i słowach na wpół wymówionych,
Z których składa się dziwna muzyka wieczoru.

    Zaczął ją puszczyk, jęcząc na poddaszu dworu;
Szepnęły wiotkim skrzydłem nietoperze, lecą
Pod dom, gdzie szyby okien, twarze ludzi świecą;
Bliżej zaś nietoperzów siostrzyczki, ćmy, rojem
Wiją się przywabione białym kobiet strojem;
Mianowicie przykrzą się Zosi, bijąc w lice
I w jasne oczki, które biorą za dwie świéce.
Na powietrzu owadów wielki krąg się zbiera,
Kręci się, grając jako harmoniki sfera;
Ucho Zosi rozróżnia wśród tysiąca gwarów
Akord muszek i półton fałszywy komarów.

    W polu koncert wieczorny ledwie jest zaczęty;
Właśnie muzycy kończą stroić instrumenty.
Już trzykroć wrzasnął derkacz, pierwszy skrzypak łąki,
Już mu z dala wtórują z bagien basem bąki,
Już bekasy, do góry porwawszy się, wiją
I bekając raz po raz, jak w bębenki biją.

    Na finał szmerów muszych i ptaszęcej wrzawy
Odezwały się chórem podwójnym dwa stawy:
Jako zaklęte w górach kaukaskich jeziora
Milczące przez dzień cały, grające z wieczora.
Jeden staw, co toń jasną i brzeg miał piaszczysty,
Modrą piersią jęk wydał cichy, uroczysty;
Drugi staw, z dnem błotnistym i gardzielem mętnym,
Odpowiedział mu krzykiem żałośnie namiętnym:
W obu stawach piały żab niezliczone hordy,
Oba chóry zgodzone w dwa wielkie akordy.
Ten fortissimo zabrzmiał, tamten nuci z cicha;
Ten zdaje się wyrzekać, tamten tylko wzdycha:
Tak dwa stawy gadały do siebie przez pola
Jak grające na przemian dwie arfy Eola.

    Mrok gęstniał. Tylko w gaju i około rzeczki
W łozach, błyskały wilcze oczy jako świeczki;
A dalej, u ścieśnionych widnokręgu brzegów,
Tu i owdzie ogniska pastuszych noclegów.
Nareszcie księżyc srebrną pochodnię zaniecił,
Wyszedł z boru i niebo, i ziemię oświecił.
One teraz, z pomroku odkryte w połowie,
Drzemały obok siebie jako małżonkowie
Szczęśliwi: niebo w czyste objęło ramiona
Ziemi pierś, co księżycem świeci posrebrzona.

    Już naprzeciw księżyca gwiazda jedna, druga
Błysnęła; już ich tysiąc, już milijon mruga.
Kastor z bratem Polluksem jaśnieli na czele,
Zwani niegdyś u Sławian Lele i Polele;
Teraz ich w zodyjaku gminnym znów przechrzczono:
Jeden zowie się *Litwą*, a drugi *Koroną*.

    Dalej niebieskiej *Wagi* dwie szale błyskają:
Na nich Bóg w dniu stworzenia (starzy powiadają)
Ważył z kolei wszystkie planety i ziemię,
Nim w przepaściach powietrza osadził ich brzemię;
Potem wagi złociste zawiesił na niebie:
Z nich to ludzie wag i szal wzór wzięli dla siebie.

    Na północ świeci okrąg gwiaździstego *Sita,*
Przez które Bóg (jak mówią) przesiał ziarnka żyta,
Kiedy je z nieba zrzucał dla Adama ojca
Wygnanego za grzechy z rozkoszy ogrojca.

    Nieco wyżej *Dawida wóz*, gotów do jazdy,
Długi dyszel kieruje od polarnej gwiazdy.
Starzy Litwini wiedzą o rydwanie owym,
Że niesłusznie pospólstwo zwie go Dawidowym:
Gdyż to jest wóz Anielski. Na nim to przed czasy
Jechał Lucyper, Boga gdy wyzwał w zapasy,
Mlecznym gościńcem pędząc cwał w niebieskie progi,
Aż go Michał zbił z wozu, a wóz zrzucił z drogi.
Teraz, popsuty, między gwiazdami się wala;
Naprawiać go Archanioł Michał nie pozwala.

    I to wiadomo także u starych Litwinów,
(A wiadomość tę pono wzięli od rabinów)
Że ów zodyjakowy *Smok* długi i gruby,
Który gwiaździste wije po niebie przeguby,
Którego mylnie wężem chrzczą astronomowie,
Jest nie wężem, lecz rybą: *Lewiatan* się zowie.
Przed czasy mieszkał w morzach, ale po potopie
Zdechł z niedostatku wody; więc na niebios stropie,
Tak dla osobliwości jako dla pamiątki,
Anieli zawiesili jego martwe szczątki.
Podobnie pleban Mirski zawiesił w kościele
Wykopane olbrzymów żebra i piszczele.

    Takie gwiazd historyje, które z książek zbadał
Albo słyszał z podania, Wojski opowiadał.
Chociaż wieczorem słaby miał wzrok Wojski stary
I nie mógł w niebie dojrzeć nic przez okulary,
Lecz na pamięć znał imię i kształt każdej gwiazdy:
Wskazywał palcem miejsca i drogę ich jazdy.

    Dziś mało go słuchano, nie zważano wcale
Na *Sito*, ni na *Smoka*, ani też na *Szale*.
Dziś oczy i myśl wszystkich pociąga do siebie
Nowy gość dostrzeżony niedawno na niebie:
Był to kometa pierwszej wielkości i mocy.
Zjawił się na zachodzie, leciał ku północy;
Krwawym okiem z ukosa na rydwan spoziera,
Jakby chciał zająć puste miejsce Lucypera,
Warkocz długi w tył rzucił i część nieba trzecią
Obwinął nim, gwiazd krocie zagarnął jak siecią
I ciągnie je za sobą, a sam wyżej głową
Mierzy, na północ, prosto w gwiazdę biegunową.

    Z niewymownym przeczuciem cały lud litewski
Poglądał każdej nocy na ten cud niebieski,
Biorąc złą wróżbę z niego, tudzież z innych znaków:
Bo zbyt często słyszano krzyk złowieszczych ptaków,
Które na pustych polach gromadząc się w kupy,
Ostrzyły dzioby, jakby czekając na trupy;
Zbyt często postrzegano, że psy ziemię ryły
I jak gdyby śmierć wietrząc, przeraźliwie wyły:
Co wróży głód lub wojnę; a strażnicy boru
Widzieli, jak przez cmentarz szła dziewica moru,
Która wznosi się czołem nad najwyższe drzewa,
A w lewym ręku chustką skrwawioną powiewa.

    Różne stąd wnioski tworzył stojący przy płocie
Ciwun, co przyszedł zdawać sprawę o robocie,
I pisarz prowentowy w szeptach z Ekonomem.

    Lecz Podkomorzy siedział na przyzbie przed domem.
Przerwał rozmowę gości; znać, że głos zabiera:
Błysnęła przy księżycu wielka tabakiera
(Cała z szczerego złota, z brylantów oprawa,
We środku, za szkłem, portret króla Stanisława);
Zadzwonił w nią palcami, zażył i rzekł: «Panie
Tadeuszu, waścine o gwiazdach gadanie
Jest tylko echem tego, co słyszałeś w szkole.
Ja o cudzie prostaków poradzić się wolę.
I ja astronomii słuchałem dwa lata
W Wilnie, gdzie Puzynina, mądra i bogata
Pani, oddała dochód z wioski dwiestu chłopów
Na zakupienie różnych szkieł i teleskopów.
Ksiądz Poczobut, człek sławny, był obserwatorem
I całej Akademii naonczas Rektorem;
Przecież w końcu katedrę i teleskop rzucił,
Do klasztoru, do cichej celi swej powrócił
I tam umarł przykładnie. Znam się też z Śniadeckim,
Który jest mądrym bardzo człekiem, chociaż świeckim.
Owóż astronomowie planetę, kometę,
Uważają tak jako mieszczanie karetę;
Wiedzą, czyli zajeżdża przed króla stolicę,
Czyli z rogatek miejskich rusza za granicę;
Lecz kto w niej jechał? po co? co z królem rozmawiał?
Czy król posła z pokojem czy z wojną wyprawiał?
O to ani pytają. Pomnę za mych czasów,
Gdy Branecki karetą swą ruszył do Jassów
I za tą niepoczciwą pociągnął karetą
Ogon Targowiczanów, jak za tą kometą;
Lud prosty, choć w publiczne nie mieszał się rady,
Zgadnął zaraz, że ogon ów jest wróżbą zdrady.
Słychać, że lud dał imię miotły tej komecie
I powiada, że ona milijon wymiecie».

    A na to rzekł z ukłonem Wojski: «Prawda, Jaśnie
Wielmożny Podkomorzy: przypominam właśnie,
Co mnie mówiono niegdyś małemu dziecięciu,
Pamiętam, choć nie miałem wówczas lat dziesięciu,
Kiedy widziałem w domu naszym nieboszczyka
Sapiehę, pancernego znaku porucznika,
Co potem był nadwornym marszałkiem królewskim,
Na koniec umarł wielkim kanclerzem litewskim,
Miawszy lat sto i dziesięć. Ten, za króla Jana
Trzeciego, był pod Wiedniem w chorągwi hetmana
Jabłonowskiego. Owóż, ów kanclerz powiadał,
Że właśnie kiedy na koń król Jan Trzeci siadał,
Gdy nuncyjusz papieski żegnał go na drogę,
A poseł austryjacki całował mu nogę,
Podając strzemię (poseł zwał się Wilczek hrabia),
Król krzyknął: »Patrzcie, co się na niebie wyrabia!«
Spojrzą, alić nad głowy suwał się kometa
Drogą, jaką ciągnęły wojska Mahometa,
Z wschodu na zachód. Potem i ksiądz Bartochowski,
Składając panegiryk na tryumf krakowski,
Pod godłem Orientis Fulmen, prawił wiele
O tym komecie. Także czytam o nim w dziele
Pod tytułem Janina, gdzie jest opisana
Cała wyprawa króla nieboszczyka Jana
I wyryta chorągiew wielka Mahometa,
I ów, taki jak dziś go widzimy, kometa».

    «Amen — rzekł na to Sędzia — ja wróżbę waszeci
Przyjmuję, oby z gwiazdą zjawił się Jan Trzeci!
Jest na zachodzie wielki dziś bohater; może
Kometa go przywiedzie do nas, co daj Boże!»

    Na to rzekł Wojski, głowę pochyliwszy smutnie:
«Kometa czasem wojny, czasem wróży kłótnie!
Niedobrze, iż się zjawił tuż nad Soplicowem,
Może nam grozi jakiem nieszczęściem domowem.
Mieliśmy wczoraj dosyć rozterku i zwady,
Tak w czasie polowania, jako i biesiady.
Rejent kłócił się z rana z panem Asesorem,
A pan Tadeusz wyzwał Hrabiego wieczorem.
Pono spór ten ze skóry niedźwiedziej pochodził;
I gdyby mnie Dobrodziej Sędzia nie przeszkodził,
Ja bym u stołu obu przeciwników zgodził.
Bo chciałem opowiedzieć wypadek ciekawy,
Podobny do zdarzenia wczorajszej wyprawy,
Co trafił się najpierwszym strzelcom za mych czasów,
Posłowi Rejtanowi i Księciu Denassów.
Przypadek był takowy:

                        Jenerał Podolskich
Ziem przejeżdżał z Wołynia do swoich dóbr polskich,
Czy też, gdy dobrze pomnę, na sejm do Warszawy.
Po drodze zwiedzał szlachtę, już to dla zabawy,
Już dla popularności; wstąpił więc do pana
Tadeusza, dziś świętej pamięci, Rejtana,
Który był potem naszym nowogrodzkim posłem
I w którego ja domu od dzieciństwa wzrosłem.
Owóż Rejtan na przyjazd księcia jenerała
Zaprosił gości. Liczna szlachta się zebrała,
Było teatrum (książę kochał się w teatrze),
Fajerwerk dawał Kaszyc, który mieszka w Jatrze,
Pan Tyzenhauz tancerzy przysłał, a kapele
Ogiński i pan Sołtan, co mieszka w Zdzieńciele.
Słowem, dawano huczne nad podziw zabawy
W domu, a w lasach wielkie robiono obławy.
Wiadomo zaś waszmościom jest, że prawie wszyscy,
Ile ich zapamiętać można, Czartoryscy,
Choć idą z Jagiellonów krwi, lecz do myślistwa
Nie są bardzo pochopni, pewno nie z lenistwa,
Lecz z gustów cudzoziemskich; i książę jenerał
Częściej do książek niźli do psiarni zazierał
I do alkówek damskich częściej niż do lasów.

    W świcie księcia był książę niemiecki Denassów,
O którym powiadano, że w libijskiej ziemi
Goszcząc, polował niegdyś z królmi murzyńskiemi
I tam tygrysa spisą w ręcznym boju zwalił,
Z czego się bardzo książę ów Denassów chwalił.
U nas zaś polowano na dziki w tę porę;
Rejtan zabił ze sztućca ogromną maciorę,
Z wielkim niebezpieczeństwem, bo z bliska wypalił.
Każdy z nas trafność strzału wydziwiał i chwalił,
Tylko Niemiec Denassów obojętnie słuchał
Pochwał takich i chodząc, pod nos sobie dmuchał:
Że trafny strzał dowodzi tylko śmiałe oko,
Biała broń śmiałą rękę; i zaczął szeroko
Znowu gadać o swojej Libiji i spisie,
O swych królach murzyńskich i o swym tygrysie.
Markotno to się stało panu Rejtanowi.
Był człek żywy, uderzył po szabli i mówi:
»Mości książę! kto patrzy śmiele, walczy śmiele,
Warte dziki tygrysów, a spis karabele«.
I zaczynali z Niemcem dyskurs nazbyt żwawy.
Szczęściem, książę jenerał przerwał te rozprawy,
Godząc ich po francusku: co tam gadał, nie wiem,
Ale ta zgoda był to popiół nad zarzewiem.
Bo Rejtan wziął do serca, okazyi czekał
I dobrą sztukę spłatać Niemcowi przyrzekał;
Tej sztuki ledwie własnym nie przypłacił zdrowiem,
A spłatał ją nazajutrz, jak to wnet opowiem».

    Tu Wojski umilknąwszy prawą rękę wznosił
I u Podkomorzego tabakiery prosił;
Długo zażywa, kończyć powieści nie raczy,
Jak gdyby chciał zaostrzyć ciekawość słuchaczy.
Zaczynał wreszcie, kiedy znowu mu przerwano
Powieść taką ciekawą, tak pilnie słuchaną!
Bo do Sędziego nagle ktoś przysłał człowieka,
Donosząc, że z niezwłocznym interesem czeka.
Sędzia, dając dobranoc, żegnał całe grono.
Natychmiast się po różnych stronach rozpierzchniono:
Ci spać do domu, tamci w stodole na sianie;
Sędzia szedł podróżnemu dawać posłuchanie.

    Inni już śpią. Tadeusz po sieniach się zwija,
Chodząc jako wartownik około drzwi stryja,
Bo musi w ważnych rzeczach rady jego szukać
Dziś jeszcze, nim spać pójdzie. Nie śmie do drzwi stukać;
Sędzia drzwi na klucz zamknął, z kimś tajnie rozmawia;
Tadeusz końca czeka, a ucha nadstawia.

    Słyszy wewnątrz szlochanie. Nie trącając klamek,
Ostrożnie dziurką klucza zagląda przez zamek:
Widzi rzecz dziwną! Sędzia i Robak na ziemi
Klęczeli, objąwszy się i łzami rzewnemi
Płakali; Robak ręce Sędziego całował,
Sędzia księdza za szyję płacząc obejmował.
Wreszcie po ćwierćgodzinnym przerwaniu rozmowy
Robak po cichu tymi odezwał się słowy:

    «Bracie! Bóg wie, żem dotąd tajemnic dochował,
Którem z żalu za grzechy w spowiedzi ślubował:
Że Bogu i Ojczyźnie poświęcony cały,
Nie służąc pysze, ziemskiej nie szukając chwały,
Żyłem dotąd i chciałem umrzeć bernardynem,
Nie wydając nazwiska, nie tylko przed gminem,
Ale nawet przed tobą i przed własnym synem!
Wszakże ksiądz prowincyjał dał mi pozwolenie
In articulo mortis zrobić objawienie.
Kto wie, czy wrócę żywy! kto wie, co się stanie!
W Dobrzynie! Bracie! wielkie, wielkie zamieszanie!
Francuz jeszcze daleko, nim przeminie zima
Trzeba czekać, a szlachta pono nie dotrzyma.
Możem zanadto czynnie z powstaniem się krzątał!
Pono źle zrozumieli! Klucznik wszystko splątał!
Ten wariat Hrabia, słyszę, pobiegł do Dobrzyna,
Nie mogłem go uprzedzić, ważna w tym przyczyna:
Stary Maciek mnie poznał, a jeśli odkryje,
Potrzeba będzie oddać pod Scyzoryk szyję.
Nic Klucznika nie wstrzyma! Mniejsza o mą głowę,
Lecz tym odkryciem, spisku zerwałbym osnowę.
Przecież dziś tam być muszę! Widzieć, co się dzieje,
Choćbym zginął: beze mnie szlachta oszaleje!
Bądź zdrów, najmilszy bracie! bądź zdrów, śpieszyć muszę.
Jeśli zginę, ty jeden westchniesz za mą duszę;
W przypadku wojny, tobie cała tajemnica
Wiadoma: kończ, com zaczął, pomnij, żeś Soplica!»

    Tu ksiądz łzy otarł, habit zapiął, kaptur włożył
I okienicę tylną po cichu otworzył,
Widać było, że oknem do ogrodu skakał;
Sędzia, zostawszy jeden, siadł w krześle i płakał.

    Chwilę czekał Tadeusz, nim w klamkę zadzwonił;
Otworzono mu, cicho wszedł, nisko się skłonił:
«Stryjaszku dobrodzieju — rzekł — ledwie dni kilka
Przebawiłem tu, dni te minęły jak chwilka;
Nie miałem czasu z twoim domem się nacieszyć
I z tobą, a odjeżdżać muszę, muszę spieszyć
Zaraz, dzisiaj, stryjaszku, a jutro najdaléj:
Wszak pamiętacie, żeśmy Hrabiego wyzwali.
Bić się z nim to rzecz moja, posłałem wyzwanie,
W Litwie jest zakazane pojedynkowanie,
Jadę więc na granicę Warszawskiego Księstwa.
Hrabia, prawda, fanfaron, lecz mu nie brak męstwa,
Na miejsce naznaczone zapewne się stawi,
Rozprawim się; a jeśli Bóg pobłogosławi,
Ukarzę go, a potem za Łososny brzegi
Przepłynę, gdzie mnie bratnie czekają szeregi.
Słyszałem, że mi ojciec testamentem kazał
Służyć w wojsku, a nie wiem, kto testament zmazał».

    «Mój Tadeuszku — rzekł stryj — czy waszeć kąpany
W gorącej wodzie, czy też kręcisz jak lis szczwany,
Co indziej kitą wije, a sam indziej bieży?
Wyzwaliśmy, zapewne, i bić się należy.
Ale jechać dziś, skądżeś waszeć tak się zaciął?
Przed pojedynkiem zwyczaj jest posłać przyjaciół,
Układać się. Wszak Hrabia może nas przeprosić,
Deprekować; czekaj waść, czasu jeszcze dosyć.
Chyba inny giez jaki waści stąd wygania,
To gadaj szczerze, po co takie omawiania?
Jestem twój stryj; choć stary, znam, co serce młode;
Byłem ci ojcem (mówiąc gładził go pod brodę),
Już w ucho szepnął o tym mnie mój palec mały,
Że waszeć masz tu jakieś z damami kabały.
Za katy, prędko teraz młódź do dam się bierze!
No, Tadeuszku, przyznaj mi się waść, a szczerze».

    «Jużci — bąknął Tadeusz — prawda: są przyczyny
Inne, kochany stryju, może z mojej winy!
Omyłka! cóż? nieszczęście! już trudno naprawić!
Nie, drogi stryju, dłużej nie mogę tu bawić!
Błąd młodości! Stryjaszku, nie pytaj o więcej,
Ja muszę z Soplicowa wyjeżdżać co prędzej».

    «Ho! — rzekł Stryj — pewnie jakieś miłośne zatargi!
Uważałem, że waszeć wczoraj gryzłeś wargi,
Poglądając spode łba na pewną dziewczynkę;
Widziałem, że i ona miała kwaśną minkę.
Znam ja te wszystkie głupstwa; kiedy dzieci para
Kocha się, to tam u nich nieszczęść co niemiara!
To cieszą się, to znowu trapią się i smucą,
To znowu, Bóg wie o co, do zębów się kłócą,
To stojąc w kątkach jakby mruki, nie gadają
Do siebie, czasem nawet w pole uciekają.
Jeżeli na was raptus podobny napada,
Bądźcie tylko cierpliwi, już jest na to rada;
Biorę na siebie wkrótce przywieść was do zgody.
Znam ja te wszystkie głupstwa, wszakże byłem młody.
Powiedz mi wasze wszystko; ja może nawzajem
Coś odkryję i tak się oba poprzyznajem».

    «Stryjaszku — rzekł Tadeusz, całując mu rękę
I rumieniąc się — powiem prawdę. Tę panienkę,
Zosię, wychowanicę stryja, podobałem
Bardzo, choć tylko parę razy ją widziałem;
A mówią, że stryj dla mnie za żonę przeznacza
Podkomorzankę, piękną i córkę bogacza.
Teraz nie mógłbym z panną Różą się ożenić,
Kiedy kocham tę Zosię; trudno serce zmienić!
Nieuczciwie, żeniąc się z jedną, kochać drugą.
Czas może mnie uleczy; wyjadę — na długo».

    «Tadeuszku — stryj przerwał — to mi dziwny sposób
Kochania się: uciekać od kochanych osób!
Dobrze, żeś szczery; widzisz, głupstwo byś wypłatał,
Odjeżdżając: a co waść powiesz, gdybym swatał
Sam waści Zosię? He? Cóż, nie skoczysz z radości?»

    Tadeusz rzekł po chwili «Dobroć jegomości
Dziwi mnie. Lecz cóż? Łaska stryja dobrodzieja
Nie przyda się już na nic! Ach, próżna nadzieja!
Bo pani Telimena nie odda mi Zosi!»
«Będziem prosić» rzekł Sędzia.

                        «Nikt jej nie uprosi —
Przerwał prędko Tadeusz — nie, czekać nie mogę,
Stryjaszku, muszę prędko, jutro jechać w drogę.
Daj mi, stryjaszku, tylko twe błogosławieństwo,
Wszystko przygotowałem, jadę zaraz w Księstwo».

    Sędzia, wąs kręcąc, z gniewem na chłopca spozierał:
«To waść tak szczery? takeś mi serce otwierał?
Naprzód ów pojedynek, potem znowu miłość
I ten wyjazd; oj, jest tu w tym jakaś zawiłość.
Już mnie gadano, jużem kroki waści badał!
Asan bałamut i trzpiot, asan kłamstwa gadał!
A gdzież to asan chodził onegdaj wieczorem,
Czego asan jak wyżeł tropił pode dworem?
O Tadeuszku! jeśli może asan Zosię
Zbałamucił i teraz uciekasz, młokosie,
To się waści nie uda! Lubisz czy nie lubisz,
Zapowiadam asanu, że Zosię poślubisz;
A nie, to bizun — jutro staniesz na kobiercu!
I gada mnie o czuciach! o niezmiennym sercu!
Łgarz jesteś! pfe! Ja z waści, panie Tadeuszu,
Zrobię śledztwo, ja waści jeszcze natrę uszu!
Dziś dość miałem kłopotów, aż mnie głowa boli;
Ten mi jeszcze spokojnie zasnąć nie dozwoli!
Idź mi waść spać!» To mówiąc, drzwi na wściąż otwierał
I zawołał Woźnego, żeby go rozbierał.

    Tadeusz cicho wyszedł, opuściwszy głowę,
Rozbierał w myśli przykrą ze stryjem rozmowę:
Pierwszy raz połajany tak ostro!… Ocenił
Słuszność wyrzutów, sam się przed sobą rumienił.
Co począć? jeśli Zosia o wszystkim się dowie?
Prosić o rękę? a cóż Telimena powie?
Nie, czuł, że nie mógł dłużej zostać w Soplicowie.

    Tak zadumany ledwie zrobił kroków parę,
Gdy mu coś drogę zaszło; spojrzał: widzi marę,
Całą w bieliźnie, długą, wysmukłą i cienką.
Suwała się ku niemu z wyciągniętą ręką,
Od której odbijał się drżący blask miesięczny,
I przystąpiwszy, cicho jęknęła: «Niewdzięczny!
Szukałeś wzroku mego, teraz go unikasz;
Szukałeś rozmów ze mną, dziś uszy zamykasz,
Jakby w słowach, we wzroku mym była trucizna!
Dobrze mi tak, wiedziałam, kto jesteś: mężczyzna!
Nie znając kokieterii, nie chciałam cię dręczyć,
Uszczęśliwiłam; takżeś umiał mnie zawdzięczyć!
Tryumf nad miękkim sercem serce twe zatwardził;
Żeś je zdobył zbyt łacno, zbyt prędkoś nim wzgardził!
Dobrze mi tak! Lecz straszną nauczona probą,
Wierz mi, iż więcej niż ty gardzę sama sobą!»

    «Telimeno — Tadeusz rzekł — dalbóg nietwarde
Mam serce ani ciebie unikam przez wzgardę;
Ale uważ no sama, wszak nas widzą, śledzą,
Czyż można tak otwarcie? cóż ludzie powiedzą?
Wszak to nieprzyzwoicie, to dalbóg jest grzechem».
«Grzechem! — odpowiedziała mu z gorzkim uśmiechem —
Niewiniątko! baranek! Ja, będąc kobiétą,
Jeśli z miłości nie dbam, choćby mnie odkryto,
Choćby mnie osławiono; a ty, ty mężczyzna?
Cóż szkodzi z was któremu, chociaż się i przyzna,
Że ma romans z dziesięciu razem kochankami?
Mów prawdę: chcesz mnie rzucić?» Zalała się łzami.
«Telimeno, cóż by świat mówił o człowieku —
Rzekł Tadeusz — który by teraz, w moim wieku,
Zdrów, żył na wsi, kochał się: kiedy tyle młodzi,
Tylu żonatych od żon, od dzieci uchodzi
Za granicę, pod znaki narodowe bieży?
Choćbym chciał zostać, czy to ode mnie zależy?
Ojciec mnie testamentem kazał, abym służył
W wojsku polskim, teraz stryj ten rozkaz powtórzył:
Jutro jadę, zrobiłem już postanowienie,
I dalbóg, Telimeno, już go nie odmienię».
«Ja — rzekła Telimena — nie chcę ci zagradzać
Drogi do sławy, szczęściu twojemu przeszkadzać!
Jesteś mężczyzną, znajdziesz kochankę godniejszą
Serca twojego, znajdziesz bogatszą, piękniejszą!
Tylko dla mej pociechy, niech wiem przed rozstaniem,
Że twoja skłonność była prawdziwym kochaniem,
Że to nie był żart tylko, nie rozpusta płocha,
Lecz miłość; niech wiem, że mnie mój Tadeusz kocha!
Niech słowo »kocham« jeszcze raz z ust twych usłyszę,
Niech je w sercu wyryję i w myśli zapiszę.
Przebaczę łacniej, chociaż przestaniesz mnie kochać,
Pomnąc jakoś mnie kochał!» I zaczęła szlochać.

    Tadeusz, widząc że tak płacze i tak błaga
Czule, i tylko takiej drobnostki wymaga,
Wzruszył się, przejęły go szczery żal i litość,
I jeżeliby badał serca swego skrytość,
Może by się w tej chwili i sam nie dowiedział,
Czyli ją kochał, czy nie, więc żywo powiedział:
«Telimeno, bogdaj mnie jasny piorun ubił,
Jeśli nie prawda, żem cię, dalbóg, bardzo lubił,
Czy kochał. Krótkie z sobą spędziliśmy chwile,
Ale one mnie przeszły tak słodko, tak mile,
Że będą długo, zawsze myśli mej przytomne,
I dalibóg, że nigdy ciebie nie zapomnę».

    Telimena skoczywszy padła mu na szyję:
«Tegom się spodziewała! Kochasz mnie, więc żyję!
Bo dzisiaj miałam dni me własną ręką skrócić;
Gdy mnie kochasz mój drogi, czyż możesz mnie rzucić?
Tobie oddałam serce, oddam ci majątek,
Pójdę za tobą wszędzie; każdy świata kątek
Będzie mnie z tobą miły! Z najdzikszej pustyni
Miłość, wierzaj mi, ogród rozkoszy uczyni».

    Tadeusz, wydarłszy się z objęcia przemocą:
«Jak to? — rzekł — czyś z rozumu obrana? gdzie? po co?
Jechać za mną? Ja, będąc sam prostym żołnierzem,
Włóczyć, czy markietankę?» — «To my się pobierzem»
Rzekła mu Telimena. «Nie, nigdy! — zawoła
Tadeusz.— Ja żenić się nie mam teraz zgoła
Zamiaru, ni kochać się. Fraszki! dajmy pokój!
Proszę cię, moja droga, rozmyśl się! uspokój!
Ja jestem tobie wdzięczen, ale niepodobna
Żenić się. Kochajmy się, ale tak — z osobna.
Zostać dłużej nie mogę; nie, nie, jechać muszę.
Bądź zdrowa, Telimeno moja; jutro ruszę».

    Rzekł, nasuwał kapelusz, odwracał się bokiem,
Chcąc iść; lecz go wstrzymała Telimena okiem
I twarzą, jak Meduzy głową. Musiał zostać
Mimowolnie; poglądał z trwogą na jej postać:
Stała blada, bez ruchu, bez tchu i bez życia;
Aż wyciągając rękę jak miecz do przebicia,
Z palcem zmierzonym prosto w Tadeusza oczy:
«Tego chciałam! — krzyknęła — ha, języku smoczy!
Serce jaszczurcze! To nic, żem tobą zajęta
Wzgardziła Asesora, Hrabię i Rejenta,
Żeś mnie uwiodł i teraz porzucił sierotę,
To nic! Jesteś mężczyzną, znam waszą niecnotę,
Wiem, że jak inni, tak ty mógłbyś wiarę złamać,
Lecz nie wiedziałam, że tak podle umiesz kłamać!
Słuchałam pode drzwiami stryja! Więc to dziecko,
Zosia, wpadła ci w oko i na nią zdradziecko
Dybiesz? Zaledwieś jedną nieszczęsną oszukał,
A jużeś pod jej okiem nowych ofiar szukał!
Uciekaj, lecz cię moje dosięgną przekleństwa —
Lub zostań, wydam światu twoje bezeceństwa;
Twe sztuki już nie zwiodą innych, jak mnie zwiodły!
Precz! gardzę tobą! jesteś kłamca, człowiek podły!»

    Na obelgę śmiertelną dla uszu szlachcica,
I której żaden nigdy nie słyszał Soplica,
Zadrżał Tadeusz, twarz mu pobladła jak trupia,
Tupnąwszy nogą, usta ścisnąwszy, rzekł: «Głupia!»

    Odszedł; lecz wyraz «podłość» echem się powtórzył
W sercu. Wzdrygnął się młodzian, czuł, że nań zasłużył,
Czuł, że wyrządził wielką krzywdę Telimenie,
Że go słusznie skarżyła, mówiło sumienie;
Lecz czuł, że po tych skargach tym mocniej ją zbrzydził.
O Zosi, ach! pomyślić nie ważył się, wstydził.
Przecież ta Zosia, taka piękna, taka miła!
Stryj swatał ją! może by jego żoną była,
Gdyby nie szatan, co go plącząc w grzech za grzechem,
W kłamstwo za kłamstwem, wreszcie odstąpił z uśmiechem!
Złajany, pogardzony od wszystkich, w dni parę
Zmarnował przyszłość! Uczuł słuszną zbrodni karę.

    W tej burzy uczuć jakby kotwica spoczynku
Zabłysnęła mu nagle myśl o pojedynku:
«Zamordować Hrabiego! łotra! krzyknął w gniewie,
Zginąć albo zemścić się!» A za co? sam nie wie;
I ten gniew wielki, jak się zajął w mgnieniu oka,
Tak wywietrzał. Znów zdjęła go żałość głęboka,
Myślił: «Jeśli prawdziwe było postrzeżenie,
Że Hrabia z Zosią jakieś ma porozumienie,
I cóż stąd? Może Hrabia kocha Zosię szczerze,
Może go ona kocha, za męża wybierze?
Jakimże prawem chciałbym zerwać to zamęście,
I, sam nieszczęśnik, wszystkich mam zaburzać szczęście?»

    Wpadł w rozpacz i nie widział innego sposobu,
Chyba ucieczkę prędką; gdzie? chyba do grobu!

    Więc kułak przycisnąwszy na schylonym czole,
Biegł ku łąkom, gdzie stawy błyszczały się w dole,
I stanął nad błotnistym; w zielonawe tonie
Łakomy wzrok utopił i błotniste wonie
Z rozkoszą ciągnął piersią, i otworzył usta
Ku nim. Bo samobójstwo jak każda rozpusta
Jest wymyślną; on w głowy szalonym zawrocie
Czuł niewymowny pociąg utopić się w błocie.

    Lecz Telimena z dzikiej młodzieńca postawy
Zgadując rozpacz, widząc że pobiegł nad stawy,
Chociaż ku niemu takim słusznym gniewem pała,
Przelękła się; w istocie dobre serce miała.
Żal jej było, że inną śmiał Tadeusz lubić,
Chciała go skarać, ale nie myśliła zgubić.
Więc puściła się za nim, wznosząc ręce obie,
Krzycząc: «Stój! głupstwo! kochaj czy nie! żeń się sobie
Czy jedź! tylko stój!» Ale on już szybkim biegiem
Wyprzedził ją daleko; już stanął nad brzegiem.

    Dziwnym zrządzeniem losów, po tym samym brzegu
Jechał Hrabia na czele dżokejów szeregu,
A zachwycony wdziękiem nocy tak pogodnej
I harmonią cudną orkiestry podwodnej,
Owych chorów, co brzmiały jak arfy eolskie,
(Żadne żaby nie grają tak pięknie jak polskie),
Wstrzymał konia i o swej zapomniał wyprawie,
Zwrócił ucho do stawu i słuchał ciekawie.
Oczy wodził po polach, po niebios obszarze:
Pewnie układał w myśli nocne peizaże.

    Zaiste, okolica była malownicza!
Dwa stawy pochyliły ku sobie oblicza
Jako para kochanków: prawy staw miał wody
Gładkie i czyste jako dziewicze jagody;
Lewy, ciemniejszy nieco, jako twarz młodziana
Smagława i już męskim puchem osypana.
Prawy złocistym piaskiem połyskał się wkoło,
Jak gdyby włosem jasnym; a lewego czoło
Najeżone łozami, wierzbami czubate;
Oba stawy ubrane w zieloności szatę.

    Z nich dwa strugi, jak ręce związane pospołu,
Ściskają się. Strug dalej upada do dołu;
Upada, lecz nie ginie, bo w rowu ciemnotę
Unosi na swych falach księżyca pozłotę;
Woda warstami spada, a na każdej warście
Połyskają się blasku miesięcznego garście,
Światło w rowie na drobne drzazgi się roztrąca,
Chwyta je i w głąb niesie toń uciekająca,
A z góry znów garściami spada blask miesiąca.
Myślałbyś, że u stawu siedzi Świtezianka,
Jedną ręką zdrój leje z bezdennego dzbanka,
A drugą ręką w wodę dla zabawki miota
Brane z fartuszka garście zaklętego złota.

    Dalej, z rowu wybiegłszy, strumień na równinie
Rozkręca się, ucisza, lecz widać że płynie,
Bo na jego ruchomej, drgającej powłoce
Wzdłuż miesięczne światełko drgające migoce.
Jako piękny wąż żmudzki, zwany giwojtosem,
Chociaż zdaje się drzemać, leżąc między wrzosem,
Pełźnie, bo na przemiany srebrzy się i złoci,
Aż nagle zniknie z oczu we mchu lub paproci:
Tak strumień kręcący się chował się w olszynach,
Które na widnokręgu czerniały kończynach,
Wznosząc swe kształty lekkie, niewyraźne oku,
Jak duchy na wpół widne, na poły w obłoku.

    Między stawami w rowie młyn ukryty siedzi.
Jako stary opiekun, co kochanków śledzi,
Podsłuchał ich rozmowę, gniewa się, szamoce,
Trzęsie głową, rękami, i groźby bełkoce:
Tak ów młyn nagle zatrząsł mchem obrosłe czoło
I palczastą swą pięścią wykręcając wkoło,
Ledwo klęknął i szczęki zębowate ruszył,
Zaraz miłośną stawów rozmowę zagłuszył
I zbudził Hrabię.

                        Hrabia widząc, że tak blisko
Tadeusz naszedł jego zbrojne stanowisko,
Krzyczy: «Do broni! łapaj!» Skoczyli dżokeje;
Nim Tadeusz rozeznać mógł, co się z nim dzieje,
Już go chwycili. Biegą do dworu, w podwórze
Wpadają. Dwór budzi się, psy w hałas, w krzyk stróże.
Wyskoczył wpół ubrany Sędzia; widzi zgraję
Zbrojną, myśli, że zbójcy, aż Hrabię poznaje.
«Co to jest?» pyta. Hrabia szpadą nad nim mignął,
Lecz widząc bezbronnego w zapale ostygnął:
«Soplico — rzekł — odwieczny wrogu mej rodziny,
Dziś skarzę cię za dawne i za świeże winy,
Dziś zdasz mi sprawę z mojej fortuny zaboru,
Nim pomszczę się obelgi mojego honoru!»

    Lecz Sędzia, żegnając się, krzyknął: «W Imię Ojca
I Syna! tfu! mospanie Hrabia, czy waść zbojca?
Przebóg! czy się to zgadza z pana urodzeniem,
Wychowaniem i z pana na świecie znaczeniem?
Nie pozwolę skrzywdzić się!» Wtem Sędziego słudzy
Biegli, jedni z kijami, ze strzelbami drudzy;
Wojski, stojąc z daleka, poglądał ciekawie
W oczy panu Hrabiemu, a nóż miał w rękawie.

    Już mieli zacząć bitwę, lecz Sędzia przeszkodził;
Próżno było bronić się, nowy wróg nadchodził:
Postrzeżono w olszynie blask, wystrzał rusznicy!
Most na rzece zahuczał tętentem konnicy
I «Hejże na Soplicę!» tysiąc głosów wrzasło.
Wzdrygnął się Sędzia: poznał Gerwazego hasło;
«Nic to — zawołał Hrabia — będzie tu nas więcéj,
Poddaj się Sędzio, to są moi sprzymierzeńcy».

    Wtem Asesor nadbiegał, krzycząc: «Areszt kładę
W imię Imperatorskiej Mości; oddaj szpadę,
Panie Hrabio, bo wezwę wojskowej pomocy,
A wiesz pan, że kto zbrojnie śmie napadać w nocy,
Zastrzeżono tysiącznym dwóchsetnym ukazem,
Że jak zło…» Wtem go Hrabia w twarz uderzył płazem.
Padł zgłuszony Asesor i skrył się w pokrzywy;
Wszyscy myśleli, że był ranny lub nieżywy.

    «Widzę — rzekł Sędzia — że się na rozbój zanosi».
Jęknęli wszyscy; wszystkich zagłuszył wrzask Zosi,
Która krzyczała, Sędzię objąwszy rękami,
Jako dziecko od Żydów kłute igiełkami.

    Tymczasem Telimena wpadła między konie,
Wyciągnęła ku Hrabi załamane dłonie:
«Na twój honor! — krzyknęła przeraźliwym głosem,
Z głową w tył wychyloną, z rozpuszczonym włosem —
Przez wszystko co jest świętym, na klęczkach błagamy!
Hrabio, śmieszże odmówić? proszą ciebie damy;
Okrutniku, nas pierwej musisz zamordować!»
Padła zemdlona. Hrabia skoczył ją ratować,
Zadziwiony i nieco zmieszany tą sceną:
«Panno Zofio — rzecze — pani Telimeno!
Nigdy się krwią bezbronnych ta szpada nie splami;
Soplicowie! jesteście moimi więźniami.
Tak zrobiłem we Włoszech, kiedy pod opoką,
Którą Sycylianie zwą Birbante-rokką,
Zdobyłem tabor zbójców: zbrojnych mordowałem,
Rozbrojonych zabrałem i związać kazałem;
Szli za końmi i tryumf mój zdobili świetny,
Potem ich powieszono u podnóża Etny».

    Było to osobliwsze szczęście dla Sopliców,
Że Hrabia, mając lepsze konie od szlachciców
I chcąc spotkać się pierwszy, zostawił ich w tyle
I biegł przed resztą jazdy, przynajmniej o milę,
Ze swym dżokejstwem, które posłuszne i karne,
Stanowiło niejako wojsko regularne;
Gdy inna szlachta była, zwyczajem powstania,
Burzliwa i niezmiernie skora do wieszania.

    Hrabia miał czas ostygnąć z zapału i gniewu,
Przemyślał, jakby skończyć bój bez krwi rozlewu;
Więc rodzinę Sopliców w domu zamknąć każe
Jako więźniów wojennych; u drzwi stawi straże.

    Wtem «Hejże na Sopliców!» Wpada szlachta hurmem,
Obstępuje dwór wkoło i bierze go szturmem,
Tym łacniej, że wódz wzięty i pierzchła załoga;
Lecz zdobywcy chcą bić się, wyszukują wroga.
Do domu niewpuszczeni biegą do folwarków,
Do kuchni. Gdy do kuchni weszli, widok garków,
Ogień ledwie zagasły, potraw zapach świeży,
Chrupanie psów gryzących ostatki wieczerzy,
Chwyta wszystkich za serca, myśl wszystkich odmienia,
Studzi gniewy, zapala potrzebę jedzenia.
Marszem i całodziennym znużeni sejmikiem,
«Jeść! jeść!» po trzykroć zgodnym wezwali okrzykiem,
Odpowiedziano: «Pić! pić!»; między szlachty zgrają
Stają dwa chóry: ci pić, a ci jeść wołają.
Odgłos leci echami; gdzie tylko dochodzi,
Wzbudza oskomę w ustach, głód w żołądkach rodzi.
I tak na dane z kuchni hasło, niespodzianie
Rozeszła się armija na furażowanie.

    Gerwazy, od pokojów Sędziego odparty,
Ustąpić musiał przez wzgląd dla Hrabiowskiej warty.
Więc nie mogąc zemścić się na nieprzyjacielu,
Myślił o drugim wielkim tej wyprawy celu.
Jako człek doświadczony i biegły w prawnictwie,
Chce Hrabiego osadzić na nowym dziedzictwie
Legalnie i formalnie: więc za Woźnym biega,
Aż go po długich śledztwach za piecem dostrzega,
Wnet porywa za kołnierz, na dziedziniec wlecze
I zmierzywszy mu w piersi Scyzoryk, tak rzecze:
«Panie Woźny, pan Hrabia śmie waćpana prosić,
Abyś raczył przed szlachtą bracią wnet ogłosić
Intromisyją Hrabi do zamku, do dworu
Sopliców, do wsi, gruntów zasianych, ugoru,
Słowem, cum gais, boris et graniciebus,
Kmetonibus, scultetis, et omnibus rebus
Et quibusdam aliis. Jak tam wiesz, tak szczekaj,
Nic nie opuszczaj!» «Panie Kluczniku, zaczekaj
— Rzekł śmiało, ręce za pas włożywszy Protazy —
Gotów jestem wypełniać wszelkie stron rozkazy,
Ale ostrzegam, że akt nie będzie miał mocy,
Wymuszony przez gwałty, ogłoszony w nocy».
«Co za gwałty — rzekł Klucznik — tu nie ma napaści,
Wszak proszę pana grzecznie; jeśli ciemno waści,
To Scyzorykiem skrzesam ognia, że waszeci
Zaraz w ślepiach jak w siedmiu kościołach zaświeci».

    «Gerwazeńku — rzekł Woźny — po co się tak dąsać?
Jestem Woźny, nie moja rzecz sprawę roztrząsać;
Wszak wiadomo, że strona Woźnego zaprasza
I dyktuje mu, co chce, a Woźny ogłasza.
Woźny jest posłem prawa, a posłów nie karzą,
Nie wiem tedy, za co mnie trzymacie pod strażą.
Wnet akt spiszę, niech mi kto latarkę przyniesie,
A tymczasem ogłaszam: bracia, uciszcie się!»

    I by donośniej mówić, wstąpił na stos wielki
Belek (pod płotem sadu suszyły się belki),
Wlazł na nie i zarazem jakby go wiatr zdmuchnął,
Zniknął z oczu. Słyszano, jak w kapustę buchnął;
Widziano, po konopiach ciemnych jego biała
Konfederatka niby gołąb przeleciała.
Konewka strzelił w czapkę, ale chybił celu;
Wtem zatrzeszczały tyki, już Protazy w chmielu.
«Protestuję!» zawołał; pewny był ucieczki,
Bo za sobą miał łozę i bagniska rzeczki.

    Po tej protestacyi, która się ozwała
Jak na zdobytych wałach ostatni strzał działa,
Ustał już wszelki opór w Soplicowskim dworze.
Szlachta głodna plądruje, zabiera co może:
Kropiciel, stanowisko zająwszy w oborze,
Jednego wołu i dwa cielce w łby zakropił,
A Brzytewka im szable w gardzielach utopił;
Szydełko równie czynnie używał swej szpadki,
Kabany i prosięta koląc pod łopatki.
Już rzeź zagraża ptastwu. Czujne gęsi stado,
Co niegdyś ocaliło Rzym przed Galów zdradą,
Darmo gęga o pomoc; zamiast Manlijusza,
Wpada w kotuch Konewka, jedne ptaki zdusza,
A drugie żywcem wiąże do pasa kontusza.
Próżno gęsi szyjami wywijając, chrypią,
Próżno gęsiory sycząc, napastnika szczypią;
On bieży osypany iskrzącym się puchem,
Unoszony jak kółmi gęstych skrzydeł ruchem,
Zdaje się być chochlikiem, skrzydlatym złym duchem.

    Ale rzeź najstraszniejsza, chociaż najmniej krzyku,
Między kurami. Młody Sak wpadł do kurniku
I z drabinek, stryczkami łowiąc, ciągnie z góry
Kogutki i szurpate, i czubate kury,
Jedne po drugich dusi i składa do kupy,
Ptastwo piękne, karmione perłowymi krupy.
Niebaczny Saku, jakiż zapał cię unosi!
Nigdy już odtąd gniewnej nie przebłagasz Zosi.

    Gerwazy przypomina starodawne czasy:
Każe sobie podawać od kontuszów pasy
I nimi z Soplicowskiej piwnicy dobywa
Beczki starej siwuchy, dębniaku i piwa.
Jedne wnet odgwożdżono, a drugie ochoczo
Szlachta, gęsta jak mrowie, porywają, toczą
Do zamku; tam na nocleg cały tłum się zbiera,
Tam założona główna Hrabiego kwatera.

    Nakładają sto ognisk, warzą, skwarzą, pieką,
Gną się stoły pod mięsem, trunek płynie rzeką;
Chce szlachta noc tę przepić, przejeść i prześpiewać.
Lecz powoli zaczęli drzemać i poziewać;
Oko gaśnie za okiem, i cała gromada
Kiwa głowami, każdy, gdzie siedział, tam pada:
Ten z misą, ten nad kotłem, ten przy wołu ćwierci.
Tak zwycięzców zwyciężył w końcu sen, brat śmierci.




Księga dziewiąta



Bitwa

O niebezpieczeństwach wynikających z nieporządnego obozowania — Odsiecz niespodziana — Smutne położenie szlachty — Odwiedziny kwestarskie są wróżbą ratunku — Major Płut zbytnią zalotnością ściąga na siebie burzę — Wystrzał z krócicy, hasło boju — Czyny Kropiciela, czyny i niebezpieczeństwa Maćka — Konewka zasadzką ocala Soplicowo — Posiłki jezdne, atak na piechotę — Czyny Tadeusza — Pojedynek dowódców przerwany zdradą — Wojski stanowczym manewrem przechyla szalę boju — Czyny krwawe Gerwazego — Podkomorzy zwycięzca wspaniałomyślny.

    A chrapali tak twardym snem, że ich nie budzi
Blask latarek i wniście kilkudziesiąt ludzi,
Którzy wpadli na szlachtę jak pająki ścienne,
Nazwane *kosarzami*, na muchy wpółsenne:
Zaledwie która bzyknie, już długimi nogi
Obejmuje ją wkoło i dusi mistrz srogi.
Sen szlachecki był jeszcze twardszy niż sen muszy:
Żaden nie bzyka, leżą wszyscy jak bez duszy,
Chociaż byli chwytani silnymi rękoma
I przewracani jako na przewiąsłach słoma.

    Tylko jeden Konewka, któremu w powiecie
Nie znajdziesz równie mocnej głowy przy bankiecie,
Konewka, co mógł wypić lipcu dwa antały
Nim mu splątał się język i nogi zachwiały:
Ten, choć długo ucztował i usnął głęboko,
Dawał przecie znak życia. Przemknął jedno oko
I widzi… istne zmory! Dwie okropne twarze
Tuż nad sobą, a każda ma wąsów po parze,
Dyszą nad nim, ust jego tykają wąsami,
I czworgiem rąk wokoło wiją jak skrzydłami.
Zląkł się, chciał przeżegnać się: darmo rękę chwyta,
Ręka prawa jak gdyby do boku przybita;
Ruszył lewą: niestety! czuje, że go duchy
Spowiły ciasno jako niemowlę w pieluchy.
Zląkł się jeszcze okropniej, wnet oko zawiera,
Leży nie dysząc, stygnie, ledwie nie umiera!

    Lecz Kropiciel zerwał się bronić się: po czasie!
Bo już był skrępowany we swym własnym pasie.
Przecież zwinął się i tak sprężyście podskoczył,
Że padł na piersi sennych, po głowach się toczył,
Miotał się jako szczupak, gdy się w piasku rzuca,
A ryczał jako niedźwiedź, bo miał silne płuca.
Ryczał: «Zdrada!» — Wnet cała zbudzona gromada
Chórem odpowiedziała: «Zdrada! gwałtu! zdrada!»

    Krzyk dochodzi echami zwierciadlanej sali,
Kędy Hrabia, Gerwazy i dżokeje spali.
Przebudza się Gerwazy: darmo się wydziera,
Związany w kij do swego własnego rapiera;
Patrzy: widzi przy oknie ludzi uzbrojonych,
W czarnych krótkich kaszkietach, w mundurach zielonych.
Jeden z nich, opasany szarfą, trzymał szpadę
I ostrzem jej kierował swych drabów gromadę,
Szepcąc: «Wiąż! wiąż!» Dokoła leżą jak barany
Dżokeje w pętach; Hrabia siedzi niezwiązany
Lecz bezbronny; przy nim dwaj z gołymi bagnety
Stoją drabi. Poznał ich Gerwazy, niestety!
Moskale!!!

                        Nieraz Klucznik był w podobnych trwogach,
Nieraz miewał powrozy na ręku i nogach,
A przecież się uwalniał; wiedział o sposobie
Rwania więzów, był silny bardzo, ufał sobie.
Przemyślał ratować się milczkiem. Oczy zmrużył,
Niby śpi; z wolna ręce i nogi przedłużył,
Dech wciągnął, brzuch i piersi ścisnął co najwężéj:
Aż jednym razem kurczy, wydyma się, pręży;
Jak wąż głowę i ogon gdy chowa w przeguby,
Tak Gerwazy z długiego stał się krótki, gruby;
Rozciągnęły się, nawet skrzypnęły powrozy,
Ale nie pękły! Klucznik ze wstydu i zgrozy
Przewrócił się i w ziemię schowawszy twarz gniewną,
Zamknąwszy oczy, leżał nieczuły jak drewno.

    Wtem ozwały się bębny; naprzód z rzadka, potem
Coraz gęstszym i coraz głośniejszym łoskotem.
Na ten apel rozkazał oficer Moskali,
Dżokejów z Hrabią zamknąć pod strażą na sali,
Szlachtę wieść na dwór, kędy stała druga rota.
Nadaremnie Kropiciel dąsa się i miota.

    Sztab stał we dworze, a z nim zbrojnej szlachty wiele:
Podhajscy, Birbaszowie, Hreczechy, Biergele,
Wszyscy Sędziego krewni albo przyjaciele;
Na odsiecz mu przybiegli słysząc o napadzie,
Zwłaszcza, że z Dobrzyńskimi byli z dawna w zwadzie.

    Kto z wiosek batalijon Moskalów sprowadził?
Kto tak prędko sąsiedztwo z zaścianków zgromadził?
Asesor li, czy Jankiel? Różnie słychać o tem,
Lecz nikt pewnie nie wiedział ni wtenczas, ni potem.

    Już też i słońce wschodzi, krwawo się czerwieni;
Brzegiem tępym, jak gdyby odartym z promieni,
Na wpół widne, na poły w czerni chmur się chowa,
Jak rozżarzona w węglach kowalskich podkowa.
Wiatr wzmagał się i pędził obłoki ze wschodu,
Gęste i poszarpane jako bryły lodu;
Każdy obłok w przelocie deszczem zimnym prószy,
Z tyłu za nim wiatr leci i deszcz znowu suszy,
Za wiatrem znowu obłok nadbiega wilgotny:
I tak dzień na przemiany był chłodny i słotny.

    Tymczasem Major belki schnące pode dworem
Każe wlec, w każdej belce wysiekać toporem
Półokrągłe otwory, w te otwory wtyka
Nogi więźniów i drugą belką je zamyka:
Oba drewna, gwoździami przebite po rogach,
Ścisnęły się jako psie paszczęki na nogach;
Zaś powrozami mocniej sznurowano ręce
Na plecach szlachty. Major ku większej ich męce
Kazał pierwej pozdzierać z głów konfederatki,
Z pleców płaszcze, kontusze, nawet taratatki,
Nawet żupany. I tak szlachta skuta w kłodzie
Siedziała rzędem, dzwoniąc zębami na chłodzie
I na deszczu, bo coraz wzmagała się słota.
Nadaremnie Kropiciel dąsa się i miota.

    Darmo Sędzia za szlachtą instancję wnosi,
I Telimena łączy prośby do łez Zosi,
Ażeby miano większy wzgląd na niewolników.
Wprawdzie oficer rotny, pan Nikita Ryków,
Moskal, lecz dobry człowiek, dał się udobruchać:
Cóż, kiedy sam majora Płuta musiał słuchać.

    Ten Major, Polak rodem z miasteczka Dzierowicz,
Nazywał się (jak słychać) po polsku Płutowicz,
Lecz przechrzcił się; łotr wielki, jak się zwykle dzieje
Z Polakiem, który w carskiej służbie zmoskwicieje.
Płut stał z fajką przed frontem, w boki się podpierał
I gdy mu kłaniano się, nos w górę zadzierał,
A za odpowiedź, na znak gniewnego humoru
Wypuścił z ust kłąb dymu i poszedł do dworu.

    A tymczasem Rykowa Sędzia ułagadza,
I Asesora także na bok odprowadza;
Przemyślają, jak by rzecz zakończyć bez sądu,
A co jeszcze ważniejsza, bez mieszań się rządu.
Więc do majora Płuta rzekł kapitan Ryków:

    «Panie Major! co nam z tych wszystkich niewolników?
Oddamy pod sąd? będzie szlachcie wielka bieda,
A panu Majorowi nikt za to nic nie da.
Wiesz co Major? ot lepiej tę sprawę zagodzić,
Pan Sędzia Majorowi musi trud nagrodzić,
My powiemy, że my tu przyszli dla wizyty,
A tak i kozy całe i wilk będzie syty.
Przysłowie ruskie: wszystko można, lecz ostrożnie;
I to przysłowie: sobie piecz na carskim rożnie;
I to przysłowie: lepsza zgoda od niezgody,
Zaplątaj dobrze węzeł, końce wsadź do wody.
Raportu nie podamy, tak się nikt nie dowie.
Bóg dał ręce żeby brać: to ruskie przysłowie».

    Słysząc to Major wstaje i od gniewu parska:
«Czy ty oszalał, Ryków? To służba cesarska:
A służba nie jest drużba, stary, głupi Ryków!
Czy ty oszalał? Ja mam puszczać buntowników!
W takim wojennym czasie! Ha, pany Polaki,
Ja was nauczę buntu! Ha, szlachta łajdaki,
Dobrzyńscy, oj ja znam was, niech łajdaki mokną!
(I zaśmiał się na całe gardło, patrząc w okno)
Wszakże ten sam Dobrzyński, co siedzi w surducie,
— Hej zdjąć mu surdut! — w roku przeszłym na reducie
Zaczął ze mną tę kłótnię; kto zaczął? on, nie ja.
On, gdy tańczyłem, krzyknął: »Precz za drzwi złodzieja!«
Że wtenczas za pułkowej okradzenie kasy
Byłem pod śledztwem, miałem wielkie ambarasy:
A jemu co do tego? Ja tańczę mazura,
On krzyczy z tyłu: »Złodziej!« szlachta za nim: »Ura!«
Skrzywdzili mnie — a co? wpadł w me szpony szlachciura!
Mówiłem: »Ej Dobrzyński! ej, przyjdzie do woza
Koza« — a co, Dobrzyński? widzisz: będzie łoza!»

    Potem Sędziemu szepnął, schyliwszy się w ucho:
«Jeśli chcesz Sędzio, żeby to uszło na sucho,
Za każdą głowę tysiąc rubelków gotówką:
Tysiąc rubelków Sędzio, to ostatnie słówko».

    Sędzia chciał targować się; lecz Major nie słuchał,
Znowu biegał po izbie, dymem gęsto buchał,
Podobny do szmermelu albo do rakiety.
Chodziły za nim prosząc i płacząc kobiety.
«Majorze — mówił Sędzia — choć pozwiesz do prawa;
Cóż wygrasz? Tu nie zaszła żadna bitwa krwawa,
Nie było ran; że zjedli kury i półgąski,
Za to wedle statutu zapłacą nawiązki.
Ja na pana Hrabiego nie zanoszę skargi;
To tylko były zwykłe sąsiedzkie zatargi».

    «A czy Sędzia — rzekł Major — żółtą księgę czytał?»
«Co to za żółta księga?» pan Sędzia zapytał.
«Księga — rzekł Major — lepsza niż wasze statuty,
A w niej pisze co słowo: stryczek, Sybir, knuty;
Księga ustaw wojennych, teraz w Litwie całéj
Ogłoszonych: już pod stół wasze trybunały!
Podług ustaw wojennych, za takową psotę,
Pójdziecie już to najmniej w sybirną robotę».
«Apeluję — rzekł Sędzia — do gubernatora».
«Apeluj — rzekł Płut — choćby do Imperatora.
Wiesz, że gdy imperator zatwierdza ukazy,
Z łaski swej często karę powiększa dwa razy.
Apelujcie, ja może wynajdę w potrzebie,
Mospanie Sędzio, dobry kruczek i na ciebie.
Wszak Jankiel, szpieg, którego już rząd dawno śledzi,
Jest twoim domownikiem, w karczmie twojej siedzi.
Mogę teraz was wszystkich wziąć w areszt od razu».
«Mnie — rzekł Sędzia — brać w areszt? jak śmiesz bez rozkazu?»
I przychodziło coraz do żywszego sporu:
Gdy nowy gość zajechał na dziedziniec dworu.

    Wjazd tłumny, dziwny. Przodem, niby laufer, bieży
Ogromny czarny baran, a łeb mu się jeży
Czterema rogami, z których dwa jako kabłąki
Kręcą się koło uszu, ubrane we dzwonki,
A dwa od czoła na bok wysuwając końce,
Wstrząsają kulki krągłe, mosiężne, brzęczące.
Za baranem szły woły, trzoda owiec, kozy,
Za bydłem cztery ciężko pakowane wozy.

    Wszyscy odgadli, że to wjazd księdza kwestarza.
Więc pan Sędzia, powinność znając gospodarza,
Stał w progu witać gościa. Ksiądz na pierwszej bryce
Jechał, kapturem na wpół zasłoniwszy lice,
Ale go wnet poznano: bo gdy więźniów minął,
Zwrócił się ku nim twarzą, palcem na znak skinął.
I drugiej bryki furman równie był poznany:
Stary Maciek-Rózeczka, za chłopa przebrany.
Szlachta zaczęła krzyczeć, skoro się pokazał,
On rzekł: «Głupi!» … i ręką milczenie nakazał.
Na trzecim wozie Prusak w kubraku wytartym,
A pan Zan z Mickiewiczem jechali na czwartym.

    A tymczasem, Podhajscy i Isajewicze,
Birbasze, Wilbikowie, Biergiele, Kotwicze,
Widząc szlachtę Dobrzyńskich w tej ciężkiej niewoli,
Zaczęli z dawnych gniewów ostygać powoli:
Bo szlachta polska, chociaż niezmiernie kłótliwa
I porywcza do bitew, przecież nie jest mściwa.
Biega więc do Macieja starego po radę.
On koło wozów całą ustawia gromadę,
Każe czekać.

                        Bernardyn wstąpił do pokoju.
Zaledwie go poznano, choć nie zmienił stroju:
Tak przybrał inną postać. Zwyczajnie ponury,
Zamyślony: a teraz głowę wzniósł do góry,
I z miną rozjaśnioną, jak kwestarz rubacha,
Nim zaczął gadać, długo śmiał się:

                        «Cha, cha, cha, cha,
Kłaniam, kłaniam! Cha, cha, cha, wyśmienicie, przednie!
Panowie oficery, kto poluje we dnie,
Wy w nocy! Dobry połów: widziałem zwierzynę;
Oj skubać, skubać szlachtę, oj drzeć z nich łupinę!
Oj weźcież ich na munsztuk, bo też szlachta bryka!
Winszuję ci Majorze, żeś złowił Hrabika:
To tłuścioszek, to bogacz, panicz z antenatów;
Nie wypuszczaj go z klatki bez trzysta dukatów.
A jak weźmiesz, na klasztor daj jakie trzy grosze,
I dla mnie! bo ja zawżdy za twą duszę proszę.
Jakem bernardyn, bardzo myślę o twej duszy!
Śmierć i sztabsoficerów porywa za uszy!
Dobrze napisał Baka, że śmierć dżga za katy
W szkarłaty, i po suknie nieraz dobrze stuknie,
I po płótnie tak utnie jak i po kapturze,
I po fryzurze równie jak i po mundurze.
Śmierć matula, powiada Baka, jak cebula,
Łzy wyciska, gdy ściska, a równie przytula
I dziecko co się lula, i zucha co hula!
Ach! ach! Majorze, dzisiaj żyjem, jutro gnijem,
To tylko nasze, co dziś zjemy i wypijem!
Panie Sędzio, wszakże to czas podobno śniadać?
Siadam za stół, i proszę wszystkich za mną siadać
Majorze, gdyby zrazów? panie poruczniku,
Co myślisz? gdyby wazę dobrego ponczyku?»

    «To prawda ojcze — rzekli dwaj oficerowie —
Czas by już zjeść i wypić pana Sędzi zdrowie!»

    Zdziwili się domowi, patrząc na Robaka,
Skąd mu się wzięła mina i wesołość taka.
Sędzia wnet kucharzowi powtórzył rozkazy:
Wniesiono wazę, cukier, butelki i zrazy.
Płut i Ryków tak czynnie zaczęli się zwijać,
Tak łakomie połykać i gęsto zapijać,
Że w pół godziny zjedli dwadzieścia trzy zrazy
I wychylili ponczu ogromne pół wazy.

    Więc Major syt i wesół w krześle się rozwalił,
Dobył fajkę, biletem bankowym zapalił,
I otarłszy śniadanie z ust końcem serwety,
Obrócił śmiejące się oczy na kobiety,
I rzekł: «Ja, piękne panie, lubię was jak wety!
Na me szlify majorskie: gdy człek zjadł śniadanie,
Najlepszą jest po zrazach zakąską gadanie
Z paniami tak pięknymi jak wy, piękne panie!
Wiecie co? grajmy w karty? w welba-cwelba? w wista?
Albo pójdźmy mazurka? he! do diabłów trzysta!
Wszak ja w jegerskim pułku pierwszy mazurzysta!»
Za czym ku damom bliżej chylił się wygięty,
I puszczał na przemiany dym i komplementy.

    «Tańczyć! — zawołał Robak — gdy wychylę flaszę,
To i ja, choć ksiądz, habit czasami podkaszę
I potańczę mazurka! Ale wiesz, Majorze,
My tu pijem, a jegry tam zmarzną na dworze?
Hulać to hulać! Sędzio, daj beczkę siwuchy:
Major pozwoli, niechaj piją jegry zuchy!»
«Prosiłbym — rzecze Major — lecz w tym nie ma musu».
«Daj Sędzio — szepnął Robak — beczkę spirytusu».
I tak, kiedy we dworze sztab wesoły łyka,
Za domem zaczęła się w wojsku pijatyka.

    Ryków kapitan milczkiem kielichy wychylał,
Lecz Major pił i razem damom się przymilał.
A wzmagał się w nim coraz tańcowania zapał.
Rzucił fajkę i rękę Telimeny złapał:
Chciał tańczyć, lecz uciekła; więc podszedł do Zosi,
Kłaniając się, słaniając, do mazurka prosi:
«Hej ty, Ryków, przestańże tam trąbić na fajce;
Precz fajka, wszak ty dobrze grasz na bałabajce.
Widzisz no tam gitarę, pódź no, weź gitarę
I mazurka! Ja, Major, idę w pierwszą parę».
Kapitan wziął gitarę i struny przykręcał,
Płut znowu Telimenę do tańca zachęcał.

    «Słowo majorskie, panno: nie Rosyjaninem
Jestem, jeżeli kłamię; chcę być sukinsynem,
Jeżeli kłamię: spytaj, a oficerowie
Wszyscy poświadczą, cała armija to powie:
Że w tej drugiej armiji, w korpusie dziewiątym,
W drugiej pieszej dywizji, w pułku pięćdziesiątym
Jegerskim, major Płut jest pierwszy mazurzysta.
Pódźże panienko! nie bądź taka narowista!
Bo ja po oficersku ukarzę panienkę…»

    To mówiąc skoczył, chwycił Telimeny rękę,
I szerokim całusem w blade ramię klasnął;
Gdy Tadeusz, przypadłszy z boku, w twarz mu trzasnął.
I całus, i policzek ozwały się razem,
Jeden za drugim, jako wyraz za wyrazem.

    Major osłupiał, oczy przetarł, z gniewu blady
Zawołał: «Bunt! buntownik!» i dobywszy szpady,
Biegł przebić. Wtem ksiądz dostał z rękawa krócicę:
«Pal, Tadeuszku! — krzyknął — pal jak w jasną świécę!»
Tadeusz wnet pochwycił, wymierzył, wypalił,
Chybił, ale Majora zgłuszył i osmalił.
Porywa się z gitarą Ryków: «Bunt! bunt!» woła,
Wpada na Tadeusza; lecz Wojski zza stoła
Machnął ręką na odlew; nóż w powietrzu świsnął
Między głowy i pierwej uderzył, niż błysnął;
Uderza w dno gitary, na wylot ją wierci,
Schylił się na bok Ryków i tak uszedł śmierci,
Lecz strwożył się. Krzyknąwszy: «Jegry! bunt! Jej Bogu!»
Dobył szpady, broniąc się, zbliżał się do progu.

    Wtem, z drugiej strony izby wpada szlachty wiele
Przez okna, z rapierami, Rózeczka na czele.
Płut w sieni, Ryków za nim, wołają żołnierzy.
Już trzech najbliższych domu na pomoc im bieży,
Już przeze drzwi włażą trzy błyszczące bagnety,
A za nimi trzy czarne schylone kaszkiety.
Maciek stał u drzwi z Rózgą wzniesioną do góry,
Lgnąc do ściany, czatował jako kot na szczury,
Aż ciął okropnie: może głowy by trzy zwalił;
Lecz stary czy nie dojrzał, czy zbyt się zapalił:
Bo nim szyję wytknęli, rąbnął po kaszkietach,
Zdarł je; Rózga spadając brzękła po bagnetach.
Moskale cofają się, Maciek ich wygania
Na dziedziniec.

                        Tam jeszcze więcej zamieszania.
Tam stronnicy Sopliców pracują w zawody
Nad rozkuciem Dobrzyńskich, rozrywają kłody.
Widząc to, jegry za broń porywają, biegą.
Sierżant wpadłszy bagnetem przebił Podhajskiego,
Dwóch drugich szlachty zranił, do trzeciego strzela:
Uciekają. Było to przy kłodzie Chrzciciela.
Ten już miał ręce wolne, gotowe ku walce;
Wstał, podniósł dłoń i zwinął w kłębek długie palce,
I z góry tak uderzył w grzbiet Rosyjanina,
Że twarz jego i skroń wbił w zamek karabina;
Trzasł zamek: lecz zalany krwią proch już nie spalił;
Sierżant u nóg Chrzciciela na swą broń się zwalił.
Chrzciciel schyla się, chwyta karabin za rurę
I wijąc jak kropidłem podnosi go w górę,
Robi młynka, dwóch zaraz szeregowych zwala
Po ramionach i w głowę ugadza kaprala.
Reszta zlękła od kłody cofa się z przestrachem:
Tak Kropiciel ruchomym nakrył szlachtę dachem.

    Za czym rozbito kłodę, rozcięto powrozy.
Szlachta, już wolna, wpada na kwestarskie wozy;
Z nich dobywa rapiery, pałasze, tasaki,
Kosy, strzelby; Konewka znalazł dwa szturmaki
I worek kul; wsypał je do swego szturmaka,
Drugi, równie nabiwszy, ustąpił dla Saka.

    Jegrów więcej przybywa. Mieszają się, tłuką;
Szlachta w zgiełku nie może ciąć krzyżową sztuką,
Jegry nie mogą strzelać; już walczą wręcz z bliska,
Już stal ząb za ząb o stal porwawszy się pryska,
Bagnet o szablę, kosa o gifes się łamie,
Pięść spotyka się z pięścią i z ramieniem ramię.

    Lecz Ryków z częścią jegrów pobiegł, gdzie stodoła
Tyka płotów; tam staje, na żołnierzy woła,
Ażeby zaprzestali bitwę tak bezładną,
Gdzie, nie używszy broni, pod pięściami padną.
Gniewny, że sam nie może dać ognia, bo w tłumie
Moskalów od Polaków rozróżnić nie umie,
Woła: «Stroj się!» (co znaczy: formuj się do szyku)
Ale komendy jego nie słychać śród krzyku.

    Stary Maciek, do ręcznych zapasów niezdolny,
Rejterował się, czyniąc przed sobą plac wolny
Na prawo i na lewo. Tu, końcem szablicy
Uciera bagnet z rury jako knot ze świécy;
Tam, machnąwszy na odlew, ścina albo kole:
I tak ostróżny Maciek ustępuje w pole.

    Lecz z największym na niego naciera uporem
Stary Gifrejter, co był pułku instruktorem,
Wielki mistrz na bagnety. Zebrał się sam w sobie,
Skurczył się, a karabin porwał w ręce obie,
Prawą u zamka, lewą w pół rury porywa,
Kręci się, podskakuje, czasem przysiadywa,
Lewą rękę opuszcza, a broń z prawej ręki
Suwa naprzód jak żądło z wężowej paszczęki
I znowu ją w tył cofa, na kolanie wspiera:
I tak kręcąc się, skacząc, na Maćka naciera.

    Ocenił przeciwnika zręczność Maciek stary
I lewą ręką włożył na nos okulary,
Prawą, rękojeść Rózgi tuż przy piersiach trzyma,
Cofa się, Gifrejtera ruch śledząc oczyma;
Sam słania się na nogach, jakoby był pijany.
Gifrejter bieży prędzej i pewny wygranej;
Żeby uchodzącego tym łacniej dosiągnął,
Powstał i całą prawą rękę wzdłuż wyciągnął,
Popychając karabin, a tak się wysilił
Pchnięciem i wagą broni, że się aż pochylił:
Maciek, tam kędy bagnet wkłada się na rurę,
Podstawia swą rękojeść, podbija broń w górę
I wnet spuszczając Rózgę, tnie Moskala w rękę
Raz, i znowu na odlew przecina mu szczękę.
Tak padł Gifrejter, fechmistrz najpierwszy z Moskalów,
Kawaler trzech krzyżyków i czterech medalów.

    Tymczasem koło kłodek lewe szlachty skrzydło
Już jest bliskie zwycięstwa. Tam walczył Kropidło
Widny z dala, tam Brzytwa wił się śród Moskali:
Ten ich w pół ciała rzeza, tamten w głowy wali.
Jako machina, którą niemieccy majstrowie
Wymyślili i która młockarnią się zowie,
A jest razem sieczkarnią, ma cepy i noże,
Razem i słomę kraje, i wybija zboże:
Tak pracują Kropiciel i Brzytwa pospołu,
Mordując nieprzyjaciół, ten z góry, ten z dołu.

    Lecz Kropiciel już pewne porzuca zwycięstwo;
Bieży na prawe skrzydło, gdzie niebezpieczeństwo
Nowe grozi Maćkowi. Śmierci Gifrejtera
Mszcząc się, Proporszczyk z długim szpontonem naciera
(Szponton, jest to zarazem dzida i siekiera;
Teraz już zaniedbany i tylko na flocie
Używają go; wówczas służył i piechocie).
Proporszczyk, człowiek młody, zręcznie się uwijał;
Ilekroć mu przeciwnik broń na bok odbijał,
On cofał się: młodego nie mógł Maciek zgonić,
I tak nie raniąc, musiał tylko siebie bronić.
Już mu Proporszczyk dzidą lekką ranę zadał,
Już wznosząc w górę berdysz do cięcia się składał,
Chrzciciel nie zdoła dobiec, lecz staje wpół drogi,
Okręca broń i ciska wrogowi pod nogi.
Skruszył kość; już Proporszczyk szponton z rąk upuszcza,
Słania się: wpada Chrzciciel, za nim szlachty tłuszcza,
A za szlachtą Moskale od lewego skrzydła
Biegą zmieszani. Wszczął się bój koło Kropidła.

    Chrzciciel, który w obronie Maćka oręż stracił,
Ledwie że tej przysługi życiem nie przypłacił:
Bo przypadło nań z tyłu dwóch silnych Moskali,
I czworo rąk zarazem we włos mu wplątali;
Upiąwszy się nogami ciągną jako liny
Sprężyste, uwiązane do masztu wiciny.
Daremnie w tył Kropiciel ciska ślepe razy;
Chwieje się: a wtem postrzegł, że blisko Gerwazy
Walczy; zawołał: «Jezus Maryja! Scyzoryku!»

    Klucznik, trwogę Chrzciciela poznawszy po krzyku,
Odwrócił się, i spuścił ostrze płytkiej stali
Między głowę Chrzciciela i ręce Moskali.
Cofnęli się, wydawszy przeraźliwe głosy;
Lecz jedna ręka, mocniej wplątana we włosy,
Została się wisząca i krwią buchająca.
Tak orlik, jedną szponę gdy wbije w zająca,
Drugą, by wstrzymać zwierza, o drzewo uczepi,
A zając, targnąwszy się, orła wpół rozsczepi;
Prawa szpona u drzewa zostaje się w lesie,
A lewą zakrwawioną źwierz na pola niesie.

    Kropiciel wolny, oczy obraca dokoła,
Ręce wyciąga, broni szuka, broni woła;
Tymczasem grzmi pięściami, stojąc; mocno w kroku,
I pilnując się z bliska Gerwazego boku,
Aż Saka, syna swego, postrzega w natłoku.
Sak prawą ręką szturmak wymierza, a lewą
Ciągnie za sobą długie sążniowate drzewo,
Uzbrojone w krzemienie i guzy, i sęki
(Nikt by go nie podźwignął prócz Chrzciciela ręki).
Chrzciciel, gdy miłą broń swą, swe Kropidło zoczył,
Chwycił je, ucałował, z radości podskoczył,
Zakręcił je nad głową i zaraz ubroczył.

    Co potem dokazywał, jakie klęski szerzył,
Daremnie śpiewać: nikt by muzie nie uwierzył;
Jak nie wierzono w Wilnie ubogiej kobiécie,
Która stojąc na świętej Ostrej Bramy szczycie,
Widziała, jako Dejów, moskiewski jenerał,
Wchodząc z pułkiem kozaków, już bramę otwierał,
I jak jeden mieszczanin, zwany Czarnobacki,
Zabił Dejowa i zniósł cały pułk kozacki.

    Dosyć, że się tak stało, jak przewidział Ryków:
Jegry w tłumie ulegli mocy przeciwników.
Dwudziestu trzech na ziemi wala się zabitych,
Trzydziestu kilku jęczy ranami okrytych,
Wielu pierzchło, skryło się w sad, w chmiele, nad rzekę,
Kilku wpadło do domu pod kobiet opiekę.

    Zwycięska szlachta biega z okrzykiem wesela:
Ci do beczek, ci łupy rwą z nieprzyjaciela;
Jeden Robak tryumfów szlachty nie podziela.
On dotąd sam nie walczył (bo bronią kanony
Księdzu bić się), lecz jako człowiek doświadczony
Dawał rady, plac boju z różnych stron obchodził,
Wzrokiem, ręką, walczących zachęcał, przywodził.
I teraz woła, aby do niego się łączyć,
Uderzyć na Rykowa, zwycięstwo dokończyć.
Tymczasem przez posłańca wskazał do Rykowa,
Że jeżeli broń złoży, życie swe zachowa;
Jeżeli zaś oddanie broni będzie zwlekać,
Robak każe otoczyć resztę i wysiekać.

    Kapitan Ryków wcale nie prosił pardonu;
Zebrawszy koło siebie pół batalijonu,
Krzyknął: «Za broń!» — wnet szereg karabiny chwyta;
Chrząsnęła broń, a była już dawno nabita;
Krzyknął: «Cel!» — rury rzędem zabłysnęły długim;
Krzyknął: «Ognia koleją!» — grzmią jeden po drugim.
Ten strzela, ten nabija, ten chwyta do ręki,
Słychać świsty kul, zamków chrzęsty, sztenflów dźwięki:
Cały szereg zdaje się być ruchomym płazem,
Który tysiąc błyszczących nóg wywija razem.

    Prawda, że jegry byli mocnym trunkiem pjani,
Źle mierzą i chybiają, rzadko który rani,
Ledwie który zabije: przecież dwóch Maciejów
Już zraniono i poległ jeden z Bartłomiejów.
Szlachta z niewiela rusznic z rzadka się odstrzela;
Chce szablami uderzyć na nieprzyjaciela,
Ale starsi wstrzymują; kule gęsto świszczą,
Rażą, spędzają, wkrótce dziedziniec oczyszczą,
Już aż po szybach dworu zaczynają dzwonić.

    Tadeusz, który został w domu, kobiet, bronić
Z rozkazu stryja, słysząc że coraz to gorzéj
Wre bitwa, wybiegł, za nim wybiegł Podkomorzy,
Któremu Tomasz wreszcie przyniósł karabelę;
Śpieszy, łączy się z szlachtą i staje na czele.
Bieży, broń wzniósłszy, szlachta rusza jego śladem:
Jegry przypuściwszy ich, sypnęli kul gradem:
Legł Isajewicz, Wilbik, Brzytewka raniony;
Za czym wstrzymują szlachtę Robak z jednej strony
A z drugiej Maciej. Szlachta ostyga w zapale,
Ogląda się, cofa się; widzą to Moskale:
Kapitan Ryków myśli ostatni cios zadać,
Spędzić szlachtę z dziedzińca i dworem owładać.

    «Formuj się do ataku! — zawołał — na sztyki!
Naprzód!» Wnet szereg rury wytknąwszy jak tyki,
Schyla głowy, zrusza się i przyśpiesza kroku.
Darmo szlachta wstrzymuje z przodu, strzela z boku:
Szereg już pół dziedzińca przeszedł bez oporu;
Kapitan pokazując szpadą na drzwi dworu,
Krzyczy: «Sędzio! poddaj się, bo dwór spalić każę!»
«Pal — woła Sędzia — ja cię w tym ogniu usmażę».

    O dworze Soplicowski! Jeśli dotąd całe
Świecą się pod lipami twoje ściany białe,
Jeśli tam dotąd szlachty sąsiedzkiej gromada
Za gościnnymi stoły Sędziego zasiada:
Pewnie tam piją często za Konewki zdrowie;
Bez niego już by było dziś po Soplicowie!

    Konewka dotąd małe dał męstwa dowody.
Choć najpierwszy ze szlachty uwolniony z kłody,
Choć zaraz znalazł w wozie swą miłą konewkę,
Swój szturmak faworytny i z nim kul sakiewkę:
Nie chciał bić się; powiadał, że sobie nie ufa
Na czczo. Szedł więc, gdzie stała spirytusu kufa:
Ręką jak łyżką strumień do ust sobie chylił.
Dopiero, gdy się dobrze rozgrzał i posilił,
Poprawił czapkę, z kolan wziął do rąk konewkę,
Zmacał sztenflem naboju, podsypał panewkę,
I spojrzał na plac boju. Widzi, że błyszcząca
Fala bagnetów szlachtę bije i roztrąca:
Przeciw tej fali płynie; schyla się do ziemi
I nurkuje pomiędzy trawami gęstemi,
Środkiem dziedzińca; aż tam, gdzie rosła pokrzywa,
Zasadza się, a Saka gestami przyzywa.

    Sak, broniąc dworu, stanął z szturmakiem u proga:
Bo w tym dworze mieszkała jego Zosia droga,
Od której choć w zalotach został pogardzony,
Kochał ją zawsze, zginąć rad dla jej obrony.

    Już szereg jegrów w marszu na pokrzywę wkracza:
Gdy Konew ruszył cyngla i z paszczy garłacza
Tuzin kul rozsiekanych puszcza śród Moskali,
Sak puszcza drugi tuzin. Jegry się zmieszali.
Przerażony zasadzką szereg w kłąb się zwija,
Cofa się, rzuca rannych; Chrzciciel ich dobija.

    Stodoła już daleko; bojąc się odwodu
Długiego, Ryków skoczył pod parkan ogrodu;
Tam, pierzchającą rotę zatrzymuje w biegu.
Szykuje, lecz szyk zmienia: z jednego szeregu
Robi trójkąt, klin ostry wystawując z przodu,
A dwa boki opiera o parkan ogrodu.
Dobrze zrobił, bo jazda nań od zamku wali.

    Hrabia, który był w zamku pod strażą Moskali,
Gdy pierzchła straż zlękniona, dworzan na koń wsadził,
I słysząc strzały, w ogień jazdę swą prowadził,
Sam na czele z żelazem nad głowę wzniesionem.
Wtem Ryków krzyknął: «Ognia pół batalijonem!»
Przeleciała po zamkach wzdłuż nitka ognista,
I z czarnych rur wytkniętych świsnęło kul trzysta.
Trzech jezdnych padło rannych, jeden trupem leży.
Padł koń Hrabi, spadł Hrabia; Klucznik krzycząc bieży
Na ratunek, bo widzi: jegry na cel wzięli
Ostatniego z Horeszków, chociaż po kądzieli.
Robak był bliższy; Hrabię ciałem swym zakrywa,
Dostał za niego postrzał, spod konia dobywa,
Uprowadza; a szlachcie każe się rozstąpić,
Lepiej mierzyć, postrzałów nadaremnych skąpić,
Kryć się za płoty, studnie, za ściany obory;
Hrabia z jazdą ma czekać sposobniejszej pory.

    Plany Robaka pojął i wykonał cudnie
Tadeusz. Stał ukryty za drewnianą studnię;
A że trzeźwy i dobrze strzelał z dubeltówki
(Mógł trafić do rzuconej w powietrze złotówki),
Okropnie razi Moskwę. Starszyznę wybiera;
Za pierwszym zaraz strzałem ubił feldfebera,
Potem z dwóch rur raz po raz dwóch sierżantów sprząta,
Mierzy to po galonach, to w środek trójkąta,
Gdzie stał sztab; za czym Ryków gniewa się i dąsa,
Tupa nogami, szpady swej rękojeść kąsa:
«Majorze Płucie — woła — co to z tego będzie?
Wkrótce tu nie zostanie nikt z nas przy komendzie!»

    Więc Płut na Tadeusza krzyknął z wielkim gniewem:
«Panie Polak, wstydź się pan, chować się za drzewem;
Nie bądź tchórz, wyjdź na środek, bij się honorowie,
Po żołniersku». A na to Tadeusz odpowie:
«Majorze! jeśli jesteś tak śmiałym rycerzem,
A czegoż ty się chowasz za jegrów kołnierzem?
Nie tchórzę ja przed tobą: wynidź no zza płotów;
Dostałeś w twarz, jam przecie bić się z tobą gotów!
Po co krwi rozlew? Między nami była zwada:
Niechajże ją rozstrzygnie pistolet lub szpada.
Daję ci broń na wybór, od działa do szpilki;
A nie, to was wystrzelam jako w jamie wilki».
I to mówiąc wystrzelił, a tak dobrze mierzył,
Że porucznika obok Rykowa uderzył.

    «Majorze — szepnął Ryków — wyjdź na pojedynek,
I pomścij się za jego raniejszy uczynek.
Jeśli tego szlachcica kto inny zabije,
To Major widzi, Major hańby swej nie zmyje.
Trzeba tego szlachcica na pole wywabić;
Nie można z karabina, to choć szpadą zabić.
»Co puka, to nie sztuka, to wolę co kole«:
Mówił stary Suworów; wyjdź Majorze w pole,
Bo on nas powystrzela; patrz, bierze do celu».
Na to rzekł Major: «Ryków! miły przyjacielu!
Ty jesteś zuch na szpady: wyjdź ty bracie Ryków.
Lub wiesz co, wyszlem kogo z naszych poruczników.
Ja, major, ja nie mogę odstąpić żołnierzy,
Do mnie batalijonu komenda należy».
Słysząc to Ryków, szpadę podniósł, wyszedł śmiało,
Kazał ognia zaprzestać, machnął chustką białą.
Pyta się Tadeusza, jaką broń podoba;
Po układach, na szpady zgodzili się oba.
Tadeusz broni nie miał: gdy szukano szpady,
Wyskoczył Hrabia zbrojny i zerwał układy.

    «Panie Soplico! — wołał — z przeproszeniem pana,
Pan wyzwałeś Majora! Ja do Kapitana
Mam dawniejszą urazę: on do zamku mego…»
(«Mów pan — przerwał Protazy — do zamku naszego»)
«On wpadł — rzekł kończąc Hrabia — na czele złodziejów,
On, poznałem Rykowa, wiązał mych dżokejów.
Skarzę, go, jakom zbójców skarał pod opoką,
Którą Sycylijanie zwą Birbante-rokko».

    Uciszyli się wszyscy, ustało strzelanie;
Wojska ciekawe patrzą na wodzów spotkanie.
Hrabia i Ryków idą, obróceni bokiem,
Prawą ręką i prawym grożąc sobie okiem;
Wtem lewymi rękami odkrywają głowy
I kłaniają się grzecznie (zwyczaj honorowy,
Nim przyjdzie do zabójstwa, naprzód się przywitać).
Już spotkały się szpady i zaczęły zgrzytać;
Rycerze wznosząc nogi, prawymi kolany
Przyklękają, w przód i w tył skacząc na przemiany.

    Ale Płut, Tadeusza widząc przed swym frontem,
Naradzał się po cichu z gifrejterem Gontem,
Który w rocie uchodził za pierwszego strzelca.
«Gonto — rzekł Major — widzisz ty tego wisielca?
Jeśli mu wsadzisz kulę, tam pod piątym żebrem,
To dostaniesz ode mnie cztery ruble srebrem».
Gont odwodzi karabin, do zamka się chyli,
Wierni go towarzysze płaszczami okryli;
Mierzy, nie w żebro, ale w głowę Tadeusza:
Strzelił i trafił… blisko, w środek kapelusza.
Okręcił się Tadeusz: aż Kropiciel wpada
Na Rykowa, a za nim szlachta krzycząc: «Zdrada!»
Tadeusz go zasłania. Ledwie zdołał Ryków
Zrejterować się i wpaść we środek swych szyków.

    Znowu Dobrzyńscy z Litwą natarli w zawody,
I pomimo dawniejsze dwóch stronnictw niezgody
Walczą jak bracia, jeden drugiego zachęca.
Dobrzyńscy, widząc, jak się Podhajski wykręca
Tuż przed szeregiem jegrów i kosą ich kraje,
Zawołali z radością: «Niech żyją Podhaje!
Naprzód bracia Litwini, górą, górą Litwa!»
Skołubowie zaś, widząc, jak waleczny Brzytwa,
Choć ranny, leci z szablą wzniesioną do góry,
Krzyknęli: «Górą Maćki, niech żyją Mazury!»
Dodawszy wzajem serca biegną na Moskali:
Nadaremnie ich Robak z Maćkiem wstrzymywali.

    Gdy tak na rotę jegrów uderzano z przodu,
Wojski rzuca plac boju, idzie do ogrodu;
Przy boku jego stąpał ostrożny Protazy,
A Wojski mu po cichu wydawał rozkazy.

    Stała w ogrodzie, prawie pod samym parkanem,
O który się opierał Ryków swym trójgranem,
Wielka stara sernica, budowana w kratki
Z belek na krzyż wiązanych, podobna do klatki.
W niej świeciły się białych serów mnogie kopy;
Wkoło zaś wahały się suszące się snopy
Szałwi, benedykty, kardy, macierzanki:
Cała zielna domowa apteka Wojszczanki.
Sernica w górze miała wszerz sążni półczwarta,
A u dołu na jednym wielkim słupie wsparta
Niby gniazdo bocianie. Stary słup dębowy
Pochylił się, bo już był wygnił do połowy,
Groził upadkiem. Nieraz Sędziemu radzono,
Aby zrzucił budowę wiekiem nadwątloną;
Ale Sędzia powiadał, że woli poprawiać
Aniżeli rozrzucać, albo też przestawiać:
Odkładał budowanie do sposobnej pory,
Tymczasem pod słup kazał wetknąć dwie podpory.
Tak pokrzepiona ale nietrwała budowa
Wyglądała za parkan nad trójkąt Rykowa.

    Ku tej sernicy Wojski z Woźnym milczkiem idą,
Każdy zbrojny ogromnym drągiem jakby dzidą;
Za nimi ochmistrzyni dąży przez konopie
I kuchcik, małe, ale bardzo silne chłopię.
Przyszedłszy, drągi wparli w wierzch słupa nadgniły,
Sami u końców wisząc pchają z całej siły:
Jako flisy uwięzłą na rapach wicinę
Długimi drągi z brzegu pędzą na głębinę.

    Trzasnął słup: już sernica chwieje się i wali
Z brzemieniem drzew i serów na trójkąt Moskali.
Gniecie, rani, zabija; gdzie stały szeregi,
Leżą drwa, trupy, sery białe jako śniegi,
Krwią i mózgiem splamione. Trójkąt w sztuki pryska,
A już w środku Kropidło grzmi, już Brzytwa błyska,
Siecze Rózga, od dworu wpada szlachty tłuszcza,
A Hrabia od bram jazdę na rozpierzchłych puszcza.

    Już tylko ośmiu jegrów z sierżantem na czele
Bronią się; bieży Klucznik, oni stoją śmiele,
Dziewięć rur wymierzyli prosto w łeb Klucznika;
On leci na strzał, kręcąc ostrze Scyzoryka.
Widzi to ksiądz: zabiega Klucznikowi drogę,
Sam pada i podbija Gerwazemu nogę:
Upadli, właśnie kiedy pluton ognia dawał.
Ledwie ołów prześwisnął, już Gerwazy wstawał,
Już wskoczył w dym, dwóm jegrom zaraz głowy zmiata
Uciekają strwożeni; Klucznik goni, płata;
Oni biegną dziedzińcem, Gerwazy ich torem;
Wpadają we drzwi gumna stojące otworem,
I Gerwazy do gumna na ich karkach wjechał,
Zniknął w ciemności, ale bitwy nie zaniechał:
Bo przeze drzwi jęk słychać, wrzask i gęste razy.
Wkrótce ucichło wszystko. Wyszedł sam Gerwazy
Z mieczem krwawym.

                        Już szlachta odzierżyła pole,
Porozpędzanych jegrów ściga, rąbie, kole.
Ryków sam został; krzyczy, że broni nie złoży,
Bije się; gdy ku niemu podszedł Podkomorzy,
I wznosząc karabelę, rzekł poważnym tonem:
«Kapitanie! nie splamisz czci twojej pardonem.
Dałeś próby, rycerzu nieszczęsny, lecz mężny,
Twojej odwagi: porzuć opór niedołężny,
Złóż broń, nim cię naszymi szablami rozbroim;
Zachowasz życie i cześć, jesteś więźniem moim!»

    Ryków, Podkomorzego zwalczony powagą,
Skłonił się i oddał mu swoję szpadę nagą,
Skrwawioną po rękojeść, i rzekł: «Lachy braty!
Oj biada mnie, żem nie miał choć jednej armaty!
Dobrze mówił Suworów: »pomnij Ryków kamrat,
Żebyś nigdy na Lachów nie chodził bez armat!«
Cóż! jegry byli pjani, Major pić pozwolił!
Och major Płut, on dzisiaj bardzo poswywolił!
On odpowie przed carem, bo on miał komendę.
Ja, panie Podkomorzy, wasz przyjaciel będę.
Ruskie przysłowie mówi: kto się mocno lubi,
Ten, panie Podkomorzy, i mocno się czubi.
Wy dobrzy do wypitki, dobrzy do wybitki,
Ale przestańcie robić nad jegrami zbytki».

    Podkomorzy, słysząc to, karabelę wznasza
I przez Woźnego pardon powszechny ogłasza;
Każe rannych opatrzyć, z trupów czyścić pole,
A jegrów rozbrojonych prowadzić w niewolę.
Długo szukano Płuta. On, w krzaku pokrzywy
Zarywszy się głęboko, leżał jak nieżywy;
Wyszedł wreszcie ujrzawszy, że było po bitwie.
Taki miał koniec zajazd ostatni na Litwie.




Księga dziesiąta



Emigracja. Jacek.

Narada tycząca się zabezpieczenia losu zwycięzców — Układy z Rykowem — Pożegnanie — Ważne odkrycie — Nadzieja.

    Owe obłoki ranne, zrazu rozpierzchnione
Jak czarne ptaki, lecąc w wyższą nieba stronę,
Coraz się zgromadzały. Ledwie słońce zbiegło
Z południa, już ich stado pół niebios obiegło
Ogromną chmurą. Wiatr ją pędził coraz chyżej,
Chmura coraz gęstniała, zwieszała się niżej:
Aż, jedną stroną na wpół od niebios oddarta,
Ku ziemi wychylona i wszerz rozpostarta,
Jak wielki żagiel, biorąc wszystkie wiatry w siebie,
Od południa na zachód leciała po niebie.

    I była chwila ciszy; i powietrze stało
Głuche, milczące, jakby z trwogi oniemiało.
I łany zbóż, co wprzódy kładąc się na ziemi
I znowu w górę trzęsąc kłosami złotemi
Wrzały jak fale, teraz stoją nieruchome
I poglądają w niebo najeżywszy słomę.
I zielone przy drogach wierzby i topole,
Co pierwej, jako płaczki przy grobowym dole,
Biły czołem, długimi kręciły ramiony,
Rozpuszczając na wiatry warkocz posrebrzony,
Teraz jak martwe, z niemej wyrazem żałoby,
Stoją na kształt posągów sypilskiej Nijoby.
Jedna osina drżąca, wstrząsa liście siwe.

    Bydło, zwykle do domu powracać leniwe,
Teraz zbiega się tłumnie, pasterzy nie czeka
I opuszczając strawę do domu ucieka.
Buhaj racicą ziemię kopie, orze rogiem,
I całą trzodę straszy ryczeniem złowrogiem;
Krowa coraz ku niebu wznosi wielkie oko,
Usta z dziwu otwiera i wzdycha głęboko;
A wieprz marudzi w tyle, dąsa się i zgrzyta,
I snopy zboża kradnie i na zapas chwyta.

    Ptastwo skryło się w lasy, pod strzechy, w głąb trawy;
Tylko wrony, stadami obstąpiwszy stawy,
Przechadzają się sobie poważnymi kroki,
Czarne oczy kierują na czarne obłoki,
Wytknąwszy język z suchej szerokiej gardzieli
I skrzydła roztaczając, czekają kąpieli;
Lecz i te, przewidując nazbyt mocną burzę,
Już w las ciągną, podobne wznoszącej się chmurze.
Ostatnia z ptaków, lotem nieścigłym zuchwała
Jaskółka, czarny obłok przeszywa jak strzała,
Wreszcie spada jak kula.

                        Właśnie w owej chwili
Szlachta z Moskwą okropną walkę zakończyli
I chronią się gromadnie w domy i stodoły,
Opuszczają plac boju, gdzie wkrótce żywioły
Stoczą walkę.

                        Na zachód, jeszcze ozłocona
Świeci ziemia ponuro, żółtawo-czerwona:
Już chmura, roztaczając cienie na kształt sieci,
Wyławia resztki światła, a za słońcem leci,
Jak gdyby je pochwycić chciała przed zachodem.
Kilka wichrów raz po raz prześwisnęło spodem,
Jeden za drugim lecą, miecąc krople dżdżyste,
Wielkie, jasne, okrągłe, jak grady ziarniste.

    Nagle wichry zwarły się, porwały się w poły,
Borykają się, kręcą, świszczącymi koły
Krążą po stawach, mącą do dna wody w stawach,
Wpadły na łąki, świszczą po łozach i trawach.
Pryskają łóz gałęzie; lecą traw przekosy
Na wiatr jako garściami wyrywane włosy,
Zmieszane z kędziorami snopów. Wiatry wyją,
Upadają na rolę, tarzają się, ryją,
Rwą skiby, robią otwór wichrowi trzeciemu,
Który wydarł się z roli jak słup czarnoziemu,
Wznosi się, jak ruchoma piramida toczy,
Łbem grunt wierci, z nóg piasek sypie gwiazdom w oczy,
Co krok wszerz wydyma się, roztwiera ku górze,
I ogromną swą trąbą otrębuje burzę.
Aż z całym tym chaosem wody i kurzawy,
Słomy, liścia, gałęzi, wydartej murawy,
Wichry w las uderzyły i po głębiach puszczy
Ryknęły jak niedźwiedzie.

                        A już deszcz wciąż pluszczy
Jak z sita, w gęstych kroplach. Wtem rykły pioruny,
Krople zlały się razem: to jak proste struny
Długim warkoczem wiążą niebiosa do ziemi,
To jak z wiader buchają warstami całemi.
Już zakryły się całkiem niebiosa i ziemia;
Noc je z burzą od nocy czarniejszą, zaciemia.
Czasem widnokrąg pęka od końca do końca,
I anioł burzy, na kształt niezmiernego słońca
Rozświeci twarz, i znowu okryty całunem
Uciekł w niebo i drzwi chmur zatrzasnął piorunem.
Znowu wzmaga się burza, ulewa nawalna
I ciemność gruba, gęsta, prawie dotykalna.
Znowu deszcz ciszej szumi, grom na chwilę uśnie;
Znowu wzbudzi się, ryknie i znów wodą chluśnie.
Aż się uspokoiło wszystko; tylko drzewa
Szumią około domu i szemrze ulewa.

    W takim dniu pożądany był czas najburzliwszy:
Bo nawałnica, boju plac mrokiem okrywszy,
Zalała drogi, mosty zerwała na rzece,
Z folwarku niedostępną zrobiła fortecę.
O tym więc, co się działo w obozie Soplicy,
Dziś nie mogła rozejść się wieść po okolicy,
A właśnie zawisł szlachty los od tajemnicy.

    W izbie Sędziego ważne toczą się narady.
Bernardyn leżał w łóżku; zmordowany, blady
I skrwawiony, lecz całkiem zdrowy na umyśle,
Daje rozkazy, Sędzia wypełnia je ściśle.
Prosi Podkomorzego, przyzywa Klucznika,
Każe przywieść Rykowa, potem drzwi zamyka.
Godzinę całą trwały tajemne rozmowy,
Aż je przerwał kapitan Ryków tymi słowy,
Rzucając na stół kiesę ciężką dukatami:
«Państwo Lachy, już jest ta gadka między wami,
Że każdy Moskal złodziej: powiedźcież, kto spyta,
Że znaliście Moskala, który zwan Nikita
Nikitycz Ryków, rotny kapitan, miał osim
Medalów i trzy krzyże — to pamiętać prosim:
Ten medal za Oczaków, ten za Izmaiłów,
Ten za bitwę pod Nowi, ten za Prejsiż-Iłów ,
Tamten za Korsakowa sławną rejteradę
Z pod Zurich; a miał także i za męstwo szpadę,
Także od feldmarszałka trzy zadowolnienia,
Dwie pochwały cesarskie i cztery wspomnienia,
Wszystko na piśmie…»

                        «Ale, ale kapitanie —
Przerwał Robak — i cóż się tedy z nami stanie,
Jeśli nie chcesz zgodzić się? Wszakże dałeś słowo
Załatwić tę rzecz».

                        «Prawda, słowo dam na nowo —
Rzecze Ryków — ot słowo! Co po waszej zgubie?
Ja człek poczciwy, ja was państwo Lachy lubię,
Że wy ludzie weseli, dobrzy do wypitki,
I także ludzie śmiali, dobrzy do wybitki.
U nas ruskie przysłowie: Kto na wozie jedzie,
Bywa często pod wozem; kto dzisiaj na przedzie,
Jutro w tyle; dziś bijesz jutro ciebie biją;
Czy o to gniew? tak u nas po żołniersku żyją.
Skąd by się człowiekowi tyle złości wzięło
Gniewać się o przegranę! Oczakowskie dzieło
Było krwawe, pod Zurich zbili nam piechotę,
Pod Austerlicem całą utraciłem rotę,
A pierwej wasz Kościuszko pod Racławicami —
Byłem sierżantem — wysiekł mój pluton kosami:
I cóż stąd? To ja znowu u Maciejowiców
Zabiłem własnym sztykiem dwóch dzielnych szlachciców:
Jeden był Mokronowski, szedł z kosą przed frontem,
I kanonierowi uciął rękę z lontem.
Oj! wy Lachy! Ojczyzna! ja to wszystko czuję,
Ja Ryków, car tak każe, a ja was żałuję.
Co nam do Lachów? Niechaj Moskwa dla Moskala,
Polska dla Lacha; ale cóż? car nie pozwala!»

    Sędzia mu na to rzecze: «Panie Kapitanie,
Żeś człek poczciwy, wiedzą tu wszyscy ziemianie,
U których na kwaterach stałeś od lat wielu.
Za ten dar nie gniewaj się, dobry przyjacielu:
Nie chcieliśmy cię skrzywdzić; te oto dukaty,
Śmieliśmy złożyć wiedząc, żeś człek niebogaty».

    «Ach, jegry! — wołał Ryków — cała rota skłuta!
Moja rota! a wszystko z winy tego Płuta!
On komendant, on za to przed carem odpowie,
A wy te grosze sobie zabierzcie, panowie;
U mnie jest kapitański mój żołd lada jaki,
A dosyć mnie na ponczyk i lulkę tabaki.
A was lubię, że z wami sobie zjem, popiję,
Pohulam, pogawędzę, i tak sobie żyję.
Otoż ja was obronię, i jak będzie śledztwo,
Słowo uczciwe, że dam za wami świadectwo.
Powiemy, że my przyszli tu z wizytą, pili
Sobie, tańczyli, trochę sobie podchmielili,
A Płut przypadkiem ognia zakomenderował,
Bitwa! i batalijon tak jakoś zmarnował.
Wy, pany, tylko śledztwo pomazujcie złotem,
Będzie kręcić się. Ale teraz powiem o tem,
Co już mówiłem temu szlachcicu, co długi
Ma rapier, że Płut pierwszy komendant, ja drugi:
Płut został żywy, może on wam zagiąć kruczka
Takiego, że zginiecie, bo to chytra sztuczka;
Trzeba mu gębę zatkać bankowym papierem.
No i cóż, panie szlachcic, ty z długim rapierem,
Czy już byłeś u Płuta? czyś się z nim naradził?»

    Gerwazy obejrzał się, łysinę pogładził,
Kiwnął niedbale ręką, jak gdyby znać dawał,
Że już wszystko załatwił. Lecz Ryków nastawał:
«Cóż, czy Płut będzie milczeć, czy słowem zaręczył?»
Klucznik zły, że go Ryków pytaniami dręczył,
Poważnie palec wielki ku ziemi naginał,
A potem machnął ręką, jak gdyby przecinał
Dalszą rozmowę i rzekł: «Klnę się Scyzorykiem,
Że Płut nie wyda! gadać już nie będzie z nikim!»
Potem dłonie opuścił i palcami chrząsnął,
Jak gdyby tajemnicę całą z rąk wytrząsnął.

    Ten ciemny gest pojęli słuchacze i stali,
Patrząc z dziwem na siebie, wzajem się badali
I posępne milczenie trwało minut kilka.
Aż Ryków rzekł: «Nosił wilk, ponieśli i wilka!»
«Requiescat in pace!» dodał Podkomorzy;
«Już ci — zakończył Sędzia — był w tym palec Boży!
Lecz ja tej krwi nie winien, jam o tym nie wiedział».

    Ksiądz porwał się z poduszek i posępny siedział.
Na koniec rzekł, spojrzawszy bystro na Klucznika:
«Wielki grzech bezbronnego zabić niewolnika!
Chrystus zabrania mścić się nawet i nad wrogiem!
Oj Kluczniku! odpowiesz ty ciężko przed Bogiem.
Jedna jest restrykcyja: jeśli popełniono
Nie z zemsty głupiej, ale pro publico bono».
Klucznik głową i ręką kiwał wyciągnioną,
I mrugając powtarzał: «Pro publico bono!»

    Więcej nie było mowy o Płucie Majorze;
Nazajutrz daremnie go szukano we dworze,
Daremnie wyznaczano za trupa nagrodę:
Major zginął bez śladu, jak gdyby wpadł w wodę.
Co się z nim stało, różnie powiadano o tem,
Lecz nikt pewnie nie wiedział ni wtenczas, ni potem.
Daremnie pytaniami Klucznika dręczono;
Nic nie wyrzekł, prócz tych słów: pro publico bono.
Wojski był w tajemnicy, lecz słowem ujęty
Honorowym, staruszek milczał jak zaklęty.

    Po zawarciu układów wyszedł z izby Ryków,
A Robak kazał wezwać szlachtę wojowników,
Do których Podkomorzy z powagą tak mówi:
«Bracia! Bóg dziś naszemu szczęścił orężowi,
Ale muszę Wać Państwu wyznać bez ogródki,
Że z tych niewczesnych bojów złe wynikną skutki.
Zbłądziliśmy i nikt tu z nas nie jest bez winy:
Ksiądz Robak, że zbyt czynnie rozszerzał nowiny,
Klucznik i szlachta, że je pojęła opacznie.
Wojna z Rosyją jeszcze nieprędko się zacznie;
Tymczasem, kto miał udział najczynniejszy w bitwie,
Ten nie może bezpieczny zostać się na Litwie:
Musicie więc do Księstwa uciekać Panowie,
A mianowicie Maciej, co się Chrzciciel zowie,
Tadeusz, Konew, Brzytew, niech unoszą głowy
Za Niemen, gdzie ich czeka zastęp narodowy.
My na was nieobecnych całą winę zwalim
I na Płuta: tak resztę rodzeństwa ocalim.
Żegnam was nie na długo; są pewne nadzieje,
Że nam z wiosną swobody zorza zajaśnieje
I Litwa, co was teraz żegna jak tułaczy,
Wkrótce jako zwycięskich swych zbawców zobaczy.
Sędzia wszystko, co trzeba, zgotuje na drogę
I ja pieniędzmi, ile zdołam, dopomogę».

    Czuła szlachta, że mądrze Podkomorzy radził:
Wiadomo, że kto z ruskim carem raz się zwadził,
Ten już z nim na tej ziemi nie zgodzi się szczérze,
I musi albo bić się, albo gnić w Sybirze.
Więc nic nie mówiąc, smutnie po sobie spójrzeli,
Westchnęli; na znak zgody głowami skinęli.

    Polak, chociaż stąd między narodami słynny
Że bardziej niźli życie kocha kraj rodzinny,
Gotów zawżdy rzucić go, puścić się w kraj świata,
W nędzy i poniewierce przeżyć długie lata,
Walcząc z ludźmi i z losem, póki mu śród burzy
Przyświeca ta nadzieja, że Ojczyźnie służy.

    Oświadczyli, że zaraz wyjeżdżać gotowi;
Tylko się to nie zdało panu Buchmanowi.
Buchman, człowiek rozsądny, w bitwę się nie wmieszał,
Ale słysząc, że radzą, głosować pośpieszał.
Znajdował projekt dobrym, lecz chciał przeinaczyć,
Dokładniej go rozwinąć, jaśniej wytłumaczyć,
A naprzód komisyją legalnie wyznaczyć,
Która by rozważyła emigracji cele,
Środki, sposoby, tudzież innych względów wiele.
Nieszczęściem, krótkość czasu była na zawadzie,
Że się nie stało zadość Buchmanowej radzie.
Szlachta żegna się śpiesznie i już w drogę rusza.

    Ale Sędzia zatrzymał w izbie Tadeusza
I rzekł do księdza: «Czas już, żebym ci powiedział
To, o czymem z pewnością wczoraj się dowiedział:
Że nasz Tadeusz szczerze zakochany w Zosi.
Niechajże przed odjazdem o rękę jej prosi.
Mówiłem z Telimeną, już nam nie przeszkadza,
Zosia także się z wolą opiekunów zgadza.
Jeśli dziś ślubem pary nie możem uwieńczyć,
Toć by ich, panie bracie, przynajmniej zaręczyć
Przed odjazdem; bo serce młode i podróżne,
Wiesz dobrze, jako miewa tentacyje różne;
A wszakże, kiedy okiem rzuci na pierścionek
I przypomni młodzieniec, że już jest małżonek,
Zaraz w nim obcych pokus ostyga gorączka.
Wierzaj mi, wielką siłę ma ślubna obrączka.

    Ja sam przed lat trzydziestu wielki afekt miałem
Ku pannie Marcie, której serce pozyskałem.
Byliśmy zaręczeni; Bóg nie błogosławił
Związkowi temu i mnie sierotą zostawił,
Wziąwszy do chwały swojej nadobną Wojszczankę,
Przyjaciela mojego córę Hreczeszankę.
Pozostała mi tylko pamiątka jej cnoty,
Jej wdzięków, i ten oto ślubny pierścień złoty.
Ilekroć nań spojrzałem, zawsze ma nieboga
Stawała przed oczyma: i tak z łaski Boga,
Dotąd mej narzeczonej dochowałem wiary,
I nie bywszy małżonkiem, jestem wdowiec stary,
Chociaż Wojski ma drugą córę dość nadobną,
I do mojej kochanej Marty dość podobną!»

    To mówiąc, na pierścionek z czułością spozierał
I odwróconą ręką łzy z oczu ocierał.
«Bracie — kończył — co myślisz? zrobim zaręczyny?
On kocha, a mam słowo ciotki i dziewczyny».

    Lecz Tadeusz podbiega i z żywością mówi:
«Czymże zdołam odwdzięczyć dobremu stryjowi,
Który tak o me szczęście ustawnie się trudzi!
Ach dobry stryju, byłbym najszczęśliwszy z ludzi,
Gdyby mi Zosia była dzisiaj zaręczona,
Gdybym wiedział że to jest moja przyszła żona.
Przecież powiem otwarcie: dziś, te zaręczyny
Do skutku przyjść nie mogą; są różne przyczyny…
Nie pytaj więcej; jeśli Zosia czekać raczy,
Może mnie wkrótce lepszym, godniejszym obaczy,
Może stałością na jej wzajemność zarobię,
Może troszeczką sławy me imię ozdobię,
Może wkrótce w ojczyste wrócim okolice;
Wtenczas, stryju, wspomnę ci twoje obietnice,
Wtenczas na klęczkach drogą powitam Zosienkę
I jeśli będzie wolna, poproszę o rękę.
Teraz porzucam Litwę może na czas długi,
Może Zosi tymczasem podobać się drugi;
Więzić jej woli nie chcę; prosić o wzajemność,
Na którąm nie zasłużył, byłaby nikczemność».

    Gdy te słowa z uczuciem mówił chłopiec młody,
Zaświeciły mu, jako dwie wielkie jagody
Pereł, dwie łzy na wielkich błękitnych źrenicach,
I stoczyły się szybko po rumianych licach.

    Ale Zosia ciekawa z głębiny alkowy
Śledziła przez szczelinę tajemne rozmowy;
Słyszała, jak Tadeusz po prostu i śmiało
Opowiedział swą miłość — serce w niej zadrżało —
I widziała tych wielkich dwoje łez w źrenicach.
Choć dojść nie mogła wątku w jego tajemnicach:
Dlaczego ją pokochał? dlaczego porzuca?
Gdzie odjeżdża? przecież ją ten odjazd zasmuca.
Pierwszy raz posłyszała w życiu z ust młodziana
Dziwną i wielką nowość: że była kochana.
Biegła więc, gdzie stał mały domowy ołtarzyk,
Wyjęła zeń obrazek i relikwijarzyk;
Na obrazku tym była święta Genowefa,
A w relikwiji suknia świętego Józefa,
Oblubieńca, patrona zaręczonej młodzi;
I z tymi świętościami do pokoju wchodzi.

    «Pan odjeżdżasz tak prędko?… Ja panu na drogę
Dam podarunek mały i także przestrogę:
Niechaj pan zawsze z sobą relikwije nosi
I ten obrazek, a niech pamięta o Zosi.
Niech pana Pan Bóg w zdrowiu i szczęściu prowadzi,
I niech prędko szczęśliwie do nas odprowadzi».
Umilkła i spuściła głowę; oczki modre
Ledwie stuliła, z rzęsów pobiegły łzy szczodre;
A Zosia z zamkniętymi stojąc powiekami,
Milczała, sypiąc łzami jako brylantami.

    Tadeusz, biorąc dary i całując rękę,
Rzekł: «Pani! już ja muszę pożegnać panienkę…
Bądź zdrowa, wspomnij o mnie i racz czasem zmówić
Pacierz za mnie! Zofijo!…» Więcej nie mógł mówić.

    Lecz Hrabia, z Telimeną wszedłszy niespodzianie,
Uważał młodej pary czułe pożegnanie,
Wzruszył się i rzuciwszy wzrok ku Telimenie:
«Ileż — rzekł — jest piękności choć w tej prostej scenie!
Kiedy dusza pasterki z wojownika duszą,
Jak łódź z okrętem w burzy, rozłączyć się muszą!
Zaiste! nic tak uczuć w sercu nie rozpala,
Jako kiedy się serce od serca oddala.
Czas jest to wiatr, on tylko małą świecę zdmuchnie,
Wielki pożar od wiatru tym mocniej wybuchnie.
I moje serce zdolne mocniej kochać z dala.
Panie Soplico! miałem ciebie za rywala;
Ten błąd był jedną z przyczyn naszej smutnej zwady,
Która mię przymusiła dostać na was szpady.
Postrzegam błąd mój: boś ty wzdychał ku pasterce,
Ja zaś tej pięknej nimfie oddałem me serce.
Niech we krwi wrogów nasze utoną urazy!
Nie będziem się zbójczymi rozpierać żelazy;
Niech się inaczej spór nasz zalotny roztrzygnie:
Walczmy, kto kogo czuciem miłości wyścignie!
Zostawim oba drogie serc naszych przedmioty,
Pośpieszymy obadwa na miecze, na groty;
Walczmy z sobą stałością, żalem i cierpieniem,
A wrogów naszych mężnym ścigajmy ramieniem».
Rzekł, na Telimenę spojrzał, ale ona
Nic nie odpowiadała, strasznie zadziwiona.

    «Mój Hrabio — przerwał Sędzia — po co chcesz koniecznie
Wyjeżdżać? Wierz mi, w twoich dobrach siedź bezpiecznie
Szlachtę biedną rząd mógłby odrzeć i przechłostać,
Ale ty Hrabio pewien jesteś cały zostać;
Wiesz, w jakim rządzie żyjesz, jesteś dość bogaty,
Wykupisz się od więzień połową intraty».

    «To niezgodna — rzekł Hrabia — z moim charakterem!
Nie mogę być kochankiem: będę bohaterem;
W miłości troskach, sławy zwę pocieszycielki,
Gdy jestem nędzarz sercem, będę ręką wielki».

    Telimena pytała: «Któż panu przeszkadza
Kochać i być szczęśliwym!» — «Mych przeznaczeń władza —
Rzekł Hrabia — ciemność przeczuć, które ruchem tajnym
Rwą się ku stronom obcym, dziełom nadzwyczajnym.
Wyznaję, że dziś chciałem na cześć Telimenie
U ołtarzów Hymena zapalić płomienie,
Ale mi dał zbyt piękny przykład ten młodzieniec,
Sam dobrowolnie ślubny swój zrywając wieniec,
I biegąc serca swego doświadczać w przeszkodach
Zmiennych losów i w krwawych wojennych przygodach.
Dziś otwiera się nowa i dla mnie epoka!
Brzmiała odgłosem broni mej Birbante-rokka:
Oby ten odgłos równie w Polszcze się rozszerzył!»
Skończył i dumnie szpady rękojeść uderzył.

    «Jużci — rzekł Robak — trudno ganić tę ochotę,
Jedź, weź pieniądze, możesz usztyftować rotę
Jak Włodzimierz Potocki, co Francuzów zdziwił
Dając na skarb milijon, jak książę Radziwiłł
Dominik, co zastawił dobra swe i sprzęty
I dwa uzbroił nowe konne regimenty.
Jedź, jedź, a weź pieniądze: rąk tam dosyć mamy,
Ale grosza brak w Księstwie; jedź wasze, żegnamy».

    Telimena smutnymi rzuciwszy oczyma:
«Niestety — rzekła — widzę że cię nic nie wstrzyma!
Rycerzu mój, w wojenne kiedy wstąpisz szranki,
Obróć czułe spojrzenie na kolor kochanki
(Tu, wstążkę oderwawszy od sukni, zrobiła
Kokardę i na piersiach Hrabi przyszpiliła).
Niech cię ten kolor wiedzie na działa ogniste,
Na kopije błyszczące i deszcze siarczyste;
A kiedy się rozsławisz walecznymi czyny,
I gdy nieśmiertelnymi przesłonisz wawrzyny
Skrwawiony szyszak i hełm twój zwycięstwem hardy:
I wtenczas jeszcze oko zwróć do tej kokardy,
Wspomnij, czyja ten kolor przyszpiliła ręka!»
Tu mu podała rękę. Pan Hrabia przyklęka,
Całuje; Telimena zbliżyła do oka
Chustkę, a drugim okiem pogląda z wysoka
Na Hrabię, który żegnał ją mocno wzruszony.
Ona wzdychała, ale ruszyła ramiony.

    Lecz Sędzia rzekł: «Mój Hrabio, śpiesz się, bo już późno,»
A ksiądz Robak «Dość tego! — wołał z miną groźną, —
Śpiesz się wasze!» Tak rozkaz Sędziego i księdza
Rozdziela czułą parę i z izby wypędza.

    Tymczasem pan Tadeusz stryja obejmował
Ze łzami i Robaka w rękę pocałował.
Robak, ku piersiom chłopca przycisnąwszy skronie
I na głowie mu na krzyż położywszy dłonie,
Spojrzał ku niebu i rzekł: «Synu! z Panem Bogiem!»
I zapłakał… A już był Tadeusz za progiem.
«Jak to? — zapytał Sędzia — nic mu brat nie powie
I teraz? Biedny chłopiec, jeszcze się nie dowie
O niczym przed odjazdem?…» «Nie — rzekł ksiądz — o niczym
(Płacząc długo z zakrytym rękami obliczem).
I po cóż by miał wiedzieć biedny, że ma ojca,
Który się skrył przed światem jak łotr, jak zabojca?
Bóg widzi, jak pragnąłbym: ale z tej pociechy
Zrobię Bogu ofiarę za me dawne grzechy».

    «Więc — rzecze Sędzia — teraz czas myśleć o sobie.
Uważ, że człowiek w twoim wieku i chorobie
Nie zdołałby z innymi razem emigrować;
Mówiłeś, że wiesz domek, gdzie się masz przechować:
Powiedz gdzie? Śpieszmy, czeka zaprzężona bryka.
Czy nie najlepiej w puszczę, do chaty leśnika?»

    Robak kiwając głową rzekł: «Do jutra rana
Mam czas. Teraz, mój bracie, poślij do plebana,
Aby tu jak najrychlej przybył z wijatykiem;
Oddal stąd wszystkich, zostań tylko sam z Klucznikiem,
Zamknij drzwi».

                        Sędzia spełnił Robaka rozkazy,
I usiada na łóżko przy nim; a Gerwazy,
Stoi, łokieć przytwierdza na głowni rapiera,
A czoło pochylone na dłoniach opiera.

    Robak, nim zaczął mówić, w Klucznika oblicze
Wzrok utkwił i milczenie chował tajemnicze.
A jako chirurg naprzód miękką rękę składa
Na ciele chorującym, nim ostrzem raz zada:
Tak Robak wyraz bystrych oczu swych złagodził,
Długo nimi po oczach Gerwazego wodził,
Na koniec, jakby ślepym chciał uderzyć ciosem,
Zasłonił oczy ręką i rzekł mocnym głosem:

    «Jam jest Jacek Soplica…»

                        Klucznik na to słowo
Pobladnął, pochylił się, i ciała połową
Wygięty naprzód, stanął, zwisł na jednej nodze,
Jak głaz lecący z góry zatrzymany w drodze.
Oczy roztwierał, usta szeroko rozszerzał,
Grożąc białymi zęby, a wąsy najeżał;
Rapier z rąk upuszczony przy ziemi zatrzymał
Kolanami i głownię prawą ręką imał,
Cisnąc ją: rapier z tyłu za nim wyciągniony,
Długim czarnym swym końcem chwiał się w różne strony;
I Klucznik był podobny rysiowi rannemu,
Który z drzewa ma skoczyć w oczy myśliwemu,
Wydyma się kłębuszkiem, mruczy, krwawe ślepie
Wyiskrza, wąsy rusza i ogonem trzepie.

    «Panie Rębajło — rzekł ksiądz — już mię nie zatrwożą
Gniewy ludzkie, bo jestem już pod ręką Bożą.
Zaklinam cię na imię Tego, co świat zbawił
I na krzyżu zabójcom swoim błogosławił,
I przyjął prośbę łotra: byś się udobruchał
I to, co mam powiedzieć, cierpliwie wysłuchał.
Sam przyznałem się: muszę dla ulgi sumienia
Pozyskać, a przynajmniej prosić przebaczenia:
Posłuchaj mej spowiedzi; potem zrobisz sobie
Ze mną, co zechcesz». I tu złożył ręce obie
Jak do pacierza. Klucznik cofnął się zdumiony,
Uderzał ręką w czoło i ruszał ramiony.

    A ksiądz zaczął swą dawną z Horeszką zażyłość
Opowiadać i swoją z jego córką miłość,
I swe z tego powodu z Stolnikiem zatargi.
Lecz mówił nieporządnie, często mieszał skargi
I żale we swą spowiedź, często rzecz przecinał,
Jak gdyby już ją kończył, i znowu zaczynał.

    Klucznik, dzieje Horeszków znający dokładnie,
Całą tę powieść, chociaż splątaną bezładnie,
Porządkował w pamięci i dopełniać umiał;
Lecz Sędzia wielu rzeczy zgoła nie rozumiał.
Oba pilnie słuchali pochyliwszy głowy,
A Jacek mówił coraz wolniejszymi słowy
I często zarywał się:

    «Wszak sam wiesz, Gerwazeńku, jak Stolnik zapraszał
Często mnie na biesiady, zdrowie moje wnaszał,
Krzyczał nieraz, do góry podniósłszy szklanicę,
Że nie miał przyjaciela nad Jacka Soplicę,
Jak on mnie ściskał! Wszyscy, którzy to widzieli,
Myślili, że on ze mną duszą się podzieli…
On przyjaciel?… On wiedział, co się wtenczas działo
W duszy mojej!…

    Tymczasem już szeptała o tym okolica,
Jaki taki gadał mi: »Ej, panie Soplica,
Daremnie konkurujesz: dygnitarskie progi
Za wysokie na Jacka podczaszyca nogi.«
Ja śmiałem się, udając że drwiłem z magnatów
I z córek ich, i nie dbam o arystokratów;
Że jeśli bywam u nich, z przyjaźni to robię,
A za żonę nie pojmę, tylko równą sobie.
Przecież, bodły mi duszę do żywca te żarty:
Byłem młody, odważny, świat był mnie otwarty
W kraju, gdzie, jako wiecie, szlachcic urodzony
Jest zarówno z panami kandydat korony!
Wszakże Tęczyński niegdyś z królewskiego domu
Żądał córy, a król mu oddał ją bez sromu.
Sopliców czyż nie równe Tęczyńskim zaszczyty
Krwią, herbem, wierną służbą Rzeczypospolitej?

    Jak łatwo może człowiek popsuć szczęście drugim
W jednej chwili, a życiem nie naprawi długim!
Jedno słowo Stolnika: jakże byśmy byli
Szczęśliwi! Kto wie, może dotąd byśmy żyli,
Może i on przy swoim kochanym dziecięciu,
Przy swojej pięknej Ewie, przy swym wdzięcznym zięciu,
Zestarzałby spokojny, może wnuki swoje
Kołysałby!… Teraz co?… Nas zgubił oboje
I sam… i to zabójstwo… i wszystkie następstwa
Tej zbrodni, wszystkie moje biedy i przestępstwa!…
Ja skarżyć nie mam prawa: ja jego morderca,
Ja skarżyć nie mam prawa: przebaczam mu z serca,
Ale i on…

    Żeby już raz otwarcie był mnie zrekuzował!…
Bo znał nasze uczucia… Gdyby nie przyjmował
Mych odwiedzin: to kto wie? może bym odjechał,
Pogniewał się, połajał, w końcu go zaniechał;
Ale on, chytrze dumny, wpadł na koncept nowy:
Udawał, że mu nawet nie przyszło do głowy,
Żeby ja mógł się starać o związek takowy!
A byłem mu potrzebnym: miałem zachowanie
U szlachty i lubili mnie wszyscy ziemianie:
Więc on niby miłości mojej nie dostrzegał,
Przyjmował mnie jak dawniej, a nawet nalegał
Abym częściej przyjeżdżał; a ilekroć sami
Byliśmy, widząc oczy me przyćmione łzami
I pierś zbyt pełną i już wybuchnąć gotową,
Chytry starzec, wnet wrzucił obojętne słowo
O procesach, sejmikach, łowach…

    Ach, nieraz przy kieliszkach, gdy się tak rozrzewniał,
Gdy mię tak ściskał i o przyjaźni zapewniał,
Potrzebując mej szabli lub kreski na sejmie,
Gdy musiałem nawzajem ściskać go uprzejmie:
To tak we mnie złość wrzała, że ja obracałem
Ślinę w gębie, a dłonią rękojeść ściskałem,
Chcąc plunąć na tę przyjaźń i wnet szabli dostać;
Ale Ewa, zważając mój wzrok i mą postać,
Zgadywała, nie wiem jak, co się we mnie działo,
Patrzyła błagająca, lice jej bledniało;
A był to taki piękny gołąbek łagodny
I wzrok miała uprzejmy taki! tak pogodny!
Taki anielski, że już nie wiem, już nie miałem
Odwagi zagniewać jej, zatrwożyć — milczałem.
I ja, zawadyjaka sławny w Litwie całéj,
Co przede mną największe pany niegdyś drżały,
Com nie żył dnia bez bitki, co, nie Stolnikowi,
Ale bym się pokrzywdzić nie dał i królowi,
Co we wściekłość najmniejsza wprawiała mnie sprzeczka:
Ja wtenczas, zły i pjany, milczał jak owieczka,
Jak gdybym Sanktissimum ujrzał!

    Ileż to razy chciałem serce me otworzyć,
I już się nawet przed nim do próśb upokorzyć,
Lecz spojrzawszy mu w oczy, spotkawszy wejrzenia
Zimne jak lód, wstyd mi było mojego wzruszenia;
Śpieszyłem znowu jak najzimniej dyskurować
O sprawach, o sejmikach, a nawet żartować!!
Wszystko to, prawda, z pychy: żeby nie ubliżyć
Imieniowi Sopliców, żeby się nie zniżyć
Przed panem prośbą próżną, nie dostać odmowy,
Bo jakież by to były między szlachtą mowy,
Gdyby wiedziano, że ja Jacek…

    Soplicy Horeszkowie odmówili dziewkę!
Że mnie, Jackowi, czarną podano polewkę!

    W końcu sam już nie wiedząc, jak sobie poradzić,
Umyśliłem ze szlachty mały pułk zgromadzić
I opuścić na zawsze powiat i ojczyznę,
Wynieść się gdzie na Moskwę lub na Tatarszczyznę
I zacząć wojnę. Jadę pożegnać Stolnika,
W nadziei, że gdy ujrzy wiernego stronnika,
Dawnego przyjaciela, prawie domownika,
Z którym pił i wojował przez tak długie lata,
Teraz żegnającego i kędyś w kraj świata
Jadącego — że może starzec się poruszy
I pokaże mi przecież trochę ludzkiej duszy
Jak ślimak rogów!

    Ach, kto choć na dnie serca ma dla przyjaciela
Choćby iskierkę czucia, gdy się z nim rozdziela,
Dobędzie się iskierka ta przy pożegnaniu,
Jako ostatni płomyk życia przy skonaniu!
Raz ostatni dotknąwszy przyjaciela skroni,
Częstokroć najzimniejsze oko łzę uroni!

    Biedna, słysząc o moim odjeździe, pobladła,
Bez przytomności, ledwie że trupem nie padła,
Nie mogła nic przemówić: aż się jej rzuciły
Strumieniem łzy — poznałem, jak byłem jej miły!

    Pomnę, pierwszy raz w życiu jam się łzami zalał
Z radości i z rozpaczy, zapomniał się, szalał.
Już chciałem znowu upaść ojcu jej pod nogi,
Wić się jak wąż u kolan, wołać: »Ojcze drogi,
Weź za syna lub zabij!« Wtem Stolnik posępny,
Zimny jako słup soli, grzeczny, obojętny,
Wszczął dyskurs — o czym? o czym? o córki weselu!…
W tej chwili! O Gerwazy! uważ, przyjacielu,
Masz ludzkie serce!

                        Stolnik rzekł: »Panie Soplica,
Właśnie przyjechał do mnie swat kasztelanica;
Ty jesteś mój przyjaciel, cóż ty mówisz na to?
Wiesz wasze, że mam córkę piękną i bogatą:
A kasztelan — witebski! Wszakże to w senacie
Niskie, drążkowe krzesło. Cóż mi radzisz, bracie?«
Nie pamiętam już zgoła co mu na to rzekłem,
Podobno nic — na konia wsiadłem i uciekłem!…»

    «Jacku! zawołał Klucznik, mądre ty przyczyny
Wynajdujesz: cóż? one nie zmniejszą twej winy!
Bo wszakże zdarzało się już nieraz na świecie,
Że kto pokochał pańskie lub królewskie dziecię,
Starał się gwałtem zdobyć, przemyślał wykradać,
Mścił się otwarcie — ale tak chytrze śmierć zadać,
Panu polskiemu, w Polszcze — i w zmowie z Moskalem!»

    «Nie byłem w zmowie — Jacek odpowiedział z żalem. —
Gwałtem porwać? Wszak mógłbym: zza krat i zza klamek
Wydarłbym ją, rozbiłbym w puch ten jego zamek!
Miałem za sobą Dobrzyn i cztery zaścianki!
Ach, gdyby ona była jak nasze szlachcianki
Silna i zdrowa! gdyby ucieczki, pogoni
Nie zlękła się i mogła słuchać szczęku broni!…
Lecz ona biedna! tak ją, rodzice pieścili,
Słaba, lękliwa! był to robaczek motyli,
Wiosenna gąsiennica! i tak ją zagrabić,
Dotknąć ją zbrojną ręką, byłoby ją zabić;
Nie mogłem, nie.

    Mścić się otwarcie? szturmem zamek zwalić w gruzy?
Wstyd!… bo by powiedziano, żem mścił się rekuzy!
Kluczniku, twoje serce poczciwe nie umie
Uczuć, ile jest piekła w obrażonej dumie.

    Szatan dumy zaczął mi lepsze plany raić:
Zemścić się krwawo, ale powód zemsty taić,
Nie bywać w zamku, miłość z serca wykorzenić,
Puścić w niepamięć Ewę, z inną się ożenić,
A potem, potem jaką wynaleźć zaczepkę,
Pomścić się…

    I zdało mi się zrazu, żem już serce zmienił,
I rad byłem z wymysłu i — jam się ożenił;
Z pierwszą, którąm napotkał, dziewczyną ubogą!
Źlem zrobił — jakże byłem ukarany srogo!
Nie kochałem jej. Biedna matka Tadeusza
Najprzywiązańsza do mnie, najpoczciwsza dusza —
Ale jam dawną miłość i złość w sercu dusił.
Byłem jako szalony, darmom siebie musił
Zająć się gospodarstwem albo interesem:
Wszystko na próżno! Zemsty opętany biesem,
Zły, opryskliwy, znaleźć nie mogłem pociechy
W niczym na świecie — i tak z grzechów w nowe grzechy,
Zacząłem pić.

    I tak niedługo żona ma z żalu umarła,
Zostawiwszy to dziecię; a mnie rozpacz żarła!

    Jakże mocno musiałem kochać tę niebogę,
Tyle lat!… Gdziem ja nie był: a dotąd nie mogę
Jej zapomnieć i zawżdy jej postać kochana
Stoi mi przed oczyma jakby malowana!
Piłem, nie mogłem zapić pamięci na chwilę,
Ani pozbyć się, chociaż przebiegłem ziem tyle!
Teraz oto w habicie jestem Bożym sługą,
Na łożu, we krwi… o niej mówiłem tak długo! —
W tej chwili, o tych rzeczach mówić? Bóg wybaczy!
Musicie wiedzieć, w jakim żalu i rozpaczy
Popełniłem…

    Było to właśnie wkrótce po jej zaręczynach.
Wszędzie gadano tylko o tych zaręczynach;
Powiadano, że Ewa, gdy brała obrączkę
Z rąk Wojewody, mdlała, że wpadła w gorączkę,
Że ma początki suchot, że ustawnie szlocha;
Zgadywano, że kogoś potajemnie kocha. —
Ale Stolnik, jak zawsze spokojny, wesoły,
Dawał na zamku bale, zbierał przyjacioły.
Mnie już nie prosił: na cóż byłem mu potrzebny?
Mój bezład w domu, bieda, mój nałóg haniebny,
Podały mnie na wzgardę i na śmiech przed światem!
Mnie, com niegdyś, rzec mogę, trząsł całym powiatem!
Mnie, którego Radziwiłł nazywał: kochanku!
Mnie, com kiedy wyjeżdżał z mojego zaścianku,
To liczniejszy dwór miałem niżeli książęcy,
Kiedym szablę dostawał, to kilka tysięcy
Szabel błyszczało wkoło, strasząc zamki pańskie!
A potem ze mnie śmiały się dzieci włościańskie!
Tak zrobiłem się nagle w oczach ludzkich lichy!
Jacek Soplica! — Kto zna co jest czucie pychy…»

    Tu bernardyn osłabiał i upadł na łoże;
A Klucznik rzekł wzruszony: «Wielkie sądy Boże!
Prawda! prawda! Więc to ty? i tyżeś to Jacku
Soplico? pod kapturem? żyłeś po żebracku!
Ty, którego pamiętam, gdy zdrowy, rumiany,
Piękny szlachcic, gdy tobie pochlebiały pany,
Gdy za tobą, kobiety szalały! Wąsalu!
Nie tak dawno! takeś zestarzał się z żalu!
Jakżem ciebie nie poznał po owym wystrzale,
Kiedyś tak do niedźwiedzia trafił doskonale?
Bo nad ciebie nie miała strzelca Litwa nasza,
Byłeś także po Maćku pierwszy do pałasza!
Prawda! o tobie niegdyś śpiewały szlachcianki:
*Oto Jacek wąs kreci, trzęsą się zaścianki,*
*A komu na swym wąsie węzełek zawiąże,*
*Ten zadrży, choćby to był sam Radziwiłł książę.*
Zawiązałeś ty węzeł i mojemu Panu!
Nieszczęśniku!… I tyżeś? do takiego stanu?
Jacek Wąsal kwestarzem? Wielkie sądy Boże!…
I teraz, ha! bezkarnie ujść tobie nie może,
Przysięgam: kto Horeszków krwi kroplę wysączył…»

    Tymczasem ksiądz na łożu usiadł i tak kończył:
«Jeździłem koło zamku. Ile biesów w głowie
I w sercu miałem: kto ich imiona wypowie!
Stolnik zabija dziecię własne! Mnie już zabił,
Zniszczył!… Jadę pod bramę: szatan mnie tam wabił.
Patrz, jak on hula! Co dzień w zamku pijatyka,
Ile świec w oknach, jaka brzmi w salach muzyka!
I ten zamek na łysą głowę mu nie runie?…

    Pomyśl o zemście, to wnet szatan broń podsunie.
Ledwiem pomyślił: szatan nasyła Moskali.
Stałem patrząc; wiesz, jak wasz zamek szturmowali.

    Bo fałsz, żebym był w jakiej z Moskalami zmowie…

    Patrzyłem. Różne myśli snuły się po głowie.
Zrazu z uśmiechem głupim, jak na pożar dziecko,
Patrzyłem; potem radość uczułem zbójecką,
Czekając rychło zacznie palić się i walić;
Czasem myśl przychodziła skoczyć, ją ocalić,
Nawet Stolnika…

    Broniliście się, ty wiesz, dzielnie i przytomnie.
Zdziwiłem się. Moskale padali wkoło mnie.
Bydlęta, źle strzelają! Na widok ich klęski
Złość mię znowu porwała. — Ten Stolnik zwycięski!
I także mu na świecie wszystko się powodzi?
I z tej strasznej napaści z tryumfem wychodzi?
Odjeżdżałem ze wstydem. Właśnie był poranek.
Wtem ujrzałem, poznałem. Wystąpił na ganek,
I brylantową szpinką ku słońcu migotał,
I wąs pokręcał dumnie, i wzrok dumny miotał…
I zdało mi się, że mnie szczególniej urągał,
Że mnie poznał i ku mnie rękę tak wyciągał,
Szydząc i grożąc… Chwytam karabin Moskala,
Ledwiem przyłożył, prawie nie mierzył — wypala!
Wiesz!…

    Przeklęta broń ognista!… Kto mieczem zabija,
Musi składać się, natrzeć, odbija, wywija,
Może rozbroić wroga, miecz wpół drogi wstrzymać;
Ale ta broń ognista… dosyć zamek imać,
Chwila, jedna iskierka…

    Czyż uciekałem, kiedyś mierzył do mnie z góry?
Utkwiłem oczy we dwie twojej broni rury;
Rozpacz jakaś, żal dziwny do ziemi mnie przybił!
Czemuż? ach mój Gerwazy, czemuś wtenczas chybił?
Łaskę byś zrobił!… Widać, za pokutę grzechu
Trzeba było…»

                        Tu znowu brakło mu oddechu.
«Bóg widzi — rzecze Klucznik — szczerze trafić chciałem!
Ileż ty krwi wylałeś twoim jednym strzałem,
Ileż klęsk spadło na nas i na twą rodzinę,
A wszystko to przez waszą, panie Jacku, winę!
A wszakże, gdy dziś jegry Hrabię na cel wzięli,
Ostatniego z Horeszków chociaż po kądzieli,
Tyś go zasłonił, i gdy Moskal do mnie palił,
Tyś mnie rzucił o ziemię: tak nas dwóch ocalił.
Jeśli prawda, że jesteś księdzem zakonnikiem,
Jużci sukienka broni cię przed Scyzorykiem.
Bądź zdrów, więcej na waszym nie postanę progu
Z nami kwita, — zostawmy resztę Panu Bogu».

    Jacek rękę wyciągnął, — cofnął się Gerwazy,
«Nie mogę — rzekł — bez mego szlachectwa obrazy
Dotykać rękę, takim morderstwem skrwawioną
Z prywatnej zemsty, nie zaś pro publico bono!»

    Ale Jacek z poduszek na łoże upadłszy,
Zwrócił się ku Sędziemu, a był coraz bladszy,
I niespokojnie pytał o księdza plebana,
I wołał na Klucznika: «Zaklinam waćpana
Abyś został. Wnet skończę. Ledwie mam dość mocy
Zakończyć — Panie Klucznik, ja umrę tej nocy!»

    «Co bracie? — krzyknął Sędzia — widziałem, wszak rana
Niewielka, co ty mówisz? po księdza plebana?
Może źle opatrzono — zaraz po doktora,
W apteczce jest…» Ksiądz przerwał: «Bracie, już nie pora!
Miałem tam strzał dawniejszy, dostałem pod Jena,
Źle zgojony, a teraz draśniono: gangrena
Już tu… Znam się na ranach, patrz, jaka krew czarna,
Jak sadza. Co tu doktor?… Ale to rzecz marna.
Raz umieramy: jutro czy dziś oddać duszę —
Panie Klucznik, przebaczysz mnie, ja skończyć muszę!

    Jest w tym zasługa nie chcieć zostać winowajcą
Narodowym, choć naród okrzyczy cię zdrajcą!
Zwłaszcza, w kim taka, jaka była we mnie duma!

    Imię zdrajcy przylgnęło do mnie jako dżuma.
Odwracali ode mnie twarz obywatele,
Uciekali ode mnie dawni przyjaciele;
Kto był lękliwy, z dala witał się i stronił:
Nawet lada chłop, lada Żyd, choć się pokłonił,
To mię zboku szyderskim przebijał uśmiechem.
Wyraz zdrajca brzmiał w uszach, odbijał się echem
W domu, w polu. Ten wyraz od rana do zmroku
Wił się przede mną, jako plama w chorym oku.
Przecież nie byłem zdrajcą kraju.

    Moskwa mnie uważała gwałtem za stronnika.
Dano Soplicom znaczną część dóbr nieboszczyka;
Targowiczanie potem chcieli mnie zaszczycić
Urzędem. — Gdybym wtenczas chciał się przemoskwicić!
Szatan radził — Już byłem możny i bogaty;
Gdybym został Moskalem, najpierwsze magnaty
Szukałyby mych względów; nawet szlachta braty,
Nawet gmin, który swoim tak łacnie uwłacza,
Tym którzy Moskwie służą, szczęśliwszym,— przebacza!
Wiedziałem to, a przecież — nie mogłem.

    Uciekłem z kraju!…
Gdziem nie był! com nie cierpiał!…

    Aż Bóg raczył lekarstwo jedyne objawić:
Poprawić się potrzeba było i naprawić
Ile możności to…

    Córka Stolnika ze swym mężem wojewodą,
Gdzieś w Sybir wywieziona, tam umarła młodo;
Zostawiła tę w kraju córkę, małą Zosię;
Kazałem ją hodować…

    Bardziej niźli z miłości, może z głupiej pychy,
Zabiłem; więc pokora… wszedłem między mnichy.
Ja, niegdyś dumny z rodu, ja, com był junakiem,
Spuściłem głowę, kwestarz, zwałem się Robakiem,
Że jako robak w prochu…

    Zły przykład dla ojczyzny, zachętę do zdrady
Trzeba było okupić dobrymi przykłady,
Krwią, poświęceniem się…

    Biłem się za kraj; gdzie? jak? zmilczę; nie dla chwały
Ziemskiej biegłem tylekroć na miecze, na strzały.
Milej sobie wspominam nie dzieła waleczne
I głośne, ale czyny ciche, użyteczne,
I cierpienia, których nikt…

    Udało mi się nieraz do kraju przedzierać,
Rozkazy wodzów nosić, wiadomości zbierać,
Układać zmowy — znają i Galicyjanie
Ten kaptur mnisi — znają i Wielkopolanie!
Pracowałem przy taczkach rok w pruskiej fortecy;
Trzy razy Moskwa kijmi zraniła me plecy,
Raz już wiedli na Sybir; potem Austryjacy,
W Szpilbergu zakopali mnie w lochach do pracy,
W carcer durum… a Pan Bóg wybawił mnie cudem,
I pozwolił umierać między swoim ludem
Z sakramentami…

    Może i teraz, kto wie? możem znowu zgrzeszył!
Możem nad rozkaz wodzów powstanie przyśpieszył!
Ta myśl, że dom Sopliców pierwszy się uzbroi,
Że pierwszą Pogoń w Litwie zatkną krewni moi!…
Ta myśl… zdaje się czysta…

    Chciałeś zemsty? masz!… Boś ty był narzędziem kary
Bożej, twoim Bóg mieczem rozciął me zamiary:
Tyś wątek spisku tyle lat snowany splątał!
Cel wielki, który całe życie me zaprzątał,
Ostatnie moje ziemskie uczucie na świecie,
Którem tulił, hodował jak najmilsze dziecię,
Tyś zabił w oczach ojca — a jam ci przebaczył!
Ty!…»

    «Oby tylko równie Bóg przebaczyć raczył! —
Przerwał Klucznik — jeżeli masz przyjąć wijatyk,
Księże Jacku: toć ja nie luter, nie syzmatyk!
Kto umierającego smuci, wiem, że grzeszy.
Powiem tobie coś, pewnie to ciebie pocieszy.
Kiedy nieboszczyk Pan mój upadał zraniony,
A ja klęcząc nad jego piersią pochylony
I miecz maczając w ranę, zemstę zaprzysiągnął,
Pan głowę wstrząsnął, rękę ku bramie wyciągnął
W stronę, gdzie stałeś, i krzyż w powietrzu naznaczył;
Mówić nie mógł, lecz dał znak, że zbójcy przebaczył.
Ja też pojąłem: ale tak się z gniewu wściekłem,
Że o tym krzyżu nigdy i słowa nie rzekłem».

    Tu rozmowę przerwały chorego cierpienia,
I nastąpiła długa godzina milczenia.
Oczekują plebana. Podkowy zagrzmiały,
Zastukał do komnaty arendarz zdyszały:
List ma ważny, samemu Jackowi pokaże.
Jacek bratu oddaje, głośno czytać każe.
List od Fiszera, który był natenczas szefem
Sztabu armii polskiej pod Księciem Józefem.
Donosi, że w cesarskim tajnym gabinecie
Stanęła wojna; cesarz już po całym świecie
Ogłasza ją, sejm walny w Warszawie zwołany,
I skonfederowane mazowieckie stany
Wyrzekną uroczyście przyłączenie Litwy.

    Jacek, słuchając, cicho odmówił modlitwy;
Przycisnąwszy do piersi święconą gromnicę,
Podniósł w niebo zatlone nadzieją źrenice,
I zalał się ostatnich łez rozkosznych zdrojem:
«Teraz rzekł, Panie, sługę twego puść z pokojem!»
Wszyscy uklękli; a wtem ozwał się pod progiem
Dzwonek: znak, że przyjechał pleban z Panem Bogiem.

    Właśnie już noc schodziła i przez niebo mleczne,
Różowe, biegą pierwsze promyki słoneczne.
Wpadły przez szyby jako strzały brylantowe,
Odbiły się na łożu o chorego głowę
I ubrały mu złotem oblicze i skronie,
Że błyszczał jako święty w ognistej koronie.




Księga jedenasta



Rok 1812

Wróżby wiosenne — Wkroczenie wojsk — Nabożeństwo — Rehabilitacja urzędowa śp. Jacka Soplicy — Z rozmów Gerwazego i Protazego wnosić można bliski koniec procesu — Umizgi ułana z dziewczyną — Rozstrzyga się spór o Kusego i Sokoła — Za czym goście zgromadzają się na biesiadę — Przedstawienie wodzom par narzeczonych.

    O roku ów! kto ciebie widział w naszym kraju!
Ciebie lud zowie dotąd rokiem urodzaju,
A żołnierz rokiem wojny; dotąd lubią starzy
O tobie bajać, dotąd pieśń o tobie marzy.
Z dawna byłeś niebieskim oznajmiony cudem
I poprzedzony głuchą wieścią między ludem;
Ogarnęło Litwinów serca z wiosny słońcem
Jakieś dziwne przeczucie, jak przed świata końcem,
Jakieś oczekiwanie tęskne i radosne.

    Kiedy pierwszy raz bydło wygnano na wiosnę,
Uważano, że chociaż zgłodniałe i chude,
Nie biegło na ruń, co już umaiła grudę,
Lecz kładło się na rolę i, schyliwszy głowy,
Ryczało albo żuło swój pokarm zimowy.

    I wieśniacy, ciągnący na jarzynę pługi,
Nie cieszą się jak zwykle z końca zimy długiéj,
Nie śpiewają piosenek: pracują leniwo,
Jakby nie pamiętali na zasiew i żniwo.
Co krok wstrzymują woły i podjezdki w bronie
I poglądają z trwogą ku zachodniej stronie,
Jakby z tej strony miał się objawić cud jaki,
I uważają z trwogą wracające ptaki.

    Bo już bocian przyleciał do rodzinnej sosny
I rozpiął skrzydła białe, wczesny sztandar wiosny;
A za nim, krzykliwymi nadciągnąwszy pułki,
Gromadziły się ponad wodami jaskółki
I z ziemi zmarzłej brały błoto na swe domki.
W wieczór słychać w zaroślach szept ciągnącej słomki
I stada dzikich gęsi szumią ponad lasem,
I znużone na popas spadają z hałasem,
A w głębi ciemnej nieba, wciąż jęczą żurawie.
Słysząc to, nocni stróże pytają w obawie,
Skąd w królestwie skrzydlatym tyle zamieszania,
Jaka burza te ptaki tak wcześnie wygania?

    Aż oto nowe stada: jakby gilów, siewek
I szpaków, stada jasnych kit i chorągiewek
Zajaśniały na wzgórkach, spadają na błonie:
Konnica! Dziwne stroje, niewidziane bronie!
Pułk za pułkiem; a środkiem, jak stopione śniegi,
Płyną drogami kute żelazem szeregi;
Z lasów czernią się czapki, rzęd bagnetów błyska,
Roją się nieźliczone piechoty mrowiska.

    Wszyscy na północ: rzekłbyś, że w on czas z wyraju
Za ptastwem i lud ruszył do naszego kraju,
Pędzony niepojętą, instynktową mocą.

    Konie, ludzie, armaty, orły, dniem i nocą
Płyną; na niebie gorą tu i ówdzie łuny,
Ziemia drży, słychać, biją stronami pioruny. —

    Wojna! wojna! Nie było w Litwie kąta ziemi,
Gdzie by jej huk nie doszedł. Pomiędzy ciemnemi
Puszczami, chłop, którego dziady i rodzice
Pomarli, nie wyjrzawszy za lasu granice,
Który innych na niebie nie rozumiał krzyków
Prócz wichrów, a na ziemi prócz bestyi ryków,
Gości innych nie widział oprócz spółleśników, —
Teraz widzi: na niebie dziwna łuna pała,
W puszczy łoskot, to kula od jakiegoś działa,
Zbłądziwszy z pola bitwy, dróg w lesie szukała,
Rwąc pnie, siekąc gałęzie. Żubr, brodacz sędziwy,
Zadrżał we mchu, najeżył długie włosy grzywy,
Wstaje na wpół, na przednich nogach się opiera,
I potrząsając brodą, zdziwiony spoziera
Na błyskające nagle między łomem zgliszcze:
Był to zbłąkany granat, kręci się, wre, świszcze,
Pękł z hukiem jakby piorun; żubr pierwszy raz w życiu,
Zląkł się i uciekł w głębszym schować się ukryciu.

    Bitwa! gdzie? w której stronie? pytają młodzieńce,
Chwytają broń; kobiety wznoszą w niebo ręce;
Wszyscy pewni zwycięstwa, wołają ze łzami:
«Bóg jest z Napoleonem, Napoleon z nami!»

    O wiosno! kto cię widział wtenczas w naszym kraju,
Pamiętna wiosno wojny, wiosno urodzaju!
O wiosno, kto cię widział, jak byłaś kwitnąca
Zbożami i trawami, a ludźmi błyszcząca,
Obfita we zdarzenia, nadzieją brzemienna!
Ja ciebie dotąd widzę, piękna maro senna!
Urodzony w niewoli, okuty w powiciu,
Ja tylko jedną taką wiosnę miałem w życiu.

    Soplicowo leżało tuż przy wielkiej drodze,
Którą od strony Niemna ciągnęli dwaj wodze:
Nasz książę Józef i król Westfalski Hieronim.
Już zajęli część Litwy od Grodna po Słonim:
Gdy król rozkazał wojsku dać trzy dni wytchnienia.
Ale polscy żołnierze mimo utrudzenia
Skarżyli się, że król im marszu nie dozwala;
Tak radzi by co prędzej doścignąć Moskala.

    W mieście pobliskim stanął główny sztab książęcy,
A w Soplicowie obóz czterdziestu tysięcy,
I ze sztabami swymi jenerał Dąbrowski,
Kniaziewicz, Małachowski, Giedrojć i Grabowski.

    Późno było, gdy weszli: więc każdy, gdzie może,
Zabierają kwatery w zamczysku, we dworze.
Skoro dano rozkazy, rozstawiono czaty,
Każdy strudzony poszedł spać do swej komnaty,
Z nocą wszystko ucichło: obóz, dwór i pole;
Widać tylko, jak cienie, błądzące patrole,
I gdzieniegdzie błyskania ognisk obozowych,
Słychać kolejne hasła stanowisk wojskowych.

    Spali gospodarz domu, wodze i żołnierze;
Oczu tylko Wojskiego sen słodki nie bierze.
Bo Wojski ma na jutro biesiadę wyprawić,
Którą chce dom Sopliców na wiek wieków wsławić:
Biesiadę godną miłych sercom polskim gości
I odpowiedną wielkiej dnia uroczystości,
Co jest świętem kościelnym i świętem rodziny:
Jutro odbyć się mają trzech par zaręczyny.
Zaś jenerał Dąbrowski oświadczył z wieczora,
Że chce mieć obiad polski.

                        Choć spóźniona pora,
Wojski zebrał co prędzej z sąsiedztwa kucharzy:
Pięciu ich było; służą, on sam gospodarzy.
Jako kuchmistrz białym się fartuchem opasał,
Wdział szlafmycę, a ręce do łokciów zakasał;
W ręku ma plackę muszą, owad lada jaki
Opędza, wpadający chciwie na przysmaki;
Drugą ręką przetarte okulary włożył,
Dobył z zanadrza księgę, odwinął, otworzył.

    Księga ta miała tytuł: Kucharz doskonały.
W niej spisane dokładnie wszystkie specyjały
Stołów polskich; podług niej hrabia na Tęczynie
Dawał owe biesiady we włoskiej krainie,
Którym się Ojciec Święty Urban Ósmy dziwił;
Podług niej później Karol-Kochanku-Radziwiłł,
Gdy przyjmował w Nieświeżu króla Stanisława,
Sprawił pamiętną ową ucztę, której sława
Dotąd żyje na Litwie we gminnej powieści.

    Co Wojski wyczytawszy pojmie i obwieści,
To natychmiast kucharze robią umiejętni.
Wre robota; pięćdziesiąt nożów w stoły tętni,
Zwijają się kuchciki czarne jak szatany:
Ci niosą drwa, ci z mlekiem i z winem sagany;
Leją w kotły, skowrody, w rondle, dym wybucha;
Dwóch kuchcików przy piecu siedzi, w mieszki dmucha,
Wojski, ażeby ogień tym łacniej rozpalać,
Rozkazał stopionego masła na drwa nalać
(Zbytek ten dozwolony jest w dostatnim domu).
Kuchciki sypią w ogień suche pęki łomu;
Inni na rożny sadzą ogromne pieczenie
Wołowe, sarnie, combry dzicze i jelenie;
Ci skubią stosy ptastwa, lecą puchów chmury,
Obnażają się głuszce, cietrzewie i kury.
Lecz kur niewiele było: od owej wyprawy,
Którą w czasie zajazdu Dobrzyński Sak krwawy
Zrobił na kurnik, kędy Zosi gospodarstwo
Zniszczył, nie zostawiwszy sztuki na lekarstwo,
Jeszcze nie mogło ptastwem zakwitnąć na nowo
Sławne niegdyś ze drobiu swego Soplicowo.
Zresztą zaś miąs wszelakich był wielki dostatek,
Co się zgromadzić dało i z domu, i z jatek,
I z lasów, i z sąsiedztwa, z bliska i z daleka:
Rzekłbyś, ptasiego tylko nie dostaje mleka.
Dwie rzeczy, których hojny pan do uczty szuka,
Łączą się w Soplicowie: dostatek i sztuka.

    Już wschodził uroczysty dzień *Najświętszej Panny*
*Kwietnej*. Pogoda była prześliczna, czas ranny;
Niebo czyste, wokoło ziemi obciągnięte,
Jako morze wiszące, ciche, wklęsło-wgięte,
Kilka gwiazd świeci z głębi, jako perły ze dna
Przez fale; z boku chmura biała, sama jedna,
Podlatuje i skrzydła w błękicie zanurza,
Podobne do niknących piór Anioła Stróża,
Który nocną modlitwą ludzi przytrzymany
Spóźnił się, śpieszy wracać między spółniebiany.

    Już ostatnie perły gwiazd zamierzchły i na dnie
Niebios zgasły, i niebo środkiem czoła bladnie.
Prawą skronią złożone na wezgłowiu cieni
Jeszcze smagławe, lewą coraz się rumieni;
A dalej okrąg, jakby powieka szeroka
Rozsuwa się i w środku widać białek oka,
Widać tęczę, źrenicę — już promień wytrysnął,
Po okrągłych niebiosach wygięty przebłysnął,
I w białej chmurce jako złoty grot zawisnął.
Na ten strzał, na dnia hasło, pęk ogniów wylata,
Tysiąc rac krzyżuje się po okręgu świata,
A oko słońca weszło. Jeszcze nieco senne,
Przymruża się, drżąc wstrząsa swe rzęsy promienne,
Siedmią barw błyszczy razem: szafirowe razem,
Razem krwawi się w rubin i żółknie topazem;
Aż rozlśniło się jako kryształ przezroczyste,
Potem jak brylant światłe, na koniec ogniste,
Jak księżyc wielkie, jako gwiazda migające:
Tak po nieźmiernym niebie szło samotne słońce.

    Dziś pospólstwo litewskie z całej okolicy
Zebrało się przed wschodem wokoło kaplicy,
Jak gdyby na nowego ogłoszenie cudu.
Zbiór ten pochodził w części z pobożności ludu,
A w części z ciekawości: bo dziś w Soplicowie
Na nabożeństwie mają być jenerałowie,
Sławni dowódcy owi naszych legijonów,
Których lud znał imiona i czcił jak patronów,
Których wszystkie tułactwa, wyprawy i bitwy
Były ewangeliją narodową Litwy.

    Już przyszło oficerów kilku, tłum żołnierzy;
Lud ich otacza, patrzy, ledwie oczom wierzy,
Oglądając rodaków mundury noszących,
Zbrojnych, wolnych i polskim językiem mówiących.

    Wyszła msza. Nie obejmie świątynia maleńka
Całego zgromadzenia: lud na trawie klęka;
Patrząc we drzwi kaplicy, odkrywają głowy.
Włos litewskiego ludu, biały albo płowy,
Pozłacał się jako łan dojrzałego żyta;
Gdzieniegdzie kraśna główka dziewicza wykwita,
Ubrana w świeże kwiaty albo w pawie oczy
I wstęgi rozplecione, ozdoby warkoczy,
Śród głów męskich jak w zbożu bławat i kąkole.
Klęczący różnobarwny tłum okrywa pole,
A na głos dzwonka, niby na wiatru powianie,
Chylą się wszystkie głowy jak kłosy na łanie.

    Wieśniaczki dziś na ołtarz Matki Zbawiciela
Niosą pierwszy dar wiosny, świeże snopki ziela;
Wszystko wkoło ubrane w bukiety i w wianki,
Ołtarz, obraz, a nawet dzwonica i ganki.
Czasem poranny wietrzyk, gdy ze wschodu wionie,
Zrywa wianki i rzuca na klęczących skronie,
I rozlewa jak z mszalnej kadzielnicy wonie.

    A gdy w kościele było po mszy i kazaniu,
Wyszedł przewodniczący całemu zebraniu
Podkomorzy, niedawno przez powiatu stany
Zgodnie konfederackim marszałkiem obrany.
Miał mundur województwa: żupan złotem szyty,
Kontusz grodeturowy z frędzlą i pas lity,
Przy którym karabela z głownią jaszczurową;
Na szyi świecił wielką szpilką brylantową;
Konfederatka biała, a na niej pęk gruby
Drogich piórek, były to białych czapel czuby
(Na fest kładzie się tylko kitka tak bogata,
Której każde pióreczko kosztuje dukata).
Tak ubrany, na wzgórek wstąpił przed kościołem,
Wieśniacy i żołnierstwo ścisnęło się kołem,
On rzekł:

                        «Bracia! ogłosił wam ksiądz na ambonie
Wolność, którą cesarz-król przywrócił Koronie,
A teraz Litewskiemu Księstwu, Polszcze całej
Przywraca; słyszeliście rządowe uchwały
I zwołujące walny sejm uniwersały.
Ja tylko mam słów parę przemówić do gminy,
W rzeczy, która się tycze Sopliców rodziny,
Tutejszych panów.

                        Cała pomni okolica,
Co tu zbroił nieboszczyk pan Jacek Soplica:
Ale kiedy o grzechach jego wszyscy wiecie,
Czas i zasługi jego ogłosić na świecie.
Obecni tu są naszych wojsk jenerałowie,
Od których usłyszałem wszystko, co wam mówię.
Ten Jacek nie był umarł (jak głoszono) w Rzymie,
Tylko odmienił życie dawne, stan i imię,
A wszystkie przeciw Bogu i Ojczyźnie winy
Zgładził przez żywot święty i przez wielkie czyny.

    On to pod Hohenlinden, gdy Ryszpans jenerał
Na pół pobity już się do odwrotu zbierał,
Nie wiedząc, że Kniaziewicz ciągnie ku odsieczy,
On to Jacek, zwan Robak, wśród grotów i mieczy
Przeniósł od Kniaziewicza listy Ryszpansowi
Donoszące, że nasi biorą tył wrogowi.
On potem w Hiszpaniji, gdy nasze ułany
Zdobyły Samosiery grzbiet oszańcowany,
Obok Kozietulskiego był ranny dwa razy!
Następnie, jak wysłaniec, z tajnymi rozkazy
Biegał po różnych stronach ducha ludzi badać,
Towarzystwa tajemne wiązać i zakładać;
Na koniec w Soplicowie, w swym ojczystym gnieździe,
Gdy gotował powstanie zginął na zajeździe.
Właśnie o jego śmierci nadeszła wiadomość
Do Warszawy w tę chwilę, gdy cesarz jegomość
Raczył mu dać za dawne czyny bohaterskie
Legiji honorowej znaki kawalerskie.

    Owoż te wszystkie rzeczy mając na uwadze,
Ja, reprezentujący województwa władzę,
Moją konfederacką ogłaszam wam laską:
Że Jacek wierną służbą i cesarską łaską
Zniósł infamiji plamę, powraca do cześci,
I znowu się w rzęd prawych patryjotów mieści.
Więc kto będzie śmiał Jacka zmarłego rodzinie
Wspomnieć kiedy o dawnej zagładzonej winie,
Ten podpadnie za karę takiego wyrzutu,
Gravis notæ maculæ, wedle słów Statutu
Karzących tak militem jak i skartabella,
Co by siał infamiją na obywatela;
A że teraz jest równość, więc artykuł trzeci
Obowiązuje równie i mieszczan, i kmieci.
Ten wyrok marszałkowski pan pisarz umieści,
W aktach jeneralności, a Woźny obwieści.

    Co się tycze legiji honorowej krzyża,
Że późno przyszedł, nic to sławie nie ubliża;
Jeśli Jackowi nie mógł służyć ku ozdobie,
Niech służy ku pamiątce: wieszam go na grobie.
Trzy dni tu będzie wisiał, potem do kaplicy
Złoży się, jako wotum dla Boga Rodzicy».

    To powiedziawszy, order wydobył z pokrowca,
I zawiesił na skromnym krzyżyku grobowca
Uwiązaną w kokardę wstążeczkę czerwoną
I krzyż biały gwiaździsty ze złotą koroną;
Przeciw słońcu promienie gwiazdy zajaśniały
Jako ostatni odbłysk ziemskiej Jacka chwały.
Tymczasem lud na klęczkach Anioł Pański mowi,
Upraszając o wieczny pokój grzesznikowi;
Sędzia obchodzi gości i wiejską gromadę,
Wszystkich do Soplicowa wzywa na biesiadę.

    Ale na przyźbie domu usiedli dwaj starce,
Mając u kolan pełne miodu dwa półgarce.
Patrzą w sad, gdzie wśród pączków barwistego maku
Stał ułan jak słonecznik, w błyszczącym kołpaku
Strojnym blachą złocistą i piórem koguta;
Przy nim dziewczę w zielonej sukience jak ruta
Pozioma, wznosi oczki błękitne jak bratki
Ku oczom chłopca; dalej panny rwały kwiatki
Po ogrodzie, umyślnie odwracając głowy
Od kochanków, żeby im nie mieszać rozmowy.

    Ale starce miód piją, tabakierką z kory
Częstując się nawzajem, toczą rozhowory.

    «Tak, tak, mój Protazeńku» rzekł Klucznik Gerwazy.
«Tak, tak, mój Gerwazeńku» rzekł Woźny Protazy.
«Tak to, tak!» powtórzyli zgodnie kilka razy,
Kiwając w takt głowami; wreszcie Woźny rzecze:
«Iż proces nasz skończy się dziwnie, ja nie przeczę.
Wszakże, były przykłady: pamiętam procesy,
W których się działy gorsze niż u nas ekscesy,
A intercyza cały zakończyła kłopot:
Tak z Borzdobohatymi pogodził się Łopot,
Krepsztulowie z Kupściami, Putrament z Pikturną,
Z Odyńcami Mackiewicz, z Kwileckimi Turno.
Co mówię! wszak Polacy miewali zamieszki
Z Litwą, gorsze niżeli z Soplicą Horeszki,
A gdy na rozum wzięła królowa Jadwiga,
To się bez sądów owa skończyła intryga.
Dobrze, gdy strony mają panny albo wdowy
Na wydaniu: to zawsze kompromis gotowy.
Najdłuższy proces zwykle bywa z duchowieństwem
Katolickim albo też z bliskim pokrewieństwem:
Bo wtenczas sprawy skończyć nie można małżeństwem.
Stąd to Lachy z Rusami w sporach nieskończonych,
Idąc z Lecha i Rusa, dwu braci rodzonych;
Stąd się tyle procesów litewskich ciągnęło
Długo z księżmi Krzyżaki, aż wygrał Jagiełło;
Stąd na koniec pendebat długo przed aktami
Sławny ów proces Rymszów z dominikanami,
Aż wygrał wreszcie syndyk klasztorny ksiądz Dymsza,
Skąd jest przysłowie: większy Pan Bóg niż pan Rymsza;
Ja zaś dołożę, lepszy miód od Scyzoryka».
To mówiąc, półgarcówką przepił do Klucznika.

    «Prawda! prawda! — rzekł na to Gerwazy wzruszony. —
Dziwneć to były losy tej naszej Korony
I naszej Litwy! Wszak to jak małżonków dwoje!
Bóg złączył, a czart dzieli; Bóg swoje, czart swoje!
Ach, bracie Protazeńku! że to oczy nasze
Widzą! że znowu do nas ci Koronijasze
Zawitali! Służyłem ja z nimi przed laty;
Pamiętam, dzielne były z nich konfederaty!
Gdyby nieboszczyk pan mój Stolnik dożył chwili!
O Jacku! Jacku!… lecz cóż będziemy kwilili?
Skoro dziś znowu Litwa łączy się z Koroną,
Toć tym samym już wszystko zgodzono, zgładzono».

    «I to dziw — rzekł Protazy — że o tej to Zosi,
O której rękę teraz nasz Tadeusz prosi,
Było przed rokiem omen, jakoby znak z nieba!»
«Panną Zofiją — przerwał Klucznik — zwać ją trzeba;
Bo już dorosła, nie jest dziewczyną maluczką,
Przy tym z krwi dygnitarskiej, jest Stolnika wnuczką».
«Owoż — kończył Protazy — był to znak proroczy
O jej losie, widziałem znak na własne oczy.
Przed rokiem tu siedziała w święto czeladź nasza
Pijąc miód; alić patrzym: pęc, pada z poddasza
Dwóch wróblów bijących się; oba samcy stare,
Jeden młodszy cokolwiek miał podgarle szare,
Drugi czarne; dalejże tłuc się po podwórzu,
Przewracać kulki, że aż zaryli się w kurzu —
My patrzym, a tymczasem szepcą sobie sługi,
Że ten czarny niech będzie Horeszko, a drugi
Soplica; więc ilekroć szary był na górze
Krzyczą: »Wiwat Soplica, pfe Horeszki tchórze!«
A gdy spadał, wołali: »Popraw się Soplica,
Nie daj się magnatowi, to wstyd na szlachcica!«
Tak śmiejąc się, czekamy, kto kogo pokona;
Wtem Zosieńka, nad ptastwem litością wzruszona,
Podbiegła i nakryła rączką te rycerze;
Jeszcze się w ręku bili, aż leciało pierze,
Taka była zawziętość w tym maleńkim lichu.
Baby patrząc na Zosię, gadały po cichu,
Że pewnie przeznaczeniem będzie tej dziewczyny
Pogodzić dwie od dawna zwaśnione rodziny.
A widzę, że się dzisiaj ziścił omen babi.
Prawdać to, że naonczas myślano o Hrabi,
Nie zaś o Tadeuszu».

                        Na to Klucznik rzecze:
«Dziwne są sprawy w świecie, kto wszystko dociecze!
Ja też powiem waszeci rzecz choć nie tak cudną
Jak ów omen, a przecież do pojęcia trudną.
Wiesz, iż dawniej rad bym był Sopliców rodzinę
W łyżce wody utopić; a tego chłopczynę,
Tadeusza, od dziecka niezmierniem polubił!
Uważałem, że gdy się z chłopiętami czubił,
Zawsze ich zbił; więc ilekroć do zamku biegał,
Jam go zawsze do trudnych imprezów podżegał.
Wszystko mu się udało: czy wydrzeć gołębie
Na wieży, czy jemiołę oberwać na dębie,
Czyli z najwyższej sosny złupić wronie gniazdo:
Wszystko umiał; myśliłem: pod szczęśliwą gwiazdą
Urodził się ten chłopiec, szkoda że Soplica!
Któż by zgadł, że w nim zamku powitam dziedzica,
Męża panny Zofiji, mej wielmożnej pani!»

    Tu skończyli rozmowę, piją zadumani;
Słychać tylko niekiedy te krótkie wyrazy:
«Tak, tak, panie Gerwazy» — «Tak, panie Protazy».

    Przyzba tykała kuchni, której okna stały
Otworem i dym jako z pożaru buchały;
Aż z kłębów dymu, niby biała gołębica,
Mignęła świecąca się kuchmistrza szlafmyca:
Wojski przez okno kuchni, ponad starców głowy,
Wytknąwszy głowę, milczkiem słuchał ich rozmowy,
I podał im nareszcie filiżanki spodek
Pełen biszkoktów, mówiąc: «Zakąście wasz miodek.
A ja wam też opowiem historią ciekawą
Sporu, który miał bitwą zakończyć się krwawą,
Gdy polujący w głębi nalibockich lasów,
Rejtan wypłatał sztukę książęciu Denassów.
Tej sztuki omal własnym nie przypłacił zdrowiem:
Jam kłótnię panów zgodził, jak — to wam opowiem».
Ale Wojskiego powieść przerwali kucharze,
Pytając komu serwis ustawiać rozkaże.

    Wojski odszedł, a starcy zaczerpnąwszy miodu,
Zadumani zwrócili oczy w głąb ogrodu,
Gdzie ów dorodny ułan rozmawiał z panienką.
Właśnie ułan ująwszy jej dłoń lewą ręką,
(Prawą miał na temlaku, widać, że był ranny)
Z takimi odezwał się słowami do panny:

    «Zofijo, musisz to mnie koniecznie powiedzieć,
Nim zamienim pierścionki, muszę o tym wiedzieć.
I cóż, że przeszłej zimy byłaś już gotowa
Dać słowo mnie? Ja wtenczas nie przyjąłem słowa:
Bo i cóż mnie po takim wymuszonym słowie?
Wtenczas bawiłem bardzo krótko w Soplicowie;
Nie byłem taki próżny, ażebym się łudził,
Żem jednym mym spojrzeniem miłość w tobie wzbudził;
Ja nie fanfaron, chciałem mą własną zasługą
Zyskać twe względy, choćby przyszło czekać długo.
Teraz jesteś łaskawa twe słowo powtórzyć:
Czymże na tyle łaski umiałem zasłużyć?
Może mnie bierzesz, Zosiu, nie tak z przywiązania,
Tylko że stryj i ciotka do tego cię skłania?
Ale małżeństwo, Zosiu, jest rzecz wielkiej wagi!
Radź się serca własnego; niczyjej powagi
Tu nie słuchaj, ni stryja gróźb, ni namów cioci.
Jeśli nie czujesz dla mnie nic oprócz dobroci,
Możem te zaręczyny czas jakiś odwlekać;
Więzić twej woli nie chcę; będziem, Zosiu, czekać.
Nic nas nie nagli, zwłaszcza że wczora wieczorem
Dano mi rozkaz zostać w Litwie instruktorem
W pułku tutejszym, nim się z mych ran nie wyleczę.
I cóż kochana Zosiu?»

                        Na to Zosia rzecze,
Wznosząc głowę i patrząc w oczy mu nieśmiało:
«Nie pamiętam już dobrze, co się dawniej działo;
Wiem, że wszyscy mówili, iż za mąż iść trzeba
Za pana: ja się zawsze zgadzam z wolą Nieba
I z wolą starszych». Potem, spuściwszy oczęta,
Dodała: «Przed odjazdem, jeśli pan pamięta,
Kiedy umarł ksiądz Robak w ową burzę nocną,
Widziałam, że pan jadąc żałował nas mocno;
Pan łzy miał w oczach; te łzy, powiem panu szczerze,
Wpadły mnie aż do serca; odtąd panu wierzę
Że mnie lubisz; ilekroć mówiłam pacierze
Za pana powodzenie, zawsze przed oczami
Stał pan z tymi dużymi błyszczacymi łzami.
Potem Podkomorzyna do Wilna jeździła,
Wzięła mnie tam na zimę; alem ja tęskniła
Do Soplicowa i do tego pokoiku,
Gdzie mnie pan naprzód w wieczór spotkał przy stoliku,
Potem pożegnał… Nie wiem, skąd pamiątka pana,
Coś niby jak rozsada w jesieni zasiana,
Przez całą zimę w moim sercu się krzewiła,
Że, jako mówię panu, ustawniem tęskniła
Do tego pokoiku, i coś mi szeptało,
Że tam znów pana znajdę — i tak się też stało.
Mając to w głowie, często też miałam na ustach
Imię pana — było to w Wilnie na zapustach;
Panny mówiły, że ja jestem zakochana:
Jużci, jeżeli kocham, to już chyba pana».
Tadeusz rad z takiego miłości dowodu,
Wziął ją pod rękę, ścisnął i wyszli z ogrodu
Do pokoju damskiego, do owej komnaty,
Kędy Tadeusz mieszkał przed dziesięcią laty.

    Teraz bawił tam Rejent cudnie wystrojony,
I usługiwał damie, swojej narzeczonéj,
Biegając i podając sygnety, łańcuszki,
Słoiki i flaszeczki, i proszki, i muszki;
Wesoł, na pannę młodą patrzył tryumfalnie.
Panna młoda kończyła robić gotowalnię:
Siedziała przed zwierciadłem radząc się bóstw wdzięku;
Pokojowe zaś, jedne z żelazkami w ręku
Odświeżają nadstygłe warkoczów pierścionki,
Drugie klęcząc pracują około falbonki.

    Gdy się tak Rejent bawi ze swą narzeczoną,
Kuchcik stuknął doń w okno: kota spostrzeżono!
Kot, wykradłszy się z łozy, prześmignął po łące
I wskoczył w sad pomiędzy jarzyny wschodzące;
Tam siedzi: wystraszyć go łacno z rozsadniku
I uszczuć, postawiwszy charty na przesmyku.
Bieży Asesor, ciągnąc za obróż Sokoła;
Pośpiesza za nim Rejent i Kusego woła.
Wojski obu z chartami przy płocie ustawił,
A sam się z placką muszą do sadu wyprawił.
Depcąc, świszcząc i klaszcząc, bardzo zwierza trwoży;
Szczwacze, trzymając każdy charta na obroży,
Ukazują palcami, skąd zając wyruszy,
Cmokają z cicha; charty nadstawiły uszy,
Wytknęły pyski na wiatr i drżą niecierpliwie,
Jak dwie strzały złożone na jednej cięciwie.
Wtem Wojski krzyknął: «Wyczha!» Zając smyk zza płotu
Na łąkę; charty za nim; i wnet bez obrotu
Sokół i Kusy razem spadli na szaraka
Ze dwóch stron w jednej chwili, jak dwa skrzydła ptaka,
I zęby mu jak szpony zatopili w grzbiecie.
Kot jęknął raz, jak nowo narodzone dziecię,
Żałośnie! Biegą szczwacze: już leży bez ducha,
A charty mu sierść białą targają spod brzucha.

    Szczwacze pogłaskali psy, a Wojski tymczasem
Dobył nożyk strzelecki wiszący za pasem,
Oderznął skoki i rzekł: «Dziś równą odprawę
Wezmą pieski, bo równą pozyskali sławę,
Równa ich była rączość, równa była praca;
Godzien jest pałac Paca, godzien Pac pałaca,
Godni są szczwacze chartów, godne szczwaczów charty.
Otóż skończony spór wasz długi i zażarty;
Ja, któregoście sędzią zakładu obrali,
Wydaję wreszcie wyrok: obaście wygrali.
Wracam fanty, niech każdy przy swoim zostanie,
A wy podpiszcie zgodę». Na starca wezwanie
Szczwacze zwrócili na się rozjaśnione lice
I długo rozdzielone złączyli prawice.

    Wtem rzekł Rejent: «Stawiłem niegdyś konia z rzędem,
Opisałem się także przed ziemskim urzędem,
Iż pierścień mój sędziemu w salarijum złożę:
Fant postawiony w zakład wracać się nie może.
Pierścień niechaj pan Wojski na pamiątkę przymie,
I każe na nim wyryć albo swoje imię,
Lub gdy zechce, herbowne Hreczechów ozdoby;
Krwawnik jest gładki, złoto jedenastej proby.
Konia teraz ułani pod jazdę zabrali,
Rzęd został przy mnie; każdy znawca ten rzęd chwali
Iż jest wygodny, trwały, a piękny jak cacko:
Kulbaczka wąska modą z turecka kozacką,
Kula na przodzie, w kuli są drogie kamienie,
Poduszeczka z rubrontu wyścieła siedzenie;
A kiedy na łęk wskoczysz, na tym miękkim puszku
Między kulami siedzisz wygodnie jak w łóżku;
A gdy w galop puścisz się (tu Rejent Bolesta,
Który, jako wiadomo, bardzo lubił gesta,
Rozstawił nogi jakby na konia wskakiwał,
Potem galop udając, powoli się kiwał)
A gdy w galop puścisz się, natenczas z czapraka
Blask bije, jakby złoto kapało z rumaka,
Bo tabenki są gęsto złotem nakrapiane,
I szerokie strzemiona srebrne pozłacane;
Na rzemieniach munsztuka i na uździenicy
Połyskają guziki perłowej macicy,
U napierśnika wisi księżyc w kształt Leliwy,
To jest w kształt nowiu. Cały ten sprzęt osobliwy,
Zdobyty (jak wieść niesie) w boju podhajeckim
Na jakimś bardzo znacznym szlachcicu tureckim,
Przyjm, Asesorze, w dowód mojego szacunku».

    A na to rzekł Asesor, wesół z podarunku:
«Ja niegdyś darowane od księcia Sanguszki
Stawiłem w zakład moje prześliczne obróżki
Jaszczurem wykładane z kolcami ze złota,
I utkaną z jedwabiu smycz, której robota
Równie droga jak kamień co się na niej świeci.
Chciałem sprzęt ten zostawić w dziedzictwie dla dzieci;
Dzieci pewnie mieć będę: wiesz, że się dziś żenię;
Ale ten sprzęt, Rejencie, proszę uniżenie,
Bądź łaskaw przyjąć w zamian za twój rzęd bogaty
I na pamiątkę sporu, co długimi laty
Toczył się i nareszcie zakończył zaszczytnie
Dla nas obu. Niech zgoda między nami kwitnie».
Więc wracali do domu oznajmić za stołem,
Że się skończył spór między Kusym i Sokołem.

    Była wieść, że zająca tego Wojski w domu
Wyhodował i w ogród puścił po kryjomu,
Ażeby szczwaczów zgodzić zbyt łatwą zdobyczą.
Staruszek tak swą sztukę zrobił tajemniczo,
Że oszukał zupełnie całe Soplicowo.
Kuchcik w lat kilka później szepnął o tym słowo,
Chcąc Assesora skłócić z Rejentem na nowo;
Ale próżno krzywdzące chartów wieści szerzył:
Wojski zaprzeczył i nikt kuchcie nie uwierzył.

    Już goście zgromadzeni w wielkiej zamku sali,
Czekając uczty, wkoło stołu rozmawiali,
Gdy pan Sędzia w mundurze wojewódzkim wchodzi
I pana Tadeusza z Zofią przywodzi.
Tadeusz lewą dłonią dotykając głowy,
Pozdrowił swych dowódców przez ukłon wojskowy;
Zofija z opuszczonym ku ziemi wejrzeniem,
Zapłoniwszy się, gości witała dygnieniem
(Od Telimeny pięknie dygać wyuczona).
Miała wianek na głowie jako narzeczona,
Zresztą ubiór ten samy, w jakim dziś w kaplicy
Składała snop wiosenny dla Boga Rodzicy.
Użęła znów dla gości nowy snopek ziela;
Jedną ręką zeń kwiaty i trawy rozdziela,
Drugą swój sierp błyszczący poprawia na głowie.
Brali ziółka, całując jej ręce, wodzowie;
Zosia znowu dygała w kolej zapłoniona.

    Wtem jenerał Kniaziewicz wziął ją za ramiona,
I złożywszy ojcowski całus na jej czole,
Podniósł w górę dziewczynę, postawił na stole,
A wszyscy klaszcząc w dłonie zawołali: «Brawo!»
Zachwyceni dziewczyny urodą, postawą,
A szczególniej jej strojem litewskim, prostaczym.
Bo dla tych wodzów, którzy w swym życiu tułaczym
Tak długo błąkali się w obcych stronach świata,
Dziwne miała powaby narodowa szata,
Która im wspominała i młode ich lata,
I dawne ich miłostki. Więc ze łzami prawie
Skupili się do stołu, patrzyli ciekawie.
Ci proszą, aby Zosia wzniosła nieco czoło
I oczy pokazała; ci, ażeby wkoło
Raczyła się obrócić; dziewczyna wstydliwa
Obraca się, lecz oczy rękami zakrywa.
Tadeusz patrzył wesół i zacierał ręce.

    Czy ktoś Zosi poradził wyjść w takiej sukience,
Czy instynktem wiedziała (bo dziewczyna zgadnie
Zawsze instynktem, co jej do twarzy przypadnie):
Dosyć, że Zosia pierwszy raz w życiu dziś z rana
Była od Telimeny za upór łajana,
Nie chcąc modnego stroju, aż wymogła płaczem
Że ją tak zostawiono, w ubraniu prostaczem.

    Spódniczkę miała długą, białą; suknię krótką
Z zielonego kamlotu z różową obwódką;
Gorset także zielony, różowymi wstęgi
Od łona aż do szyi sznurowany w pręgi;
Pod nim pierś jako pączek pod listkiem się tuli.
Od ramion świecą białe rękawy koszuli,
Jako skrzydła motyle do lotu wydęte,
U dłoni skarbowane i wstążką opięte.
Szyja także koszulką obciśniona wąską,
Kołnierzyk zadzierzgniony różową zawiązką;
Zauszniczki wyrżnięte sztucznie z pestek wiszni,
Których się wyrobieniem Sak Dobrzyński pyszni
(Były tam dwa serduszka z grotem i płomykiem
Dane dla Zosi, gdy Sak był jej zalotnikiem);
Na kołnierzyku wiszą dwa sznurki bursztynu,
Na skroniach zielonego wianek rozmarynu;
Wstążki warkoczów Zosia rzuciła na barki,
A na czoło włożyła, zwyczajem żniwiarki,
Sierp krzywy, świeżym żęciem traw oszlifowany,
Jasny jak nów miesięczny nad czołem Dyjany.

    Wszyscy chwalą, klaskają. Jeden z oficerów
Dobył z kieszeni portefeuille z plikami papierów,
Rozłożył je, ołówek przyciął, w ustach zmoczył,
Patrzy w Zosię, rysuje. Ledwie Sędzia zoczył
Papiery i ołówki, poznał rysownika;
Choć go bardzo odmienił mundur pułkownika,
Bogate szlify, mina prawdziwie ułańska
I wąsik poczerniony i bródka hiszpańska.
Sędzia poznał: «Jak się masz, mój jaśnie wielmożny
Hrabio, i w ładownicy masz twój sprzęt podróżny
Do malarstwa!» W istocie, był to Hrabia młody;
Niedawny żołnierz: lecz że wielkie miał dochody
I swoim kosztem cały pułk jazdy wystawił,
I w pierwszej zaraz bitwie wybornie się sprawił,
Cesarz go pułkownikiem dziś właśnie mianował;
Więc Sędzia witał Hrabię i rangi winszował,
Ale Hrabia nie słuchał, a pilnie rysował.

    Tymczasem weszła druga para narzeczona:
Asesor, niegdyś cara, dziś Napoleona
Wierny sługa; żandarmów oddział miał w komendzie,
A choć ledwie dwadzieścia godzin był w urzędzie,
Już włożył mundur siny z polskimi wyłogi
I ciągnął krzywą szablę i dzwonił w ostrogi.
Obok poważnym krokiem szła jego kochanka
Ubrana bardzo strojnie, Tekla Hreczeszanka;
Bo Asesor już dawno Telimenę rzucił,
I aby tę kokietkę tym mocniej zasmucił,
Ku Wojszczance afekty serdeczne obrócił.
Panna nie nadto młoda, już pono półwieczna,
Lecz gospodyni dobra, osoba stateczna
I posażna: bo oprócz swej dziedzicznej wioski
Sumką z daru Sędziego powiększała wnioski.

    Trzeciej pary daremnie czekają czas długi.
Sędzia niecierpliwi się i wysyła sługi;
Wracają: powiadają, że trzeci małżonek,
Pan Rejent, szczując kota, zgubił swój pierścionek
Ślubny, szuka na łące; a Rejenta dama
Jeszcze u gotowalni, choć spieszy się sama
I choć jej pomagają służebne kobiety,
Nie mogła w żaden sposób skończyć toalety:
Ledwie będzie gotowa na godzinę czwartą.




Księga dwunasta



Kochajmy się

Ostatnia uczta staropolska — Arcy-serwis — Objaśnienie jego figur — Jego ruchy — Dąbrowski udarowany — Jeszcze o Scyzoryku — Kniaziewicz udarowany — Pierwszy akt urzędowy Tadeusza przy objęciu dziedzictwa — Uwagi Gerwazego — Koncert nad koncertami — Polonez — Kochajmy się.

    Na koniec z trzaskiem sali drzwi na wściąż otwarto.
Wchodzi pan Wojski w czapce i z głową zadartą,
Nie wita się i miejsca za stołem nie bierze:
Bo Wojski występuje w nowym charakterze
Marszałka dworu. Laskę ma na znak urzędu
I tą laską z kolei jako mistrz obrzędu,
Wskazuje wszystkim miejsca i gości usadza.
Naprzód, jako najpierwsza województwa władza,
Podkomorzy-Marszałek wziął miejsce zaszczytne:
Ze słoniowym poręczem krzesło aksamitne;
Obok na prawej stronie jenerał Dąbrowski,
Na lewej siadł Kniaziewicz, Pac i Małachowski;
Śród nich Podkomorzyna, dalej inne panie,
Oficerowie, pany, szlachta i ziemianie,
Mężczyźni i kobiety, na przemian po parze,
Usiadają porządkiem, gdzie Wojski ukaże.

    Pan Sędzia, skłoniwszy się, opuścił biesiadę.
On na dziedzińcu włościan traktował gromadę;
Zebrawszy ich za stołem na dwa staje długim,
Sam siadł na jednym końcu, a pleban na drugim.
Tadeusz i Zofia do stołu nie siedli;
Zajęci częstowaniem włościan, chodząc jedli.
Starożytny był zwyczaj, iż dziedzice nowi
Na pierwszej uczcie sami służyli ludowi.

    Tymczasem goście, potraw czekający w sali,
Z zadziwieniem na wielki serwis poglądali,
Którego równie drogi kruszec jak robota.
Jest podanie, że książę Radziwiłł-Sierota
Kazał ten sprzęt na urząd w Wenecyi zrobić
I wedle własnych planów po polsku ozdobić.
Serwis potem zabrany czasu wojny szwedzkiéj
Przeszedł, nie wiedzieć jaką drogą, w dom szlachecki;
Dziś ze skarbca dobyty zajął środek stoła
Ogromnym kręgiem, na kształt karetnego koła.

    Serwis ten był nalany ode dna po brzegi
Piankami i cukrami białymi jak śniegi:
Udawał przewybornie krajobraz zimowy.
W środku czerniał ogromny bór konfiturowy,
Stronami domy, niby wioski i zaścianki,
Okryte zamiast śronu cukrowymi pianki;
Na krawędziach naczynia stoją dla ozdoby
Niewielkie z porcelany wydęte osoby
W polskich strojach: jakoby aktory na scenie,
Zdawały się przedstawiać jakoweś zdarzenie;
Gest ich sztucznie wydany, farby osobliwe,
Tylko głosu im braknie, zresztą gdyby żywe.

    Cóż przedstawiają? goście pytali ciekawi.
Za czym Wojski podnosi laskę i tak prawi:
(Tymczasem podawano wódkę przed jedzeniem)
«Za mych wielce mościwych panów pozwoleniem:
Te persony, których tu widzicie bez liku,
Przedstawiają polskiego historię sejmiku,
Narady, wotowanie, tryumfy i waśnie;
Sam tę scenę odgadłem i państwu objaśnię.

    Oto na prawo widać liczne szlachty grono:
Pewnie ich przed sejmikiem na ucztę sproszono.
Czeka nakryty stolik; nikt gości nie sadza,
Stoją kupkami, każda kupka się naradza.
Patrzcie, iż w każdej kupce stoi w środku człowiek,
Z którego ust otwartych, z podniesionych powiek,
Rąk niespokojnych, widać: mówca — coś tłumaczy,
I palcem eksplikuje, i na dłoni znaczy.
Ci mówcy zalecają swoich kandydatów;
Z różnym skutkiem, jak widać z miny szlachty bratów.

    «Wprawdzie tam, w drugiej kupie, szlachta pilnie słucha.
Ten ręce za pas zatknął i przyłożył ucha,
Ów dłoń przy uchu trzyma i milczkiem wąs kręci,
Zapewne słowa zbiera i niże w pamięci;
Cieszy się mówca widząc, że są nawróceni,
Gładzi kieszeń, bo kreski ich już ma w kieszeni.

    Lecz za to w trzecim gronie dzieje się inaczej:
Tu mówca musi łowić za pasy słuchaczy.
Patrzcie, wyrywają się i cofają uszy;
Patrzcie, jako ten słuchacz od gniewu się puszy,
Wzniósł ręce, grozi mówcy, usta mu zatyka,
Pewnie słyszał pochwały swego przeciwnika;
Ten drugi, pochyliwszy czoło na kształt byka,
Powiedziałbyś, że mówcę pochwyci na rogi;
Ci biorą się do szabel, tamci poszli w nogi.

    Jeden między kupkami szlachcic cichy stoi.
Widać, że człek bezstronny; waha się i boi;
Za kim dać kreskę? nie wie, i sam z sobą w walce,
Pyta losu, wzniósł ręce, wytknął wielkie palce,
Zmrużył oczy, paznokciem do paznokcia mierzy:
Widać, że kreskę swoją kabale powierzy;
Jeśli palce trafią się, da afirmatywę,
A jeżeli się chybią, rzuci negatywę.

    Na lewej druga scena; refektarz klasztoru
Obrócony na salę szlacheckiego zboru.
Starsi rzędem na ławach siedzą, młodzi stają
I ciekawi przez głowy w środek zaglądają;
W środku marszałek stoi, wazon w ręku trzyma,
Liczy gałki, szlachta je pożera oczyma,
Właśnie wstrząsnął ostatnią; woźni ręce wznoszą
I imię obranego urzędnika głoszą.

    Jeden szlachcic na zgodę powszechną nie zważa.
Patrz, wytknął głowę oknem z kuchni refektarza;
Patrz, jak oczy wytrzeszczył, jak pogląda śmiało,
Usta otworzył, jakby chciał zjeść izbę całą;
Łatwo zgadnąć, że szlachcic ten zawołał: »Veto!«
Patrzcie, jak za tą nagłą do kłótni podnietą,
Tłoczy się do drzwi ciżba, pewnie idą w kuchnię;
Dostali szable, pewnie krwawy bój wybuchnie.

    Lecz tam na korytarzu, Państwo uważacie
Tego starego księdza, co idzie w ornacie:
To przeor; Sanktissimum z ołtarza wynosi,
A chłopiec w komży dzwoni i na ustęp prosi.
Szlachta wnet szable chowa, żegna się i klęka,
A ksiądz tam się obraca, gdzie jeszcze broń szczęka.
Skoro przyjdzie, wnet wszystkich uciszy i zgodzi.

    «Ach! wy nie pamiętacie tego Państwo młodzi!
Jak wśród naszej burzliwej szlachty samowładnej,
Zbrojnej, nie trzeba było policyi żadnej:
Dopóki wiara kwitła, szanowano prawa,
Była wolność z porządkiem i z dostatkiem sława!
W innych krajach, jak słyszę, trzyma urząd drabów,
Policyjantów różnych, żandarmów, konstabów:
Ale jeśli miecz tylko bezpieczeństwa strzeże,
Żeby w tych krajach była wolność — nie uwierzę».

    Wtem dzwoniąc w tabakierę, rzekł pan Podkomorzy:
«Panie Wojski, niech wasze na potem odłoży
Te historie. Prawda, że sejmik ciekawy:
Ale my głodni, każ wać przynosić potrawy».

    Na to Wojski, skłaniając aż do ziemi laskę:
«Jaśnie wielmożny panie, zróbże mi tę łaskę,
Zaraz dokończę scenę ostatnią sejmików.
Oto nowy marszałek na ręku stronników
Wyniesion z refektarza. Patrz, jak szlachta braty
Rzucają czapki, usta otwarli, — wiwaty!
A tam, po drugiej stronie pan przekreskowany
Sam jeden, czapkę wcisnął na łeb zadumany.
Żona przed domem czeka, zgadła, co się dzieje,
Biedna! oto na ręku pokojowej mdleje;
Biedna! jaśnie wielmożnej tytuł przybrać miała,
A znów tylko wielmożną na lat trzy została!»

    Tu Wojski skończył opis i laską znak daje.
I wnet zaczęli wchodzić parami lokaje
Roznoszący potrawy: barszcz królewskim zwany,
I rosół staropolski sztucznie gotowany,
Do którego pan Wojski z dziwnymi sekrety
Wrzucił kilka perełek i sztukę monety
(Taki rosół krew czyści i pokrzepia zdrowie);
Dalej inne potrawy, a któż je wypowie!
Kto zrozumie nieznane już za naszych czasów,
Te półmiski kontuzów, arkasów, blemasów,
Z ingrediencyjami pomuchl, figatelów,
Cybetów, piżm, dragantów, pinelów, brunelów;
Owe ryby: łososie suche, dunajeckie,
Wyżyny i kawijary weneckie, tureckie,
Szczuki główne i szczuki podgłówne, łokietne,
Flądry i karpie ćwiki, i karpie szlachetne;
W końcu sekret kucharski: ryba niekrojona
U głowy przysmażona, we środku pieczona,
A mająca potrawkę z sosem u ogona.

    Goście ani pytali nazwiska potrawy,
Ani ich zastanowił ów sekret ciekawy;
Wszystko prędko z żołnierskim jedli apetytem,
Kieliszki napełniając węgrzynem obfitym.

    Ale tymczasem wielki serwis barwę zmienił,
I odarty ze śniegu już się zazielenił.
Bo lekka, ciepłem letnim powoli rozgrzana,
Roztopiła się lodu cukrowego piana
I dno odkryła, dotąd zatajone oku;
Więc krajobraz przedstawił nową porę roku,
Zabłysnąwszy zieloną, różnofarbną wiosną.
Wychodzą różne zboża, jak na drożdżach rosną,
Pszenicy szafranowej buja kłos złocisty,
Żyto ubrane w srebra malarskiego listy
I gryka wyrabiana sztucznie z czokolady,
I kwitnące gruszkami i jabłkami sady.

    Ledwie mają czas goście darów lata użyć;
Darmo proszą Wojskiego, żeby je przedłużyć:
Już serwis, jak planeta koniecznym obrotem,
Zmienia porę, już zboża malowane złotem,
Nabrawszy ciepła w izbie powoli topnieją,
Już trawy pożółkniały, liścia czerwienieją,
Sypią się: rzekłbyś, iż wiatr jesienny powiewa;
Na koniec owe chwilą przedtem strojne drzewa,
Teraz, jakby odarte od wichrów i szronu,
Stoją nagie: były to laski cynamonu,
Lub udające sosnę gałązki wawrzynu,
Odziane zamiast kolców ziarenkami kminu.

    Goście pijący wino zaczęli gałązki
Pnie i korzenie zrywać i gryźć dla zakąski.
Wojski obchodził serwis i pełen radości,
Tryumfujące oczy obracał na gości.

    Henryk Dąbrowski udał wielkie zadziwienie
I rzekł: «Mój panie Wojski, czy to chińskie cienie?
Czy to Pinety panu dał w służbę swe bisy?
Czy dotąd u was w Litwie są takie serwisy
I wszyscy takim starym ucztują zwyczajem?
Powiedz mi, bo ja życie strawiłem za krajem».

    Wojski rzekł kłaniając się: «Nie, jaśnie wielmożny
Jenerale, nie jest to żaden kunszt bezbożny!
Jest to pamiątka tylko owych biesiad sławnych,
Które dawano w domach panów starodawnych,
Gdy Polska używała szczęścia i potęgi!
Com zrobił, tom wyczytał z tej tu oto księgi.
Pytasz, czy wszędzie w Litwie ten się zwyczaj chowa?
Niestety! już i do nas włazi moda nowa.
Niejeden panicz krzyczy, że nie cierpi zbytków:
Je jak Żyd, skąpi gościom potraw i napitków,
Węgrzyna pożałuje, a pije szatańskie
Fałszywe wino modne, moskiewskie, szampańskie;
Potem w wieczór na karty tyle złota straci,
Że za nie dałbyś ucztę na stu szlachty braci.
Nawet (bo co na sercu mam, dziś powiem szczerze,
Niech tego Podkomorzy za złe mi nie bierze)
Kiedym ten serwis cudny ze skarbca dobywał,
To nawet Podkomorzy, i on mnie przedrwiwał!
Mówiąc, że to machina żmudna, staroświecka,
Że to ma pozór niby zabawki dla dziecka,
Nieprzyzwoitej dla tak znakomitych ludzi!
Sędzio! i Sędzia mówił że to gości znudzi!
A przecież, ile wnoszę z panów zadziwienia,
Widzę, iż ten kunszt piękny godzien był widzenia!
Nie wiem, czy się podobna okazja zdarzy
Częstować w Soplicowie takich dygnitarzy.
Widzę, że pan jenerał na biesiadach zna się,
Niechaj przyjmie tę książkę! Ona panu zda się,
Gdy będziesz dla monarchów zagranicznych grona
Dawał ucztę, ba, nawet dla Napoleona.
Ale pozwól, nim księgę tę panu poświęcę,
Niech powiem, jakim trafem wpadła w moje ręce».

    Wtem szmer powstał za drzwiami; razem głosów wiele
Zawołało: «Niech żyje Kurek na kościele!»
Ciżba tłoczy się w salę, a Maciej na czele.
Sędzia gościa za rękę do stołu prowadził
I wysoko pomiędzy wodzami posadził,
Mówiąc: «Panie Macieju, niedobry sąsiedzie,
Przyjeżdżasz bardzo późno, prawie po obiedzie».
«Jem wcześnie — rzekł Dobrzyński — ja tu nie dla jadła
Przybyłem, tylko że mnie ciekawość napadła,
Obejrzeć z bliska naszą armią narodową.
Wieleby gadać — jest to ani to, ni owo!
Szlachta mnie obaczyła i gwałtem tu wiedzie,
A Waszeć za stół sadzasz — dziękuję, sąsiedzie».
To wyrzekłszy, przewrócił talerz dnem do góry,
Na znak że jeść nie będzie, i milczał ponury.

    «Panie Dobrzyński — rzekł mu jenerał Dąbrowski,
Tyż to jesteś ów sławny rębacz Kościuszkowski,
Ów Maciej, zwany Rózga! znam ciebie ze sławy.
I proszę, takiś dotąd czerstwy, taki żwawy!
Ileż to lat minęło! Patrz, jam się podstarzał;
Patrz, i Kniaziewiczowi już się włos poszarzał:
A ty jeszcze z młodymi mógłbyś pójść w zapasy,
I Rózga twoja kwitnie pono jak przed czasy;
Słyszałem, żeś niedawno Moskalów oćwiczył.
Lecz gdzie są bracia twoi? Niezmiernie bym życzył
Widzieć te Scyzoryki i te wasze Brzytwy,
Ostatnie egzemplarze starodawnej Litwy».

    «Jenerale — rzekł Sędzia — po owym zwycięstwie,
Prawie wszyscy Dobrzyńscy schronili się w Księstwie;
Zapewne do którego weszli legionu».
«W istocie — odpowiedział młody Szef szwadronu —
Mam w drugiej kompaniji wąsate straszydło,
Wachmistrza Dobrzyńskiego, co się zwie Kropidło,
A Mazury zowią go litewskim niedźwiedziem.
Jeśli Jenerał każe, to go tu przywiedziem».
«Jest — rzekł porucznik — kilku innych rodem z Litwy,
Jeden żołnierz znajomy pod imieniem Brzytwy
I drugi co z tromblonem jeździ na flankiery;
Są także w pułku strzelców dwa grenadyjery
Dobrzyńscy».

                        «Ale, ale: o ich naczelniku —
Rzekł jenerał — chcę wiedzieć o tym Scyzoryku,
O którym mnie pan Wojski tyle prawił cudów,
Jakby o jednym z owych dawnych wielkoludów».
«Scyzoryk — rzecze Wojski — choć nie egzulował,
Ale bojąc się śledztwa, przed Moskwą się schował,
Całą zimę nieborak tułał się po lasach,
Teraz dopiero wyszedł. W tych wojennych czasach
Mógłby się na co przydać, jest rycerskim człekiem,
Szkoda tylko, że trochę przyciśniony wiekiem.
Lecz owóż on!…» Tu Wojski palcem wskazał w sieni,
Gdzie czeladź i wieśniacy stali natłoczeni,
A nad wszystkich głowami łysina błyszcząca
Ukazała się nagle jak pełnia miesiąca;
Trzykroć weszła i trzykroć znikła w głów obłoku.
Klucznik idąc kłaniał się, aż dobył się z tłoku,
I rzekł:

                        «Jaśnie wielmożny koronny hetmanie,
Czy jenerale, mniejsza o tytułowanie,
Jam jest Rębajło, staję na twe zawołanie
Z tym moim Scyzorykiem, który nie z oprawy
Ani z napisów, ale z hartu nabył sławy,
Że nawet o nim jaśnie wielmożny pan wiedział.
Gdyby on gadać umiał, może by powiedział
Cokolwiek na pochwałę i tej starej ręki,
Która służyła długo, wiernie, Bogu dzięki,
Ojczyźnie, tudzież panów Horeszków rodzinie,
Czego pamięć dotychczas między ludźmi słynie.
Mopanku! rzadko który pisarz prowentowy
Tak zręcznie temperuje pióra, jak on głowy.
Długo liczyć! A nosów i uszu bez liku!
A nie ma żadnej szczerby na tym Scyzoryku
I żaden go nie splamił zbojecki uczynek:
Tylko otwarta wojna albo pojedynek.
Raz tylko! Panie daj mu wieczny odpoczynek!
Bezbronnego człowieka, niestety, sprzątniono…
A i to, Bóg mi świadkiem, pro publico bono».

    «Pokaż no — rzekł śmiejąc się jenerał Dąbrowski —
A to piękny scyzoryk, istny miecz katowski!»
I z zadziwieniem wielki rapier opatrywał
I innym oficerom w kolej pokazywał.
Próbowali go wszyscy, ale ledwie który
Z oficerów mógł podnieść ten rapier do góry.
Mówiono, że Dembiński, sławny ręki siłą,
Podźwignąłby szablicę, lecz go tam nie było.
Z obecnych zaś tylko szef szwadronu Dwernicki
I dowódca plutonu, porucznik Różycki
Potrafili obracać tym żelaznym drągiem:
I tak rapier na próbę szedł z rak do rąk ciągiem.

    Lecz jenerał Kniaziewicz, wzrostem najsłuszniejszy
Pokazało się, iż był w ręku najsilniejszy:
Ująwszy rapier lekko, jakby szpadę dźwignął
I nad głowami gości błyskawicą mignął,
Przypominając polskie fechtarskie wykręty:
*Krzyżową sztukę, młyńca, cios krzywy, raz cięty,*
*Cios kradziony* i tempy *kontrpunktów, tercetów,*
Które też umiał, bo był ze szkoły kadetów.

    Gdy śmiejąc się fechtował, Rębajło już klęczał,
Objął go za kolana i ze łzami jęczał;
Za każdym zwrotem miecza: «Pięknie! jenerale,
Czyś był konfederatem? pięknie, doskonale!
To sztych Puławskich! tak się Dzierżanowski składał.
To sztych Sawy! Któż panu tak rękę układał?
Chyba Maciej Dobrzyński! A to? Jenerale,
Mój wynalazek, dalbóg mój; ja się nie chwalę:
To cięcie znane tylko w Rębajłów zaścianku,
Od mojego imienia zwane *cios mopanku*;
Któż to pana nauczył? to jest moje cięcie,
Moje!» Wstał, jenerała porwawszy w objęcie:
«Teraz umrę spokojny! Jest przecie na świecie
Człowiek, który przytuli moje drogie dziecię;
Bo wszak nad tym od dawna dzień i noc boleję,
Czy po śmierci ten rapier mój nie zerdzewieje!
Otóż nie zerdzewieje! Mój jaśnie wielmożny
Jenerale, wybacz mi, porzućcie te rożny,
Niemieckie szpadki; to wstyd szlacheckiemu dziecku
Nosić ten kijek: weźmij szablę po szlachecku!
Oto ten mój Scyzoryk u nóg twoich składam,
To jest co najdroższego na świecie posiadam;
Nie miałem nigdy żony, nie miałem dziecięcia,
On był żoną i dzieckiem; z mojego objęcia
Nigdy on nie wychodził; od rana do mroku
Pieściłem go, on w nocy sypiał przy mym boku;
A kiedym się zestarzał, nad łóżkiem na ścianie
Wisiał, jako nad Żydem Boże przykazanie!
Myśliłem zakopać go razem z ręką w grobie,
Lecz znalazłem dziedzica — Niechaj służy tobie!»

    Jenerał wpół śmiejąc się, a na wpół wzruszony:
«Kolego — rzekł — jeżeli ustąpisz mnie żony
I dziecka, to zostaniesz przez resztę żywota
Bardzo samotny, stary, wdowiec i sierota!
Powiedz, czym ci ten drogi dar mam wynagrodzić
I czym twoje sieroctwo i wdowstwo osłodzić?»
«Czy ja Cybulski? — rzecze na to Klucznik z żalem —
Co żonę przegrał, grając w mariasza z Moskalem,
Jak o tym pieśń powiada. Ja mam dosyć na tem,
Że mój Scyzoryk jeszcze zabłyśnie przed światem
W takim ręku! Niech tylko jenerał pamięta,
Aby tasiemka była długa, rozciągnięta,
Bo to długie; a zawsze od lewego ucha
Ciąć oburącz, to przetniesz od głowy do brzucha».

    Jenerał wziął Scyzoryk; lecz że bardzo długi,
Nie mógł nosić, w furgonie schowały go sługi.
Co się z nim stało, różnie powiadają o tem,
Lecz nikt pewnie nie wiedział ni wtenczas, ni potem.

    Dąbrowski rzekł do Maćka: «A ty co, kolego?
Zdaje się, żeś ty nie rad z przybycia mojego?
Milczysz kwaśny? I jakże, serce ci nie skacze,
Gdy widzisz orły złote, srebrne? gdy trębacze
Pobudkę Kościuszkowską trąbią ci nad uchem?
Maćku, myśliłem że ty większym jesteś zuchem!
Jeśli szabli nie weźmiesz i na koń nie siędziesz,
Przynajmniej z kolegami wesoło pić będziesz
Zdrowie Napoleona i Polski nadzieje!»

    «Ha! — rzekł Maciej — słyszałem, widzę co się dzieje!
Ale panie, dwóch orłów razem się nie gnieździ!
Łaska pańska, hetmanie, na pstrym koniu jeździ!
Cesarz wielki bohater! gadać o tym wiele!
Pamiętam, że Pułascy, moi przyjaciele,
Mawiali, poglądając na Dymuliera,
Że dla Polski polskiego trzeba bohatera,
Nie Francuza ani też Włocha, ale Piasta,
Jana albo Józefa, lub Maćka — i basta.
Wojsko! mówią, że polskie!… Lecz te fizyliery,
Sapery, grenadiery i kanonijery:
Więcej słychać niemieckich tytułów w tym tłumie
Niżeli narodowych! Kto to już zrozumie!
A muszą też być z wami Turki czy Tatary
Czy syzmatyki, co ni Boga, ani wiary:
Sam widziałem, kobiety w wioskach napastują,
Przechodniów odzierają, kościoły rabują!
Cesarz idzie do Moskwy… daleka to droga,
Jeśli cesarz jegomość wybrał się bez Boga!
Słyszałem, że już podpadł pod klątwy biskupie;
Wszytko to jest…» Tu Maciej chleb umoczył w zupie,
I jedząc nie dokończył ostatniego słowa.

    Nie w smak Podkomorzemu poszła Maćka mowa,
Młodzież zaczęła szemrać; Sędzia przerwał swary,
Głosząc przybycie trzeciej narzeczonej pary.

    Był to Rejent, sam siebie Rejentem ogłosił,
Nikt go nie poznał. Dotąd polskie suknie nosił,
Lecz teraz Telimena, przyszła żona, zmusza
Warunkiem intercyzy, wyrzec się kontusza;
Więc się Rejent rad nierad po francusku przebrał.
Widno, że mu frak duszy połowę odebrał,
Stąpa, jakby kij połknął, prosto, nieruchawo,
Jak żuraw; nie śmie spójrzeć ni w lewo, ni w prawo;
Mina gęsta, lecz z miny widać że jest w męce,
Nie wie jak się pokłonić, gdzie ma podziać ręce,
On, co tak gesty lubił! Ręce za pas sadził,
Nie masz pasa — tylko się po żołądku gładził;
Postrzegł omyłkę; bardzo zmieszał się, spiekł raka,
I ręce obie schował w jedną kieszeń fraka.
Idzie jakby przez rózgi śród szeptów i drwinek,
Wstydząc się za frak, jakby za niecny uczynek;
Aż spotkał oczy Maćka i zadrżał z bojaźni.

    Maciej dotąd z Rejentem żył w wielkiej przyjaźni;
Teraz wzrok nań obrócił tak ostry i dziki,
Że Rejent zbladnął, zaczął zapinać guziki,
Myśląc, że Maciej wzrokiem suknie z niego złupi.
Dobrzyński tylko dwakroć wyrzekł głośno: «Głupi!»
I tak strasznie zgorszył się z Rejenta przebrania,
Że zaraz wstał od stołu, i bez pożegnania
Wymknąwszy się, wsiadł na koń, wrócił do zaścianka.

    A tymczasem Rejenta nadobna kochanka,
Telimena, roztacza blaski swej urody,
I ubiór, od stóp do głów co najświeższej mody.
Jaką miała sukienkę, jaki strój na głowie,
Daremnie pisać, pióro tego nie wypowie;
Chyba pędzel by skreślił te tiule, ptyfenie,
Blondyny, kaszemiry, perły i kamienie,
I oblicze różane i żywe wejrzenie.

    Poznał ją zaraz Hrabia. Z zadziwienia blady
Wstał od stołu i szukał koło siebie szpady:
«I tyżeś to! — zawołał — czy mnie oczy łudzą?
Ty? w obecności mojej ściskasz rękę cudzą?
O niewierna istoto, o duszo zmiennicza!
I nie skryjesz ze wstydu pod ziemię oblicza?
Takeś twojej tak świeżej niepomna przysięgi?
O łatwowierny! po cóż nosiłem te wstęgi!
Lecz biada rywalowi, co mię tak znieważa!
Po moim chyba trupie pójdzie do ołtarza!»

    Goście powstali, Rejent okropnie się zmieszał,
Podkomorzy rywalów zagodzić pośpieszał;
Lecz Telimena wziąwszy Hrabiego na stronę:
«Jeszcze — szepnęła — Rejent nie wziął mię za żonę;
Jeżeli pan przeszkadzasz, odpowiedzże na to,
A odpowiedz mi zaraz, krótko, węzłowato:
Czy mnie kochasz, czyś dotąd serca nie odmienił,
Czyś gotów, żebyś ze mną zaraz się ożenił,
Zaraz, dziś?… jeśli zechcesz, odstąpię Rejenta».
Hrabia rzekł: «O kobieto dla mnie niepojęta!
Dawniej w uczuciach twoich byłaś poetyczną,
A teraz mi się zdajesz całkiem prozaiczną!
Cóż są wasze małżeństwa, jeśli nie łańcuchy,
Które związują tylko ręce, a nie duchy?
Wierzaj: są oświadczenia, nawet bez wyznania;
Są obowiązki, nawet bez obowiązania!
Dwa serca, pałające na dwóch końcach ziemi,
Rozmawiają jak gwiazdy promieńmi drżącemi;
Kto wie! może dla tego ziemia tak do słońca
Dąży, i tak jest zawsze miłą dla miesiąca,
Że wiecznie patrzą na się i najkrótszą drogą
Biegą do siebie — ale zbliżyć się nie mogą!»
«Dość już tego — przerwała — nie jestem planetą
Z łaski Bożej, dość Hrabio: ja jestem kobietą,
Już wiem resztę, przestań mi pleść ni to ni owo.
Teraz ostrzegam: jeśli piśniesz jedno słowo
Ażeby ślub mój zerwać, to jak Bóg na niebie
Że z tymi paznokciami przyskoczę do ciebie
I…» — «Nie będę — rzekł Hrabia — szczęścia pani kłócił»
I oczy pełne smutku i wzgardy odwrócił.
I ażeby ukarać niewierną kochankę,
Za przedmiot stałych ogniów wziął Podkomorzankę.

    Wojski pragnął młodzieńców poróżnionych zgodzić
Przykładami mądrymi: więc zaczął wywodzić
Historyję o dziku Nalibockich lasów
I o kłótni Rejtana z księżęciem Denassów.
Ale goście tymczasem skończyli jeść lody
I z zamku na dziedziniec wyszli dla ochłody.

    Tam włość już kończy ucztę: krążą miodu dzbany.
Muzyka już się stroi i wzywa na tany;
Szukają Tadeusza, który stał na stronie
I coś pilnego szeptał swojej przyszłej żonie.

    «Zofio! muszę ciebie w bardzo ważnej rzeczy
Radzić się; już pytałem stryja, on nie przeczy.
Wiesz, iż znaczna część wiosek które mam posiadać,
Wedle prawa na ciebie powinna by spadać.
Ci chłopi są nie moi, lecz twoi poddani:
Nie śmiałbym ich urządzić bez woli ich pani.
Teraz, kiedy już mamy Ojczyznę kochaną:
Czyliż wieśniacy zyszczą z tą szczęśliwą zmianą
Tyle tylko, że pana innego dostaną?
Prawda, że byli dotąd rządzeni łaskawie:
Lecz po mej śmierci, Bóg wie, komu ich zostawię.
Jestem żołnierz, jesteśmy śmiertelni oboje,
Jestem człowiek, sam własnych kaprysów się boję:
Bezpieczniej zrobię, kiedy władzy się wyrzekę,
I oddam los włościanów pod prawa opiekę.
Sami wolni, uczyńmy i włościan wolnemi,
Oddajmy im w dziedzictwo posiadanie ziemi,
Na której się zrodzili, którą krwawą pracą
Zdobyli, z której wszystkich żywią i bogacą.
Lecz muszę ciebie ostrzec, że tych ziem nadanie
Zmniejszy nasz dochód, w miernym musimy żyć stanie.
Ja przywykłem do życia oszczędnego z młodu;
Lecz ty Zofio, jesteś z wysokiego rodu,
W stolicy przepędziłaś twoje młode lata,
Czyż zgodzisz się żyć na wsi, z daleka od świata,
Jak ziemianka?»

                        A na to Zosia rzekła skromnie:
«Jestem kobietą, rządy nie należą do mnie,
Wszakże pan będziesz mężem; ja do rady młoda,
Co pan urządzisz, na to całym sercem zgoda!
Jeśli, włość uwalniając, zostaniesz uboższy,
To Tadeuszu będziesz sercu memu droższy.
O moim rodzie mało wiem i nie dbam o to;
Tyle pomnę, że byłam ubogą sierotą,
Że od Sopliców byłam za córkę przybrana,
W ich domu hodowana i za mąż wydana.
Wsi nie lękam się. Jeśli w wielkim mieście żyłam,
To dawno, zapomniałam, wieś zawsze lubiłam;
I wierz mi, że mnie moje kogutki i kurki
Więcej bawiły niźli owe Peterburki.
Jeśli czasem tęskniłam do zabaw, do ludzi,
To z dzieciństwa; wiem teraz że mnie miasto nudzi;
Przekonałam się zimą po krótkim pobycie
W Wilnie, że ja na wiejskie urodzona życie:
Pośród zabaw tęskniłam znów do Soplicowa.
Pracy też nie lękam się, bom młoda i zdrowa,
Umiem chodzić około domu, nosić klucze;
Gospodarstwa, obaczysz, jak ja się wyuczę!»

    Gdy Zosia domawiała ostatnie wyrazy,
Podszedł ku niej zdziwiony i kwaśny Gerwazy:
«Już wiem! — rzekł — Sędzia mówił już o tej wolności!
Lecz nie pojmuję, co to ściąga się do włości!
Boję się, żeby to coś nie było z niemiecka!
Wszak wolność nie jest chłopska rzecz, ale szlachecka!
Prawda, że się wywodzim wszyscy od Adama,
Alem słyszał, że chłopi pochodzą od Chama,
Żydowie od Jafeta, my szlachta od Sema,
A więc panujem jako starsi nad obiema.
Jużci pleban inaczej uczy na ambonie…
Powiada, że to było tak w Starym Zakonie,
Ale skoro Chrystus Pan, choć z królów pochodził,
Między Żydami w chłopskiej stajni się urodził,
Odtąd więc wszystkie stany porównał i zgodził;
Niech i tak będzie, kiedy inaczej nie można!
Zwłaszcza, że jako słyszę, i jaśnie wielmożna
Pani moja Zofija na wszystko się zgadza;
Jej rozkazać, mnie słuchać: jużci przy niej władza.
Tylko ostrzegam, byśmy wolności nie dali
Pustej i słownej tylko, jako za Moskali,
Kiedy pan Karp nieboszczyk włościan wyswobodził ,
A Moskal ich podatkiem potrójnym ogłodził.
Radzę więc, aby chłopów starym obyczajem,
Uszlachcić i ogłosić, że im herb nasz dajem.
Pani udzieli jednym wioskom Półkozica,
Drugim niech swą Leliwę nada pan Soplica.
Natenczas i Rębajło uzna chłopa równym,
Gdy go ujrzy szlachcicem wielmożnym, herbownym.
Sejm potwierdzi.

                        A niech się mąż pani nie trwoży,
Iż oddanie ziem państwo tak bardzo zuboży:
Nie da Bóg, abym rączki córy dygnitarskiej
Widział umozolone w pracy gospodarskiej.
Jest na to sposób. W zamku wiem ja pewną skrzynię,
W której jest Horeszkowskie stołowe naczynie,
Przy tym różne sygnety, kanaki, manele,
Kity bogate, rzędy, cudne karabele.
Skarbczyk Stolnika, w ziemi skryty od grabieży,
Pani Zofii jako dziedziczce należy;
Pilnowałem go w zamku jako oka w głowie,
Od Moskalów i od was, państwo Soplicowie.
Mam także spory worek mych własnych talarów,
Uzbieranych z wysługi, tudzież z pańskich darów.
Myśliłem, gdy nam zamek wróconym zostanie,
Obrócić grosz na murów wyreperowanie;
Nowemu gospodarstwu dziś zda się w potrzebie; —
A więc, panie Soplico, wnoszę się do ciebie,
Będę żył u mej pani na łaskawym chlebie
I kołysząc Horeszków pokolenie trzecie,
Wprawiać do Scyzoryka pani mojej dziecię,
Jeśli syn — a syn będzie: bo wojny nadchodzą,
A w czasie wojny zawżdy synowie się rodzą».

    Ledwie ostatnie słowa domówił Gerwazy,
Gdy poważnymi kroki przystąpił Protazy.
Skłonił się i wydobył z zanadrza kontusza
Panegiryk ogromny, w półtrzecia arkusza.
Skomponował go rymem podoficer młody,
Który niegdyś w stolicy sławne pisał ody;
Potem wdział mundur, lecz i w wojsku beletrysta,
Wiersze rabiał. Już Woźny przeczytał ich trzysta,
Aż gdy przyszedł do miejsca: *O ty, której wdzięki*
*Budzą bolesną radość i rozkoszne męki!*
*Która na szyk Bellony gdy zwrócisz twarz piękną,*
*Złamią się wnet oszczepy i tarcze rozpękną!*
*Zwalcz dziś Marsa Hymenem; srogiej niezgód hydrze*
*Niech dłoń twoja syczące z czoła żmije wydrze!* —
Tadeusz i Zofia ustawnie klaskali,
Niby chwaląc, w istocie nie chcąc słuchać daléj.
Już z rozkazu Sędziego pleban stał na stole
I ogłaszał włościanom Tadeusza wolę.

    Zaledwie usłyszeli nowinę poddani,
Skoczyli do panicza, padli do nóg pani,
«Zdrowie państwu naszemu»! ze łzami krzyknęli;
Tadeusz krzyknął: «Zdrowie spółobywateli,
Wolnych, równych — Polaków!» — «Wnoszę ludu zdrowie!»
Rzekł Dąbrowski; lud krzyknął «Niech żyją wodzowie!
Wiwat wojsko, wiwat lud, wiwat wszystkie stany!»
Tysiącem głosów, zdrowia grzmiały na przemiany.

    Tylko Buchman radości podzielać nie raczył;
Pochwalał projekt, lecz go rad by przeinaczył:
A naprzód, komisyją legalną wyznaczył,
Która by… Krótkość czasu była na zawadzie,
Że nie stało się zadość Buchmanowej radzie.
Bo na dziedzińcu zamku już stali parami
Oficery z damami, wiara z wieśniaczkami.
«Poloneza!» krzyknęli wszyscy w jedno słowo.
Oficerowie wiodą muzykę wojskową;
Ale pan Sędzia w ucho rzekł do jenerała:
«Każ pan, żeby się jeszcze kapela wstrzymała.
Wiesz, że dzisiaj synowca mego zaręczyny;
A dawnym obyczajem jest naszej rodziny,
Zaręczać się i żenić przy wiejskiej muzyce.
Patrz, stoi cymbalista, skrzypak i kozice,
Poczciwi muzykanci; już się skrzypak zżyma,
A kobeźnik kłania się i żebrze oczyma.
Jeżeli ich odprawię, biedni będą płakać;
Lud przy innej muzyce nie potrafi skakać.
Niechaj ci zaczną; niech się i lud podweseli;
Potem będziem wybornej twej słuchać kapeli».
Dał znak.

                        Skrzypak u sukni zakasał rękawek,
Ścisnął gryf krzepko, oparł brodę o podstawek
I smyk jak konia w zawód puścił po skrzypicy.
Na to hasło, stojący obok kobeźnicy,
Jak gdyby w skrzydła bijąc, częstym ramion ruchem
Dmą w miechy i oblicza wypełniają duchem:
Myśliłbyś, że ta para w powietrze uleci,
Podobna do pyzatych Boreasza dzieci.
Brakło cymbałów.

                        Było cymbalistów wielu,
Ale żaden z nich nie śmiał zagrać przy Jankielu
(Jankiel przez całą zimę nie wiedzieć gdzie bawił,
Teraz się nagle z głównym sztabem wojska zjawił);
Wiedzą wszyscy, że mu nikt na tym instrumencie
Nie wyrówna w biegłości, w guście i talencie.
Proszą, ażeby zagrał, podają cymbały;
Żyd wzbrania się, powiada, że ręce zgrubiały,
Odwykł od grania, nie śmie i panów się wstydzi;
Kłaniając się umyka. Gdy to Zosia widzi,
Podbiega i na białej podaje mu dłoni
Drążki, którymi zwykle mistrz we struny dzwoni;
Drugą rączką po siwej brodzie starca głaska
I dygając: «Jankielu — mówi — jeśli łaska!
Wszak to me zaręczyny: zagrajże Jankielu!
Wszak nie raz przyrzekałeś grać na mym weselu?»

    Jankiel niezmiernie Zosię lubił: kiwnął brodą
Na znak, że nie odmawia; więc go w środek wiodą,
Podają krzesło, usiadł, cymbały przynoszą,
Kładą mu na kolanach. On patrzy z rozkoszą
I z dumą: jak weteran w służbę powołany,
Gdy wnuki ciężki jego miecz ciągną ze ściany,
Dziad śmieje się, choć miecza dawno nie miał w dłoni,
Lecz uczuł, że dłoń jeszcze nie zawiedzie broni.

    Tymczasem dwaj uczniowie przy cymbałach klęczą,
Stroją na nowo struny i próbując, brzęczą;
Jankiel z przymrużonymi na poły oczyma
Milczy i nieruchome drążki w palcach trzyma.

    Spuścił je. Zrazu bijąc taktem tryumfalnym,
Potem gęściej siekł struny jak deszczem nawalnym:
Dziwią się wszyscy. Lecz to była tylko proba;
Bo wnet przerwał i w górę podniósł drążki oba.

    Znów gra. Już drżą drążki, tak lekkimi ruchy,
Jak gdyby zadzwoniło w strunę skrzydło muchy,
Wydając ciche, ledwie słyszalne brzęczenia.
Mistrz zawsze patrzył w niebo czekając natchnienia.
Spójrzał z góry, instrument dumnym okiem zmierzył,
Wzniósł ręce, spuścił razem, w dwa drążki uderzył:
Zdumieli się słuchacze.

                        Razem ze strun wiela
Buchnął dźwięk, jakby cała janczarska kapela
Ozwała się z dzwonkami, z zelami, z bębenki:
Brzmi Polonez Trzeciego Maja! — Skoczne dźwięki
Radością oddychają, radością słuch poją;
Dziewki chcą tańczyć, chłopcy w miejscu nie dostoją —
Lecz starców myśli z dźwiękiem w przeszłość się uniosły,
W owe lata szczęśliwe, gdy senat i posły,
Po dniu Trzeciego Maja, w ratuszowej sali,
Zgodzonego z narodem króla fetowali,
Gdy przy tańcu śpiewano: *Wiwat król kochany!*
*Wiwat Sejm, wiwat Naród, wiwat wszystkie Stany!*

    Mistrz coraz takty nagli i tony natęża;
A wtem puścił fałszywy akord jak syk węża,
Jak zgrzyt żelaza po szkle: przejął wszystkich dreszczem
I wesołość pomięszał przeczuciem złowieszczem.
Zasmuceni, strwożeni, słuchacze zwątpili,
Czy instrument niestrojny? czy się muzyk myli?
Nie zmylił się mistrz taki! On umyślnie trąca
Wciąż tę zdradziecką strunę, melodyję zmąca,
Coraz głośniej targając akord rozdąsany,
Przeciwko zgodzie tonów skonfederowany:
Aż Klucznik pojął mistrza, zakrył ręką lica
I krzyknął: «Znam! znam głos ten! to jest *Targowica*!»
I wnet pękła ze świstem struna złowróżąca; Muzyk bieży do prymów, urywa takt, zmaca,
Porzuca prymy, bieży z drążkami do basów,
Słychać tysiące coraz głośniejszych hałasów;
Takt marszu, wojna, atak, szturm; słychać wystrzały,
Jęk dzieci, płacze matek. — Tak mistrz doskonały
Wydał okropność szturmu, że wieśniaczki drżały,
Przypominając sobie ze łzami boleści
*Rzeź Pragi*, którą znały z pieśni i z powieści,
Rade, że mistrz na koniec strunami wszystkiemi
Zagrzmiał, i głosy zdusił, jakby wbił do ziemi.

    Ledwie słuchacze mieli czas wyjść z zadziwienia,
Znowu muzyka inna — znów zrazu brzęczenia
Lekkie i ciche; kilka cienkich strunek jęczy,
Jak kilka much, gdy z siatki wyrwą się pajęczéj.
Lecz strun coraz przybywa: Już rozpierzchłe tony
Łączą się i akordów wiążą legijony,
I już w takt postępują zgodzonymi dźwięki,
Tworząc nutę żałośną tej sławnej piosenki:
*O żołnierzu, tułaczu, który borem, lasem*
*Idzie, z biedy i z głodu przymierając czasem,*
*Na koniec pada u nóg konika wiernego,*
*A konik nogą grzebie mogiłę dla niego.*
Piosenka stara, wojsku polskiemu tak miła!
Poznali ją żołnierze; wiara się skupiła
Wkoło mistrza; słuchają, wspominają sobie,
Ów czas okropny, kiedy na Ojczyzny grobie
Zanucili tę piosnkę i poszli w kraj świata;
Przywodzą na myśl długie swej wędrówki lata,
Po lądach, morzach, piaskach gorących i mrozie,
Pośrodku obcych ludów, gdzie często w obozie
Cieszył ich i rozrzewniał ten śpiew narodowy.
Tak rozmyślając smutnie pochylili głowy.

    Ale je wnet podnieśli, bo mistrz tony wznosi,
Natęża, takty zmienia: coś innego głosi.
I znowu spójrzał z góry, okiem struny zmierzył,
Złączył ręce, oburącz w dwa drążki uderzył:
Uderzenie tak sztuczne, tak było potężne,
Że struny zadzwoniły jak trąby mosiężne
I z trąb znana piosenka ku niebu wionęła,
Marsz tryumfalny: *Jeszcze Polska nie zginęła*!
*Marsz Dąbrowski do Polski!* — I wszyscy klasnęli,
I wszyscy «Marsz Dąbrowski!» chórem okrzyknęli.

    Muzyk, jakby sam swojej dziwił się piosence,
Upuścił drążki z palców, podniósł w górę ręce;
Czapka lisia spadła mu z głowy na ramiona,
Powiewała poważnie broda podniesiona,
Na jagodach miał kręgi dziwnego rumieńca,
We wzroku ducha pełnym błyszczał żar młodzieńca,
Aż gdy na Dąbrowskiego starzec oczy zwrócił,
Zakrył rękami, spod rąk łez potok się rzucił:
«Jenerale — rzekł — ciebie długo Litwa nasza
Czekała — długo, jak my Żydzi Mesyjasza…
Ciebie prorokowali dawno między ludem
Śpiewaki, ciebie niebo obwieściło cudem,
Żyj i wojuj, o ty nasz!…» Mówiąc, ciągle szlochał,
Żyd poczciwy Ojczyznę jako Polak kochał!
Dąbrowski mu podawał rękę i dziękował,
On, czapkę zdjąwszy, wodza rękę ucałował.

    Poloneza czas zacząć. — Podkomorzy rusza
I z lekka zarzuciwszy wyloty kontusza,
I wąsa pokręcając, podał rękę Zosi
I skłoniwszy się grzecznie w pierwszą parę prosi.
Za Podkomorzym szereg w pary się gromadzi,
Dano hasło, zaczęto taniec: on prowadzi.

    Nad murawą czerwone połyskają buty,
Bije blask z karabeli, świeci się pas suty,
A on stąpa powoli, niby od niechcenia:
Ale z każdego kroku, z każdego ruszenia,
Można tancerza czucia i myśli wyczytać.
Oto stanął, jak gdyby chciał swą damę pytać,
Pochyla ku niej głowę, chce szepnąć do ucha;
Dama głowę odwraca, wstydzi się, nie słucha;
On zdjął konfederatkę, kłania się pokornie,
Dama raczyła spójrzeć, lecz milczy upornie;
On krok zwalnia, oczyma jej spojrzenia śledzi,
I zaśmiał się na koniec; rad z jej odpowiedzi
Stąpa prędzej, pogląda na rywalów z góry,
I swą konfederatkę z czaplinymi pióry
To na czole zawiesza, to nad czołem wstrząsa,
Aż włożył ją na bakier i pokręcił wąsa.
Idzie; wszyscy zazdroszczą, biegą w jego ślady,
On by rad ze swą damą wymknąć się z gromady:
Czasem staje na miejscu, rękę grzecznie wznosi
I żeby mimo przeszli, pokornie ich prosi;
Czasem zamyśla zręcznie na bok się uchylić,
Odmienia drogę, rad by towarzyszów zmylić,
Lecz go szybkimi kroki ścigają natręty,
I zewsząd obwijają tanecznymi skręty;
Więc gniewa się, prawicę na rękojeść składa,
Jakby rzekł: «Nie dbam o was, zazdrośnikom biada!»
Zwraca się z dumą w czole i z wyzwaniem w oku,
Prosto w tłum; tłum tancerzy nie śmie dostać w kroku,
Ustępują mu z drogi, — i zmieniwszy szyki,
Puszczają się znów za nim. —

                        Brzmią zewsząd okrzyki:
«Ach to może ostatni! patrzcie, patrzcie młodzi,
Może ostatni, co tak poloneza wodzi!»
I szły pary po parach hucznie i wesoło,
Rozkręcało się, znowu skręcało się koło,
Jak wąż olbrzymi w tysiąc łamiący się zwojów;
Mieni się cętkowata, różna barwa strojów
Damskich, pańskich, żołnierskich, jak łuska błyszcząca,
Wyzłocona promieńmi zachodniego słońca
I odbita o ciemne murawy wezgłowia.
Wre taniec, brzmi muzyka, oklaski i zdrowia!

    Tylko kapral Dobrzyński Sak ani kapeli
Nie słucha, ani tańczy, ani się weseli.
Ręce w tył założywszy, stoi zły, ponury,
Wspomina swe dawniejsze do Zosi konkury;
Jak lubił dla niej nosić kwiaty, pleść koszyczki,
Wybierać gniazda ptasie, robić zauszniczki.
Niewdzięczna! Chociaż tyle pięknych darów strwonił,
Choć przed nim uciekała, choć mu ojciec bronił:
On jeszcze! ile razy na parkanie siadał,
By ją dojrzeć przez okna, w konopie się wkradał,
Żeby patrzeć, jak ona pleła swe ogródki,
Rwała ogórki albo karmiła kogutki!
Niewdzięczna! Spuścił głowę i na koniec świsnął
Mazurka; potem kaszkiet na uszy nacisnął
I szedł w obóz, gdzie stała przy armatach warta;
Tam dla rozerwania się zaczął grać w drużbarta
Z wiarusami, kielichem osładzając żałość.
Taka była dla Zosi Dobrzyńskiego stałość.

    Zosia tańczy wesoło: lecz choć w pierwszej parze,
Ledwie widna z daleka. Na wielkim obszarze
Zarosłego dziedzińca, w zielonej sukience,
Ustrojona w równianki i w kwieciste wieńce,
Śród traw i kwiatów krąży niewidzialnym lotem,
Rządząc tańcem, jak anioł nocnych gwiazd obrotem.
Zgadniesz gdzie jest: bo ku niej obrócone oczy,
Wyciągnięte ramiona, ku niej zgiełk się tłoczy.
Darmo się Podkomorzy zostać przy niej sili:
Zazdrośnicy już z pierwszej pary go odbili;
I szczęśliwy Dąbrowski niedługo się cieszył,
Ustąpił ją drugiemu; a już trzeci spieszył;
I ten zaraz odbity, odszedł bez nadziei.
Aż Zosia, już strudzona, spotkała z kolei
Tadeusza, i dalszej lękając się zmiany,
I chcąc przy nim pozostać, zakończyła tany.
Idzie do stołu gościom nalewać kielichy.

    Słońce już gasło, wieczór był ciepły i cichy,
Okrąg niebios gdzieniegdzie chmurkami zasłany,
U góry błękitnawy, na zachód różany;
Chmurki wróżą pogodę: lekkie i świecące,
Tam jako trzody owiec na murawie śpiące,
Ówdzie nieco drobniejsze, jak stada cyranek;
Na zachód obłok na kształt rąbkowych firanek,
Przejrzysty, sfałdowany, po wierzchu perłowy,
Po brzegach pozłacany, w głębi purpurowy,
Jeszcze blaskiem zachodu tlił się i rozżarzał,
Aż powoli pożółkniał, zbladnął i poszarzał.
Słońce spuściło głowę, obłok zasunęło,
I raz ciepłym powietrzem westchnąwszy — usnęło.

    A szlachta ciągle pije i wiwaty wznosi:
Napoleona, wodzów, Tadeusza, Zosi,
Wreszcie z kolei wszystkich trzech par zaręczonych,
Wszystkich gości obecnych, wszystkich zaproszonych,
Wszystkich przyjaciół, których kto żywy spamięta,
I których zmarłych pamięć pozostała święta!

    I ja tam z gośćmi byłem, miód i wino piłem,
A com wiedział i słyszał, w księgi umieściłem.



Epilog

    O tymże dumać na paryskim bruku,
Przynosząc z miasta uszy pełne stuku,
Przeklęstw i kłamstwa, niewczesnych zamiarów,
Zapóźnych żalów, potępieńczych swarów?…

    Biada nam zbiegi, żeśmy w czas morowy
Lękliwe nieśli za granicę głowy!
Bo gdzie stąpili, szła przed nami trwoga,
W każdym sąsiedzie znajdowali wroga;
Aż nas objęto w ciasny krąg łańcucha,
I każą oddać co najprędzej ducha.

    A gdy na żale ten świat nie ma ucha,
Gdy ich co chwila nowina przeraża,
Bijąca z Polski jako dzwon smętarza,
Gdy im prędkiego zgonu życzą straże,
Wrogi ich wabią z dala jak grabarze,
Gdy w niebie nawet nadziei nie widzą…
Nie dziw, że ludzi, świat, siebie ohydzą,
Że utraciwszy rozum w mękach długich,
Plwają na siebie i źrą jedni drugich!

    Chciałem pominąć, ptak małego lotu,
Pominąć strefy ulewy i grzmotu,
I szukać tylko cienia i pogody:
Wieki dzieciństwa, domowe zagrody…

    Jedyne szczęście: kto w szarej godzinie,
Z kilką przyjaciół siadłszy przy kominie,
Drzwi od Europy zamykał hałasów,
Wyrwał się myślą do szczęśliwszych czasów,
I dumał, marzył o swojej krainie…

    Ale o krwi tej, co się świeżo lała,
O łzach, którymi płynie Polska cała,
O sławie, która jeszcze nie przebrzmiała:
O nich pomyśleć nie mieliśmy duszy!…
Bo naród bywa na takiej katuszy,
Że, kiedy zwróci wzrok ku jego męce,
Nawet Odwaga załamuje ręce.

    Te pokolenia żałobami czarne,
Powietrze tylą klątwami ciężarne,
Tam myśl nie śmiała swoich zwrócić lotów,
W sferę okropną nawet ptakom grzmotów.

    O Matko Polsko! Ty tak świeżo w grobie
Złożona… Nie masz sił mówić o tobie!

    Ach, czyjeż usta śmią pochlebiać sobie,
Że znajdą dzisiaj to czarowne słowo,
Które rozczuli rozpacz marmurową,
Które z serc wieko podejmie kamienne,
Rozwiąże oczy, tylą łez brzemienne
I sprawia, że łza przystygła wypłynie,
Nim się te usta znajdą, wiek przeminie.

    Kiedyś… gdy zemsty lwie przehuczą ryki,
Przebrzmi głos trąby, przełamią się szyki,
Gdy orły nasze lotem błyskawicy
Spadną u dawnej Chrobrego granicy,
Ciał się najedzą, krwią całe opłyną,
I skrzydła wreszcie na spoczynek zwiną;
Gdy wróg ostatni wyda krzyk boleści,
Umilknie, światu swobodę obwieści —
Wtenczas — dębowym liściem uwieńczeni,
Rzuciwszy miecze, siędą rozbrojeni
Rycerze nasi, zechcą słuchać o przeszłości!
Wtenczas zapłaczą nad ojców losami,
I wtenczas łza ta ich lica nie splami.

    Dziś dla nas, w świecie nieproszonych gości,
W całej przeszłości i w całej przyszłości,
Jedna już tylko dziś kraina taka,
W której jest trochę szczęścia dla Polaka:
Kraj lat dziecinnych! On zawsze zostanie
Święty i czysty jak pierwsze kochanie,
Niezaburzony błędów przypomnieniem,
Niepodkopany nadziei złudzeniem,
Ani zmieniony wypadków strumieniem.

    Te kraje rad bym myślami powitał,
Gdziem rzadko płakał, a nigdy nie zgrzytał:
Kraje dzieciństwa, gdzie człowiek po świecie
Biegł jak po łące, a znał tylko kwiecie
Miłe i piękne, jadowite rzucił,
Ku pożytecznym oka nie odwrócił.

    Ten kraj szczęśliwy, ubogi i ciasny,
Jak świat jest boży, tak on był nasz własny!
Jakże tam wszystko do nas należało,
Jak pomnim wszystko, co nas otaczało:
Od lipy, która koroną wspaniałą
Całej wsi dzieciom użyczała cienia,
Aż do każdego strumienia, kamienia,
Jak każdy kącik ziemi był znajomy
Aż po granicę — po sąsiadów domy.

    A jeśli czasem i Moskal się zjawił,
Tyle nam tylko pamiątki zostawił,
Że był w błyszczącym i pięknym mundurze:
Bo węża tylko znaliśmy po skórze.

    I tylko krajów tych obywatele
Jedni zostali wierni przyjaciele,
Jedni dotychczas sprzymierzeńcy pewni!
Bo któż tam mieszkał? Matka, bracia, krewni,
Sąsiedzi dobrzy!… Kogo z nich ubyło,
Jakże tam o nim czule się mówiło!
Ile pamiątek, jaka żałość długa,
Tam, gdzie do pana przywiązańszy sługa
Niż w innych krajach małżonka do męża;
Gdzie żołnierz dłużej żałuje oręża
Niż tu syn ojca; po psie płaczą szczerze
I dłużej niż tu lud po bohaterze.

    I przyjaciele wtenczas pomogli rozmowie.
I do pieśni rzucali mi słowo po słowie:
Jak bajeczne żurawie, na dzikim ostrowie,
Nad zaklętym pałacem przelatując wiosną,
I słysząc zaklętego chłopca skargę głośną,
Każdy ptak chłopcu jedno pióro rzucił:
On zrobił skrzydła i do swoich wrócił…

    O, gdybym kiedyś dożył tej pociechy,
Żeby te księgi zbłądziły pod strzechy;
Żeby wieśniaczki kręcąc kołowrotki,
Gdy odśpiewają ulubione zwrotki
O tej dziewczynie, co tak grać lubiła,
Że przy skrzypeczkach gąski pogubiła,
O tej sierocie, co piękna jak zorze,
Zaganiać ptastwo szła w wieczornej porze:
Gdyby też wzięły wieśniaczki do ręki
Te księgi proste jako ich piosenki!…

    Tak za dni moich przy wiejskiej zabawie,
Czytano nieraz pod lipą na trawie
Pieśń o Justynie, powieść o Wiesławie;
A przy stoliku drewnianym pan włodarz
Albo ekonom, lub nawet gospodarz,
Nie bronił czytać i sam słuchać raczył,
I młodszym rzeczy trudniejsze tłumaczył,
Chwalił piękności, a błędom wybaczył.

    I zazdrościła młodzież wieszczów sławie,
Która tam dotąd brzmi w lasach i w polu,
I którym droższy niż laur Kapitolu,
Wianek rękami wieśniaczki usnuty
Z modrych bławatków i zielonej ruty…'''


for x in range(97,123):
    litera=chr(x)
    print(litera, len(re.findall(litera,tekst)))

for y in range(65,97):
    litera=chr(y)
    print(litera, len(re.findall(litera,tekst)))