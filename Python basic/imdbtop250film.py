import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")

list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=250) 
count=1
for tr in list:
    title=tr.find("td",{"class":"titleColumn"}).find("a").text
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()") 
    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    
    print(f"{count}-film: {title.ljust(60)} yıl: {year.ljust(20)} değerlendirme: {rating}")  
    count+=1




"""""""""""
Output
1-film: The Shawshank Redemption                                     yıl: 1994                 değerlendirme: 9.2
2-film: The Godfather                                                yıl: 1972                 değerlendirme: 9.2
3-film: The Dark Knight                                              yıl: 2008                 değerlendirme: 9.0
4-film: The Godfather Part II                                        yıl: 1974                 değerlendirme: 9.0
5-film: 12 Angry Men                                                 yıl: 1957                 değerlendirme: 8.9
6-film: Schindler's List                                             yıl: 1993                 değerlendirme: 8.9
7-film: The Lord of the Rings: The Return of the King                yıl: 2003                 değerlendirme: 8.9
8-film: Pulp Fiction                                                 yıl: 1994                 değerlendirme: 8.8
9-film: The Lord of the Rings: The Fellowship of the Ring            yıl: 2001                 değerlendirme: 8.8
10-film: Il buono, il brutto, il cattivo                              yıl: 1966                 değerlendirme: 8.8
11-film: Forrest Gump                                                 yıl: 1994                 değerlendirme: 8.8
12-film: Fight Club                                                   yıl: 1999                 değerlendirme: 8.7
13-film: Inception                                                    yıl: 2010                 değerlendirme: 8.7
14-film: The Lord of the Rings: The Two Towers                        yıl: 2002                 değerlendirme: 8.7
15-film: The Empire Strikes Back                                      yıl: 1980                 değerlendirme: 8.7
16-film: The Matrix                                                   yıl: 1999                 değerlendirme: 8.7
17-film: Goodfellas                                                   yıl: 1990                 değerlendirme: 8.7
18-film: One Flew Over the Cuckoo's Nest                              yıl: 1975                 değerlendirme: 8.6
19-film: Se7en                                                        yıl: 1995                 değerlendirme: 8.6
20-film: Shichinin no samurai                                         yıl: 1954                 değerlendirme: 8.6
21-film: It's a Wonderful Life                                        yıl: 1946                 değerlendirme: 8.6
22-film: The Silence of the Lambs                                     yıl: 1991                 değerlendirme: 8.6
23-film: Cidade de Deus                                               yıl: 2002                 değerlendirme: 8.6
24-film: Saving Private Ryan                                          yıl: 1998                 değerlendirme: 8.6
25-film: La vita è bella                                              yıl: 1997                 değerlendirme: 8.6
26-film: The Green Mile                                               yıl: 1999                 değerlendirme: 8.6
27-film: Interstellar                                                 yıl: 2014                 değerlendirme: 8.6
28-film: Star Wars                                                    yıl: 1977                 değerlendirme: 8.6
29-film: Terminator 2: Judgment Day                                   yıl: 1991                 değerlendirme: 8.5
30-film: Back to the Future                                           yıl: 1985                 değerlendirme: 8.5
31-film: Sen to Chihiro no kamikakushi                                yıl: 2001                 değerlendirme: 8.5
32-film: Psycho                                                       yıl: 1960                 değerlendirme: 8.5
33-film: The Pianist                                                  yıl: 2002                 değerlendirme: 8.5
34-film: Léon                                                         yıl: 1994                 değerlendirme: 8.5
35-film: Gisaengchung                                                 yıl: 2019                 değerlendirme: 8.5
36-film: The Lion King                                                yıl: 1994                 değerlendirme: 8.5
37-film: Gladiator                                                    yıl: 2000                 değerlendirme: 8.5
38-film: American History X                                           yıl: 1998                 değerlendirme: 8.5
39-film: The Departed                                                 yıl: 2006                 değerlendirme: 8.5
40-film: The Usual Suspects                                           yıl: 1995                 değerlendirme: 8.5
41-film: The Prestige                                                 yıl: 2006                 değerlendirme: 8.5
42-film: Casablanca                                                   yıl: 1942                 değerlendirme: 8.5
43-film: Whiplash                                                     yıl: 2014                 değerlendirme: 8.5
44-film: The Intouchables                                             yıl: 2011                 değerlendirme: 8.5
45-film: Seppuku                                                      yıl: 1962                 değerlendirme: 8.5
46-film: Hotaru no haka                                               yıl: 1988                 değerlendirme: 8.5
47-film: Modern Times                                                 yıl: 1936                 değerlendirme: 8.4
48-film: Once Upon a Time in the West                                 yıl: 1968                 değerlendirme: 8.4
49-film: Rear Window                                                  yıl: 1954                 değerlendirme: 8.4
50-film: Alien                                                        yıl: 1979                 değerlendirme: 8.4
51-film: City Lights                                                  yıl: 1931                 değerlendirme: 8.4
52-film: Nuovo Cinema Paradiso                                        yıl: 1988                 değerlendirme: 8.4
53-film: Apocalypse Now                                               yıl: 1979                 değerlendirme: 8.4
54-film: Memento                                                      yıl: 2000                 değerlendirme: 8.4
55-film: Top Gun: Maverick                                            yıl: 2022                 değerlendirme: 8.4
56-film: Raiders of the Lost Ark                                      yıl: 1981                 değerlendirme: 8.4
57-film: Django Unchained                                             yıl: 2012                 değerlendirme: 8.4
58-film: WALL·E                                                       yıl: 2008                 değerlendirme: 8.4
59-film: The Lives of Others                                          yıl: 2006                 değerlendirme: 8.4
60-film: Sunset Blvd.                                                 yıl: 1950                 değerlendirme: 8.4
61-film: Paths of Glory                                               yıl: 1957                 değerlendirme: 8.4
62-film: The Shining                                                  yıl: 1980                 değerlendirme: 8.4
63-film: The Great Dictator                                           yıl: 1940                 değerlendirme: 8.4
64-film: Witness for the Prosecution                                  yıl: 1957                 değerlendirme: 8.4
65-film: Avengers: Infinity War                                       yıl: 2018                 değerlendirme: 8.4
66-film: Aliens                                                       yıl: 1986                 değerlendirme: 8.3
67-film: American Beauty                                              yıl: 1999                 değerlendirme: 8.3
68-film: Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb yıl: 1964                 değerlendirme: 8.3
69-film: Spider-Man: Into the Spider-Verse                            yıl: 2018                 değerlendirme: 8.3
70-film: The Dark Knight Rises                                        yıl: 2012                 değerlendirme: 8.3
71-film: Oldeuboi                                                     yıl: 2003                 değerlendirme: 8.3
72-film: Joker                                                        yıl: 2019                 değerlendirme: 8.3
73-film: Amadeus                                                      yıl: 1984                 değerlendirme: 8.3
74-film: Braveheart                                                   yıl: 1995                 değerlendirme: 8.3
75-film: Toy Story                                                    yıl: 1995                 değerlendirme: 8.3
76-film: Coco                                                         yıl: 2017                 değerlendirme: 8.3
77-film: Inglourious Basterds                                         yıl: 2009                 değerlendirme: 8.3
78-film: Das Boot                                                     yıl: 1981                 değerlendirme: 8.3
79-film: Mononoke-hime                                                yıl: 1997                 değerlendirme: 8.3
80-film: Avengers: Endgame                                            yıl: 2019                 değerlendirme: 8.3
81-film: Once Upon a Time in America                                  yıl: 1984                 değerlendirme: 8.3
82-film: Good Will Hunting                                            yıl: 1997                 değerlendirme: 8.3
83-film: Kimi no na wa.                                               yıl: 2016                 değerlendirme: 8.3
84-film: Requiem for a Dream                                          yıl: 2000                 değerlendirme: 8.3
85-film: Toy Story 3                                                  yıl: 2010                 değerlendirme: 8.3
86-film: Singin' in the Rain                                          yıl: 1952                 değerlendirme: 8.3
87-film: 3 Idiots                                                     yıl: 2009                 değerlendirme: 8.3
88-film: Star Wars: Episode VI - Return of the Jedi                   yıl: 1983                 değerlendirme: 8.3
89-film: Tengoku to jigoku                                            yıl: 1963                 değerlendirme: 8.3
90-film: 2001: A Space Odyssey                                        yıl: 1968                 değerlendirme: 8.3
91-film: Eternal Sunshine of the Spotless Mind                        yıl: 2004                 değerlendirme: 8.3
92-film: Reservoir Dogs                                               yıl: 1992                 değerlendirme: 8.3
93-film: Capharnaüm                                                   yıl: 2018                 değerlendirme: 8.3
94-film: Citizen Kane                                                 yıl: 1941                 değerlendirme: 8.3
95-film: Lawrence of Arabia                                           yıl: 1962                 değerlendirme: 8.3
96-film: Jagten                                                       yıl: 2012                 değerlendirme: 8.3
97-film: M - Eine Stadt sucht einen Mörder                            yıl: 1931                 değerlendirme: 8.3
98-film: North by Northwest                                           yıl: 1959                 değerlendirme: 8.3
99-film: Idi i smotri                                                 yıl: 1985                 değerlendirme: 8.2
100-film: Vertigo                                                      yıl: 1958                 değerlendirme: 8.2
101-film: Le fabuleux destin d'Amélie Poulain                          yıl: 2001                 değerlendirme: 8.2
102-film: A Clockwork Orange                                           yıl: 1971                 değerlendirme: 8.2
103-film: Double Indemnity                                             yıl: 1944                 değerlendirme: 8.2
104-film: Full Metal Jacket                                            yıl: 1987                 değerlendirme: 8.2
105-film: The Apartment                                                yıl: 1960                 değerlendirme: 8.2
106-film: Scarface                                                     yıl: 1983                 değerlendirme: 8.2
107-film: Ikiru                                                        yıl: 1952                 değerlendirme: 8.2
108-film: The Sting                                                    yıl: 1973                 değerlendirme: 8.2
109-film: To Kill a Mockingbird                                        yıl: 1962                 değerlendirme: 8.2
110-film: Taxi Driver                                                  yıl: 1976                 değerlendirme: 8.2
111-film: Heat                                                         yıl: 1995                 değerlendirme: 8.2
112-film: Up                                                           yıl: 2009                 değerlendirme: 8.2
113-film: L.A. Confidential                                            yıl: 1997                 değerlendirme: 8.2
114-film: Metropolis                                                   yıl: 1927                 değerlendirme: 8.2
115-film: Incendies                                                    yıl: 2010                 değerlendirme: 8.2
116-film: Jodaeiye Nader az Simin                                      yıl: 2011                 değerlendirme: 8.2
117-film: Die Hard                                                     yıl: 1988                 değerlendirme: 8.2
118-film: Snatch                                                       yıl: 2000                 değerlendirme: 8.2
119-film: Indiana Jones and the Last Crusade                           yıl: 1989                 değerlendirme: 8.2
120-film: Ladri di biciclette                                          yıl: 1948                 değerlendirme: 8.2
121-film: Hamilton                                                     yıl: 2020                 değerlendirme: 8.2
122-film: 1917                                                         yıl: 2019                 değerlendirme: 8.2
123-film: Taare Zameen Par                                             yıl: 2007                 değerlendirme: 8.2
124-film: Der Untergang                                                yıl: 2004                 değerlendirme: 8.2
125-film: Per qualche dollaro in più                                   yıl: 1965                 değerlendirme: 8.2
126-film: Batman Begins                                                yıl: 2005                 değerlendirme: 8.2
127-film: Dangal                                                       yıl: 2016                 değerlendirme: 8.2
128-film: The Kid                                                      yıl: 1921                 değerlendirme: 8.2
129-film: Some Like It Hot                                             yıl: 1959                 değerlendirme: 8.2
130-film: All About Eve                                                yıl: 1950                 değerlendirme: 8.2
131-film: The Father                                                   yıl: 2020                 değerlendirme: 8.2
132-film: Spider-Man: No Way Home                                      yıl: 2021                 değerlendirme: 8.2
133-film: Green Book                                                   yıl: 2018                 değerlendirme: 8.2
134-film: The Wolf of Wall Street                                      yıl: 2013                 değerlendirme: 8.2
135-film: Judgment at Nuremberg                                        yıl: 1961                 değerlendirme: 8.2
136-film: Ran                                                          yıl: 1985                 değerlendirme: 8.2
137-film: Casino                                                       yıl: 1995                 değerlendirme: 8.2
138-film: Unforgiven                                                   yıl: 1992                 değerlendirme: 8.2
139-film: Pan's Labyrinth                                              yıl: 2006                 değerlendirme: 8.2
140-film: There Will Be Blood                                          yıl: 2007                 değerlendirme: 8.2
141-film: The Sixth Sense                                              yıl: 1999                 değerlendirme: 8.2
142-film: The Truman Show                                              yıl: 1998                 değerlendirme: 8.2
143-film: A Beautiful Mind                                             yıl: 2001                 değerlendirme: 8.2
144-film: Monty Python and the Holy Grail                              yıl: 1975                 değerlendirme: 8.2
145-film: Yôjinbô                                                      yıl: 1961                 değerlendirme: 8.1
146-film: The Treasure of the Sierra Madre                             yıl: 1948                 değerlendirme: 8.1
147-film: Shutter Island                                               yıl: 2010                 değerlendirme: 8.1
148-film: Jurassic Park                                                yıl: 1993                 değerlendirme: 8.1
149-film: The Great Escape                                             yıl: 1963                 değerlendirme: 8.1
150-film: Rashômon                                                     yıl: 1950                 değerlendirme: 8.1
151-film: Kill Bill: Vol. 1                                            yıl: 2003                 değerlendirme: 8.1
152-film: No Country for Old Men                                       yıl: 2007                 değerlendirme: 8.1
153-film: Finding Nemo                                                 yıl: 2003                 değerlendirme: 8.1
154-film: The Elephant Man                                             yıl: 1980                 değerlendirme: 8.1
155-film: Chinatown                                                    yıl: 1974                 değerlendirme: 8.1
156-film: Raging Bull                                                  yıl: 1980                 değerlendirme: 8.1
157-film: The Thing                                                    yıl: 1982                 değerlendirme: 8.1
158-film: Gone with the Wind                                           yıl: 1939                 değerlendirme: 8.1
159-film: V for Vendetta                                               yıl: 2005                 değerlendirme: 8.1
160-film: Inside Out                                                   yıl: 2015                 değerlendirme: 8.1
161-film: Lock, Stock and Two Smoking Barrels                          yıl: 1998                 değerlendirme: 8.1
162-film: Dial M for Murder                                            yıl: 1954                 değerlendirme: 8.1
163-film: El secreto de sus ojos                                       yıl: 2009                 değerlendirme: 8.1
164-film: Hauru no ugoku shiro                                         yıl: 2004                 değerlendirme: 8.1
165-film: The Bridge on the River Kwai                                 yıl: 1957                 değerlendirme: 8.1
166-film: Three Billboards Outside Ebbing, Missouri                    yıl: 2017                 değerlendirme: 8.1
167-film: Trainspotting                                                yıl: 1996                 değerlendirme: 8.1
168-film: Warrior                                                      yıl: 2011                 değerlendirme: 8.1
169-film: Gran Torino                                                  yıl: 2008                 değerlendirme: 8.1
170-film: Fargo                                                        yıl: 1996                 değerlendirme: 8.1
171-film: Prisoners                                                    yıl: 2013                 değerlendirme: 8.1
172-film: Tonari no Totoro                                             yıl: 1988                 değerlendirme: 8.1
173-film: Million Dollar Baby                                          yıl: 2004                 değerlendirme: 8.1
174-film: Catch Me If You Can                                          yıl: 2002                 değerlendirme: 8.1
175-film: The Gold Rush                                                yıl: 1925                 değerlendirme: 8.1
176-film: Everything Everywhere All at Once                            yıl: 2022                 değerlendirme: 8.1
177-film: Blade Runner                                                 yıl: 1982                 değerlendirme: 8.1
178-film: On the Waterfront                                            yıl: 1954                 değerlendirme: 8.1
179-film: Bacheha-Ye aseman                                            yıl: 1997                 değerlendirme: 8.1
180-film: The Third Man                                                yıl: 1949                 değerlendirme: 8.1
181-film: Ben-Hur                                                      yıl: 1959                 değerlendirme: 8.1
182-film: Before Sunrise                                               yıl: 1995                 değerlendirme: 8.1
183-film: 12 Years a Slave                                             yıl: 2013                 değerlendirme: 8.1
184-film: Smultronstället                                              yıl: 1957                 değerlendirme: 8.1
185-film: The General                                                  yıl: 1926                 değerlendirme: 8.1
186-film: Gone Girl                                                    yıl: 2014                 değerlendirme: 8.1
187-film: Harry Potter and the Deathly Hallows: Part 2                 yıl: 2011                 değerlendirme: 8.1
188-film: The Deer Hunter                                              yıl: 1978                 değerlendirme: 8.1
189-film: In the Name of the Father                                    yıl: 1993                 değerlendirme: 8.1
190-film: The Grand Budapest Hotel                                     yıl: 2014                 değerlendirme: 8.1
191-film: Mr. Smith Goes to Washington                                 yıl: 1939                 değerlendirme: 8.1
192-film: Barry Lyndon                                                 yıl: 1975                 değerlendirme: 8.1
193-film: Le salaire de la peur                                        yıl: 1953                 değerlendirme: 8.1
194-film: Sherlock Jr.                                                 yıl: 1924                 değerlendirme: 8.1
195-film: Salinui chueok                                               yıl: 2003                 değerlendirme: 8.1
196-film: Hacksaw Ridge                                                yıl: 2016                 değerlendirme: 8.1
197-film: Klaus                                                        yıl: 2019                 değerlendirme: 8.1
198-film: Relatos salvajes                                             yıl: 2014                 değerlendirme: 8.1
199-film: Det sjunde inseglet                                          yıl: 1957                 değerlendirme: 8.1
200-film: Room                                                         yıl: 2015                 değerlendirme: 8.1
201-film: Mad Max: Fury Road                                           yıl: 2015                 değerlendirme: 8.1
202-film: How to Train Your Dragon                                     yıl: 2010                 değerlendirme: 8.1
203-film: The Big Lebowski                                             yıl: 1998                 değerlendirme: 8.1
204-film: Mary and Max.                                                yıl: 2009                 değerlendirme: 8.1
205-film: Monsters, Inc.                                               yıl: 2001                 değerlendirme: 8.1
206-film: Jaws                                                         yıl: 1975                 değerlendirme: 8.1
207-film: Tôkyô monogatari                                             yıl: 1953                 değerlendirme: 8.1
208-film: La passion de Jeanne d'Arc                                   yıl: 1928                 değerlendirme: 8.1
209-film: Dead Poets Society                                           yıl: 1989                 değerlendirme: 8.1
210-film: Hotel Rwanda                                                 yıl: 2004                 değerlendirme: 8.1
211-film: Rocky                                                        yıl: 1976                 değerlendirme: 8.0
212-film: Ford v Ferrari                                               yıl: 2019                 değerlendirme: 8.0
213-film: Platoon                                                      yıl: 1986                 değerlendirme: 8.0
214-film: Pather Panchali                                              yıl: 1955                 değerlendirme: 8.0
215-film: Stand by Me                                                  yıl: 1986                 değerlendirme: 8.0
216-film: The Terminator                                               yıl: 1984                 değerlendirme: 8.0
217-film: Spotlight                                                    yıl: 2015                 değerlendirme: 8.0
218-film: Rush                                                         yıl: 2013                 değerlendirme: 8.0
219-film: Logan                                                        yıl: 2017                 değerlendirme: 8.0
220-film: Network                                                      yıl: 1976                 değerlendirme: 8.0
221-film: Into the Wild                                                yıl: 2007                 değerlendirme: 8.0
222-film: Ratatouille                                                  yıl: 2007                 değerlendirme: 8.0
223-film: The Wizard of Oz                                             yıl: 1939                 değerlendirme: 8.0
224-film: Groundhog Day                                                yıl: 1993                 değerlendirme: 8.0
225-film: Before Sunset                                                yıl: 2004                 değerlendirme: 8.0
226-film: The Exorcist                                                 yıl: 1973                 değerlendirme: 8.0
227-film: The Best Years of Our Lives                                  yıl: 1946                 değerlendirme: 8.0
228-film: The Incredibles                                              yıl: 2004                 değerlendirme: 8.0
229-film: To Be or Not to Be                                           yıl: 1942                 değerlendirme: 8.0
230-film: La battaglia di Algeri                                       yıl: 1966                 değerlendirme: 8.0
231-film: The Grapes of Wrath                                          yıl: 1940                 değerlendirme: 8.0
232-film: Rebecca                                                      yıl: 1940                 değerlendirme: 8.0
233-film: Hachi: A Dog's Tale                                          yıl: 2009                 değerlendirme: 8.0
234-film: Cool Hand Luke                                               yıl: 1967                 değerlendirme: 8.0
235-film: Amores perros                                                yıl: 2000                 değerlendirme: 8.0
236-film: Pirates of the Caribbean: The Curse of the Black Pearl       yıl: 2003                 değerlendirme: 8.0
237-film: La haine                                                     yıl: 1995                 değerlendirme: 8.0
238-film: Les quatre cents coups                                       yıl: 1959                 değerlendirme: 8.0
239-film: Babam ve Oglum                                               yıl: 2005                 değerlendirme: 8.0
240-film: Persona                                                      yıl: 1966                 değerlendirme: 8.0
241-film: It Happened One Night                                        yıl: 1934                 değerlendirme: 8.0
242-film: Life of Brian                                                yıl: 1979                 değerlendirme: 8.0
243-film: The Sound of Music                                           yıl: 1965                 değerlendirme: 8.0
244-film: Ah-ga-ssi                                                    yıl: 2016                 değerlendirme: 8.0
245-film: Jai Bhim                                                     yıl: 2021                 değerlendirme: 8.0
246-film: Dersu Uzala                                                  yıl: 1975                 değerlendirme: 8.0
247-film: Aladdin                                                      yıl: 1992                 değerlendirme: 8.0
248-film: Gandhi                                                       yıl: 1982                 değerlendirme: 8.0
249-film: The Help                                                     yıl: 2011                 değerlendirme: 8.0
250-film: The Iron Giant                                               yıl: 1999                 değerlendirme: 8.0 
"""""""""