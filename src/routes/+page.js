const quotes = [
  "yo soy milk",
  "I wanna smash my face into the goddamn radio",
  "chocolate makes you happy",
  "bring me the head of whoever said play fair",
  "got you all in check",
  "I've come to my senses that I've become senseless",
  "mirror in the bathroom please talk free",
  "every day is like Sunday",
  "",
];

export function load() {
  return {
    quote: quotes[Math.floor(Math.random() * quotes.length)],
  };
}
