gutenberg_authors <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
gutenberg_languages <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
gutenberg_metadata <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
gutenberg_subjects <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')



data <- gutenberg_metadata %>%
  merge(gutenberg_authors, by = c("gutenberg_author_id", 
                                  "author")) %>%
  merge(gutenberg_languages, by = c("gutenberg_id", 
                                    "language")) %>%
  group_by(alias) %>%
  summarise(languages = n()) %>%
  arrange(-languages)
  