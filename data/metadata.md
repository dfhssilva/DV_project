**Airbnb Metadata**

**Base de dados e contexto**

Esta base de dados contém dados publicamente disponíveis à cerca da Airbnb, sendo que estes foram _scrapped_ diretamente do seu _website_. Os dados presentes permitem explorar como a Airbnb tem vindo a ser usada no distrito de Lisboa. É conhecido que a Airbnb tem vindo a destabilizar o mercado de habitação em todo o mundo, porém tal plataforma também ajuda a desenvolver o turismo. Como tal, propomos que através dos dados disponíveis explorem o verdadeiro impacto, quer positivo ou negativo, desta plataforma no cenário de habitação da capital portuguesa. Tratar-se-á a Airbnb de um conceito disruptivo? Ou será que existe solução para os efeitos negativos desta companhia? Para mais conhecimento sobre este tópico, por favor ler: [https://www.bbc.com/news/business-45083954](https://www.bbc.com/news/business-45083954)

**Documentos**

lisbon\_0619\_listings.csv

- Este dataset revela informação à cerca de cada listing (anúncio) apresentado no site do Airbnb referente ao distrito de lisboa.

_listing\_Id_: identificador único de um anúncio

_listing\_url_: url link do anúncio

_scrape\_id_: identificador do _scrape_

_last\_scraped_: data quando os dados foram _scrapped_ pela última vez

_name_: nome do anúncio

_summary_: sumário do anúncio

_space_: descrição do espaço (alguns anfitriões interpretaram o _space_ como propriedade, outros como localização)

_description_: descrição do anúncio. Contém informação diversa sobre o anúncio (e.g. propriedade, localização, como chegar, etc.)

_experiences\_offered_: quais as experiências incluídas com a estadia

_neighborhood\_overview_: descrição do bairro em que a propriedade está inserida

_notes_: notas com informação adicional

_transit_: informações sobre meios de transporte desde a propriedade e de que maneira o hospede pode-os utilizar

_access_: informação à cerca dos acessos (alguns anfitriões interpretaram o _access_ como acesso do hospede às diversas partes da propriedade, outros como forma de chegar à propriedade)

_interaction_: de que forma o hospede irá interagir com o anfitrião

_house\_rules_: regras da propriedade

_thumbnail\_url_: url link do _thumbnail_

_medium\_url_: url link do _medium_

_picture\_url_: url link da foto

_xl\_picture\_url_: url link da foto grande

_host\_id_: identificador do anfitrião

_property\_id_: identificador da propriedade

_room\_type_: tipo do quarto disponibilizado pelo anúncio

_accommodates_: número de hospedes permitido pelo anúncio

_bathrooms_: número de casas de banho listado

_bedrooms_: número de quartos listado

_beds_: número de camas listado

_bed\_type_: tipo das camas

_amenities_: comodidades oferecidas pelo anúncio

_square\_feet_: dimensão do espaço disponibilizado pelo anúncio em pés quadrados

_price_: preço por noite listado

_weekly\_price_: preço por semana listado

_monthly\_price_: preço por mês listado

_security\_deposit_: depósito de dinheiro necessário pelo anúncio (se necessário)

_cleaning\_fee_: cobrança pela limpeza necessária pelo anúncio (se necessária)

_guests\_included_: número de pessoas incluídas sem pagar taxa extra

_extra\_people_: taxa extra por número de pessoas adicional ao valor de _guests\_included_

_minimum\_nights_: número mínimo de noites que um hospede pode reservar (critério geral)

_maximum\_nights_: número máximo de noites que um hospede pode reservar (critério geral)

_minimum\_minimum\_nights_: menor número mínimo de noites que um hospede pode reservar. O anfitrião pode definir um número mínimo de noites diferente para ocasiões específicas (e.g. fim de semanas, época de verão, passagem de ano, etc.)

_maximum\_minimum\_nights_: menor número máximo de noites que um hospede pode reservar. O anfitrião pode definir um número máximo de noites diferente para ocasiões específicas (e.g. fim de semanas, época de verão, passagem de ano, etc.)

_minimum\_maximum\_nights_: maior número mínimo de noites que um hospede pode reservar. O anfitrião pode definir um número mínimo de noites diferente para ocasiões específicas (e.g. fim de semanas, época de verão, passagem de ano, etc.)

_maximum\_maximum\_nights_: maior número máximo de noites que um hospede pode reservar. O anfitrião pode definir um número máximo de noites diferente para ocasiões específicas (e.g. fim de semanas, época de verão, passagem de ano, etc.)

_minimum\_nights\_avg\_ntm_: média dos números mínimos de noites que um hospede pode reservar para os próximos 12 meses (ntm= _next twelve months_)

_maximum\_nights\_avg\_ntm_: media dos números máximos de noites que um hospede pode reservar para os próximos 12 meses (ntm= _next twelve months_)

_calendar\_updated_: última vez que o calendário do anúncio foi atualizado (e.g. datas bloqueadas/ libertadas, preços mudados, restrições quanto ao número de noites por reserva alterados)

_has\_availability_: tem ou não disponibilidade para reservar

_availability\_next\_30_: quantos dias dos próximos 30 dias estão disponíveis para serem reservados

_availability\_next\_60_: quantos dias dos próximos 60 dias estão disponíveis para serem reservados

_availability\_next\_90_: quantos dias dos próximos 90 dias estão disponíveis para serem reservados

_availability\_next\_365_: quantos dias dos próximos 365 dias estão disponíveis para serem reservados

_calendar\_last\_scraped_: data quando o calendário foi _scrapped_ pela última vez

_number\_of\_reviews_: número de _reviews_ do anúncio

_number\_of\_reviews\_ltm_: número de _reviews_ do anúncio nos últimos 12 meses (ltm= _last twelve months_)

_reviews\_per\_month_: número médio de _reviews_ por mês

_first\_review_: data quando o anúncio obteve a sua primeira _review_

_last\_review_: data quando o anúncio obteve a sua última _review_

_review\_scores\_rating_: avaliação geral da estadia (_What was your guest&#39;s overall experience?)_

_review\_scores\_accuracy_: avaliação referente à precisão do anúncio (_How accurately did your listing page represent your space?)_

_review\_scores\_cleanliness_: avaliação referente à limpeza da propriedade (_Did your guests feel that your space was clean and tidy?_)

_review\_scores\_checkin_: avaliação referente à chegada dos hospedes (_How smoothly did their check-in go?_)

_review\_scores\_communication_: avaliação referente à comunicação hospede-anfitrião (_How well did you communicate with your guest before and during their stay?_)

_review\_scores\_location_: avaliação referente à localização da propriedade (_How did guests feel about your neighborhood?_)

_review\_scores\_value_: avaliação referente ao aspeto valor-preço (_Did your guest feel your listing provided good value for the price?_)

_requires\_license_: é preciso licença para listar a casa no Airbnb? Algumas cidades requerem que hospedes obtenham uma licença ou número de registo de modo a que possam listar as suas casas no Airbnb

_license_: licença ou número de registo necessário para listar a casa no Airbnb. Nem todos os hospedes necessitam de registar, portanto a ausência do número não significa necessariamente que o hospede não esteja a cumprir com as normas. &quot;Exempt&quot; significa que a listagem do anfitrião está isenta do processo de registo da cidade por razões determinadas pela cidade

_jurisdiction\_names_: nomes das jurisdições

_instant\_bookable_: &quot;instant bookable&quot; significa que o anúncio não precisa de aprovação do anfitrião para ser reservado. Esta variável determina se o anúncio é &quot;instante bookable&quot; ou não

_is\_business\_travel\_ready:_ &quot;business travel ready&quot; é um programa lançado em 2015 pela Airbnb para atrair viajantes profissionais e desviá-los dos hosteis locais. Esta variável determina se o anúncio é &quot;business travel ready&quot; ou não

_cancellation\_policy_: política de cancelamento do anúncio

_require\_guest\_profile\_picture_: é necessária uma fotografia de perfil para o hospede puder reservar no anúncio?

_require\_guest\_phone\_verification_: As verificações de perfil são uma forma de vincular o perfil da Airbnb a outras informações pessoais, como o perfil do Facebook, número de telefone, endereço de email ou identificação emitida pelo governo. Estas permitem confirmar a identidade da pessoa, dando confiança a relação hospede-anfitrião. Esta variável identifica se o anúncio requer que o hospede tenha o número de telefone vinculado ao perfil da Airbnb para efetuar uma reserva.

lisbon\_0619\_dailycalendar.csv

- Para cada anúncio mostra o calendário dos próximos 365 dias assim como informação para cada um dos dias. Relação anúncio-calendário de 1-N.

_listing\_id_: identificador único de um anúncio

_date_: data referente ao calendário

_available_: disponibilidade do anúncio para uma determinada data

_price_: preço do anúncio para uma determinada data

_adjusted\_price_: preço ajustado do anúncio para uma determinada data (o que o hospede irá pagar na realidade)

_minimum\_nights_: número mínimo de noites que o anúncio pode ser reservado para essa data

_maximum\_nights_: número máximo de noites que o anúncio pode ser reservado para essa data

lisbon\_0619\_hosts.csv

- Mostra informação relativa a cada anfitrião. Relação anúncio-anfitrião de N-1.

_host\_id_: identificador único de um anfitrião

_host\_url_: url link do anfitrião

_host\_name_: nome do anfitrião

_host\_since_: data a partir de quando a pessoa se tornou anfitrião

_host\_location_: onde o anfitrião vive

_host\_about_: informação pessoal à cerca do anfitrião

_host\_response\_time_: tempo que o anfitrião normalmente demora a responder às mensagens

_host\_response\_rate_: percentagem das mensagens a que o anfitrião responde

_host\_acceptance\_rate_: percentagem de pedidos de reserva aceitados pelo anfitrião

_host\_is\_superhost_: o anfitrião é &quot;superhost&quot;? Os &quot;Superhosts&quot; são anfitriões experientes que dão um excelente exemplo para os outros e garantem experiências extraordinárias aos seus hóspedes. Para ser um &quot;superhost&quot; é necessário: 1) concluir pelo menos 10 viagens ou concluir com sucesso 3 reservas que totalizem pelo menos 100 noites; 2) manter uma taxa de resposta de 90% ou superior; 3) manter uma taxa de cancelamento de 1% (1 cancelamento por cada 100 reservas) ou menos, com exceções para cancelamentos que se enquadrem na nossa política de Circunstâncias Atenuantes; 4) manter uma classificação geral de 4,8

_host\_thumbnail\_url_: url link da foto de perfil pequena

_host\_picture\_url_: url link da foto de perfil normal

_host\_neighbourhood_: bairro do anfitrião

_host\_listings\_count_: número de anúncios que o anfitrião tem

_host\_total\_listings\_count_: número total de anúncios que o anfitrião tem

_host\_verifications_: as verificações de perfil são uma forma de vincular o perfil da Airbnb a outras informações pessoais, como o perfil do Facebook, número de telefone, endereço de email ou identificação emitida pelo governo. Estas permitem confirmar a identidade da pessoa, dando confiança a relação hospede-anfitrião. Esta variável mostra quais as verificações de perfil que o anfitrião possui

_host\_has\_profile\_pic_: identifica se o anfitrião possui uma foto de perfil

_host\_identity\_verified_: a verificação de identidade requer que um anfitrião faça upload de um documento de identificação governamental válido (e.g. passaporte, carta de condução, cartão de cidadão, bilhete de identidade, etc.), assim como de uma foto recente que permita ser comparada com a do documento de identificação. Se o documento for válido e após a comparação ser validada, o anfitrião tem a sua identidade verificada, o que atribui credibilidade a este. Esta variável mostra se o anfitrião tem a sua identidade verificada.

_calculated\_host\_listings\_count_: cálculo do número de anúncios que o anfitrião tem

_calculated\_host\_listings\_count\_entire\_homes_: cálculo do número de anúncios com casa inteira disponível (_room\_type_) que o anfitrião tem

_calculated\_host\_listings\_count\_private\_rooms_: cálculo do número de anúncios com quarto privado (_room\_type_) que o anfitrião tem

_calculated\_host\_listings\_count\_shared\_rooms_: cálculo do número de anúncios com quarto partilhado (_room\_type_) que o anfitrião tem

lisbon\_0619\_property.csv

- Mostra todas as propriedades listadas no Airbnb, assim como informação respetiva. Relação anúncio-propriedade de N-1.

_property\_id_: identificador único de uma propriedade

_street_: rua onde a propriedade está inserida

_neighbourhood_: bairro onde a propriedade está inserida

_neighbourhood\_cleansed_: bairro onde a propriedade está inserida (sem erros de _encoding_)

_neighbourhood\_group\_cleansed_: concelho onde a propriedade está inserida

_city_: cidade onde a propriedade está inserida

_state_: estado onde a propriedade está inserida

_zipcode_: código postal da propriedade

_market_: mercado onde a propriedade está listada

_smart\_location_: morada da propriedade (incompleta)

_country\_code_: código do país onde a propriedade está inserida

_country_: país onde a propriedade está inserida

_latitude_: latitude da propriedade

_longitude_: longitude da propriedade

_is\_location\_exact_: a localização da propriedade é exata? Opção de privacidade.

_property\_type_: tipo da propriedade (e.g. apartamento, moradia, etc.)

lisbon\_0619\_neighbourhoods.csv

- Mostra quais os concelhos e bairros existentes no distrito de Lisboa. Relação propriedade-bairro de N-1.

_neighbourhood\_group_: grupo de bairros (concelho)

_neighbourhood_: bairro

lisbon\_0619\_reviews.csv

- Revela todas as _reviews_ feitas por hospedes aos anúncios correspondentes. Relação anúncio-_review_ de 1-N.

_listing\_id_: identificador único do anúncio

_review\_id_: identificador único da _review_

_date_: data de quando a _review_ foi escrita

_reviewer\_id_: identificador único da pessoa que escreveu a _review_

_reviewer\_name_: nome da pessoa que escreveu a _review_

_comments_: comentário realizado na _review_