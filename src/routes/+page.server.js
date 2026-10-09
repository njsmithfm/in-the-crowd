const quotes = [
  "I wanna smash my face into the goddamn radio",
  "chocolate makes you happy",
  "bring me the head of whoever said play fair",
  "WOO-HAH!!",
  "I've come to my senses that I've become senseless",
  "mirror in the bathroom please talk free",
  "every day is like Sunday",
  "I go to Fugazi shows requesting Minor Threat songs",
  "I ride the rhythm like a Schwinn bike",
  "she's always passin me by",
  "M-E-T-H-O-D MAN",
  "let me tell you what I think about frog spit (I'm for it)",
  "na-na-na-na-na-na-na-na-na-na-na",
  "plugged in and ready to fall",
];

export function load() {
  return {
    quote: quotes[Math.floor(Math.random() * quotes.length)],
  };
}
