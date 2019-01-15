# Module 01 - Event Files - Clean and Import Data

## Import Built-in Libraries

The dataset for this project is stored in several CSV files found in the `games` folder. It represents all events that occurred in all of the MLB All-star games. We will import and clean these files in this module. 

To start, open the file called `data.py` in the `stats` folder - the rest of the tasks in this module happen in this same file.

At the top of the file create two `import` statements for `os` and `glob`. These libraries will allow us to work with a collection of files.

## Import Pandas

Import the core library that we will use throughout the project: `pandas`. 

For convenience use an `as` statement to import `pandas` as `pd`.

## Python File Management

Below the import statements create a variable called `game_files` that is set to a call to the `glob.glob()` function.

Pass the `glob` function a single argument, a call to the `os.path.join()` function.

In turn pass `os.path.join()` three arguments: `os.getcwd()`, `'games'`, and `'*.EVE'`.

## Sorting File Names

`game_files` now contains a list of all file names that end with `.EVE` in the `games` folder.

To better prepare the `game_files` list for reading into pandas, sort it in place by calling `sort()`. 

**Note: There are two sorting functions in Python. To sort in place use `list.sort()`, not `sorted(list)` which returns a new list.**

## Read CSV Files

The `game_files` list now contains a sorted list of file names i.e. `['1933AS.EVE', '1934AS.EVE', ..., '2017AS.EVE', '2018AS.EVE']`

To read each of these files into Pandas create a `for in` loop that loops through `game_files`, call the current file `game_file`

In the body of the `for in` loop use the `pd.read_csv()` function to read the current file `game_file` into a Pandas DataFrame called `game_frame`.

Now that the current `game_file` is being passed to `pd.read_csv()`, add a keyword argument to the `pd.read_csv()` call of  `names` set equal to a list with the values: `'type'`, `'multi2'`, `'multi3'`, `'multi4'`, `'multi5'`, `'multi6'`,  and `'event'`.

## Append Event Frames

Above the `for in` loop create an empty list called `event_frames`. In the body of the `for in` loop below the `pd.read_csv` call, `append` the current `event_frame` to the `event_frames` list.

## Concatenate DataFrames

Below the `for in` loop create a variable called `games` and assign it a call to the `pd.concat()` function. Pass in the list of DataFrames `game_frames`.

## Clean Values

We now have a large DataFrame called `games` that contains all of the data from all of the event files. Let's clean up some of the data so that it will not hinder our analysis. 

Use the `loc[]` function to select rows that have a value of `??` in the `multi5` column in the `games` DataFrame. Replace `??` with and empty string.

## Extract Identifiers

Each row of data should be associated with the proper `game_id`. This can be accomplished with the `extract()` function. 

Below the existing code select just the `multi2` column of the `games` DataFrame using `games['multi2']`.

Call the `extract()` function of the `str` namespace on this column. **Hint: column.str.extract().**

Pass the regular expression, `r'(.LS(\d{4})\d{5})'` to the `extract()` function.

The `extract()` function returns a DataFrame, assign this resulting DataFrame the name `identifiers`.

## Forward Fill Identifiers

The `identifiers` DataFrame now has two columns. For rows that match the regex, the row has the correct extracted values.

We need these values to be filled in for all rows on the `identifiers` DataFrame. 

To do this, call the `fillna()` function on the `identifiers` DataFrame. Provide a keyword argument to `fillna()` of `method='ffill'`.

Assign the resulting `DataFrame` back to `identifiers`.

## Rename Columns

Let's change the columns labels of the `identifiers` DataFrame. 

Below the `fillna()` function call, set the `columns` property of the `identifiers` DataFrame to a list with the values `'game_id'`, and `'year'`.

## Concatenate Identifier Columns

Use `pd.concat()` to append the columns of the `identifiers` DataFrame to the `games` DataFrame. 

This will require passing three arguments to the `pd.concat()` function. 

The first argument is the list of the DataFrames to concatenate: `[games, identifiers]`. 

The second and third arguments are the keyword arguments, `axis=1`,  and `sort=False`.

## Fill NaN Values

Fill in all `NaN` values in the `games` DataFrame with `' '` using the `fillna()` function. 

Don't forget to reassign the resulting DataFrame to `games`.

## Categorical Event Type

To slightly reduce the memory used by the games DataFrame we can provide Pandas with a clue to what data is contained in certain columns.

The `type` column of our `games` DataFrame only contains one of six values info, start, play, com, sub, and data. Pandas can optimize this column with `Categorical()`.

Select all rows and just the `type` column with the `loc()` function. **Hint: use the `:` wildcard .**
Assign this the result of `pd.Categorical()`, passing in a call to `games.loc()` with the same row and column selection.

## Print DataFrame

To ensure that the `games` DataFrame contains the correct data print the first five rows to the terminal.

**Hint: use the `head()` function.**

Finally, run the `data.py` file with this command at the terminal: `python3 stats/data.py`

---

The event files for this project are provided by [Retrosheet](http://retrosheet.org).  

As per the Retrosheet license.

The information used here was obtained
free of charge from and is copyrighted by Retrosheet.  
Interested parties may contact Retrosheet at "www.retrosheet.org".

# Module 2 - Attendance - Select and Plot Data

## Import Pandas

Let's answer the question: 'How has All-star game attendance changed over time.' 

Open `attendance.py`, which we will work in for the rest of the module, and at the top import `pandas` as `pd`.

## Import MatPlotLib

Below the pandas import, import `matplotlib.pyplot` as `plt`.

## Import `games` DataFrame

The final import should import the `games` DataFrame from `.data`.

## Select Attendance

The `games` DataFrame contains the attendance for each game. The row looks like this:

```
type multi2    multi3 ... year
info attendance  45342 ... 1946
```

We need to select all of these rows, so below the import statements, select these rows using `loc[]` with the conditions:
- `games['type'] == 'info'`
- `games['multi2'] == 'attendance'`

Select only the `year`, and `multi3` columns.

`loc[]` returns the new selection as a DataFrame. Call this new DataFrame `attendance`.

## Column Labels

The `attendance` DataFrame only has two columns now. Change the labels of these columns to `year`, and `attendance` with the `columns` property.

## Convert to Numeric

Select all rows and just the `attendance` column of the `attendance` DataFrame with the `loc[]` function. 

**Hint: dataframe.loc[:, [column1, column2]]**

Set this selection equal to a call to `pd.to_numeric()`.  

As an argument to the `pd.to_numeric()` function call, pass in the same `loc[]` selection as above.

**Hint: `selection = pd.to_numeric(selection)`**

## Plot DataFrame

Call `plot()` on the `attendance` DataFrame with the keyword arguments `x='year'`, `y='attendance'`, and `kind='bar'`.

To show the plot you will need to call `plt.show()`.

## Axis Labels

To add a bit of polish to the plot change the x and y-axis labels.

Above `plt.show()` use the `plt.xlabel()` function to add an `x-axis` label of `Year`. 

Change the `y-axis` label to `Attendance` using `plt.ylabel()`.

## Mean Line

Add code below the axis labels to draw a `dashed` `green` line perpendicular to the x-axis at the mean.

**Hint: Use the `plt.axhline()` function, the `dataframe['column'].mean()` function, and the keyword arguments of `plt.axhline()` should be: `label`, `linestyle`, and `color`.**

# Module 3 - Pitching - Group Data

## Select All Plays

Open the file called `pitching.py`, this modules file, in the `stats` folder. 

At the top, you will find that `pandas` and `matplotlib` have already been imported.

Import the `games` DataFrame from `.data`.

With access to the `games` DataFrame we can condense the data to just rows of type `play`. 

As a shortcut use `games[]` to access the DataFrame. 

In the square brackets use a conditional to test if the `type` columns value equals `'play'`. 

Store this new DataFrame in a variable called `plays`.

## Select All Strike Outs	

Now that we have a DataFrame in `pitching.py` that includes only plays called `plays`.  Let's pare it down even farther.

Select all rows of the `plays` DataFrame that contain the letter `K` in the `event` column.

**Hint: Use shortcut selection i.e. `dataframe[]` and the `dataframe['column'].str.contains()` function.**

Call this new DataFrame `strike_outs`.

## Group by Year and Game

Still in `pitching.py` group the `strike_outs` DataFrame by `year` and then `game_id`.

**Hint: `dataframe.groupby([column1, column2])`**

Chain a call to the `size()` function on this new `groupby` object. 

Reassign the result to the `strike_outs` DataFrame.

## Reset Index

`strike_outs` in `pitching.py` is now a `groupby` object, that is grouped by `year` and `game_id`. It also contains a new column that contain the number of strike outs in the game.

To convert this `groupby` object to a DataFrame and to name the column that was created use the `reset_index()` function with a keyword argument of `name='strike_outs'`. 

Reassign these set of operations to `strike_outs`.

## Apply an Operation to Multiple Columns

A frequently needed operation when working with DataFrames is to apply a function to multiple columns.

Select all rows, the `year`, and `strike_outs` columns of the `strike_outs` DataFrame with the `loc[]` function. 

Chain a call to `apply()` and pass in the function to apply `pd.to_numeric`. 

This converts the two selected columns values to numeric. 

Because `apply()` returns a new DataFrame, assign the chain `dataframe.loc[].apply()` to the same variable `strike_outs`.

## Change Plot Formatting

To plot the `strikes_outs` DataFrame in `pitching.py` call `plot()`.

In the call to plot specify the x-axis as the `year`, and the y-axis as `strike_outs`, and use a scatter plot. This is all done with keyword arguments.

Adjust the legend to say `Strike Outs` instead of  `strikes_outs` by chaining a call to the  `legend()` function on `plot()`.

Don't forget to show the plot.

# Module 4 - Offense - Reshape with Pivot

## Select All Plays

In the file called `offense.py` in the `stats` folder. You will find similar imports as the last module.

Import the `games` DataFrame from `.data`.

With access to the `games` DataFrame, select all rows that have a `type` of `play`. Use the shortcut method. **Hint: square brackets, simple boolean comparison.**

Assign this new DataFrame to a variable called `plays`. 

To make it easier to access certain columns, label them with the `columns` property: `'type'`, `'inning'`, `'team'`, `'player'`, `'count'`, `'pitches'`, `'event'`, `'game_id'`, and `'year'`.

## Select Only Hits	

The `plays` DataFrame now contains all plays from every All-star game. 

The question we want to answer in this plot is: `What is the distribution of hits across innings`.
 
For this we need just the hits, singles, doubles, triples, and home runs.  

Use `loc[]`, `str.contains()` and the regex `'^(?:S(?!B)|D|T|HR)'` to select the rows where the events column value starts with S (not SB), D, T, and HR in the `plays` DataFrame. 

Only return the `inning` and `event` columns. Assign the result DataFrame to `hits`.

## Convert Column Type

Convert the `inning` column of the `hits` DataFrame from strings to numbers using the  `pd.to_numeric()` function. **Hint: select the column with `loc[]`**

## Replace Dictionary	

The `event` column of the `hits` DataFrame now contains event information of various configurations. It contains where the ball was hit and other information that isn't needed. We will replace this with the type of hit for grouping later on. 

Create a dictionary called 
`replacements` that contains the following key value pairs

- `r'^S(.*)': 'single'`
- `r'^D(.*)': 'double'`
- `r'^T(.*)': 'triple'`
- `r'^HR(.*)': 'hr'`

## Replace Function	

Call the `replace()` function on the `hits['event']` column and pass in the `replacements` dictionary as the first parameter and` regex=True` as a keyword argument.

Assign the result which is a DataFrame to `hit_type`.

## Add A New Column

We have previously created new columns using `groupby` and concatenated DataFrames together. This time we will add a new column with `assign()`. 

Below the `replace()` function, call `assign()` on the `hits` DataFrame, pass in the keyword argument with the new column name and the new column `hit_type=hit_type`.  Reassign the new resulting DataFrame to `hits`.

## Group By Inning and Hit Type	

In one line, group the `hits` DataFrame by `inning` and `hit_type`. 

Then call `size()` to count the number of `hits`. Reset the index calling the new column `count` assign it all back to `hits`.

## Convert Hit Type to Categorical

Since there are only four types of hits let's save some memory by making `hits['hit_type']` a categorical column with  `pd.Categorical()`. 

Pass a second parameter as a list `'single', 'double', 'triple', and 'hr'`. This specifies the order.

## Sort Values

Sort the values in the `hits` DataFrame by `inning`, and `hit_type` using the `sort_values()` function. Remember to reassign this operation to `hits`.

## Reshape With Pivot

We need to reshape the `hits` DataFrame for plotting. 

Call the `pivot()` function of the `hits` DataFrame. 

To get clean results, pass the `pivot()` function three keyword arguments `index='inning'`, `columns='hit_type'`, and `values='count'`

## Stacked Bar Plot	

The most appropriate plot for our data is a stacked bar chart. To create this type of plot call `plot.bar()` with `stacked` set to True on the `hits` DataFrame.

As always, show the plot.
 
# Module 5 - Defensive Efficiency Ratio - Merge Data

## Import Existing DataFrames

In this module we will answer the question: 'What is the DER by league since 1978.'

Open `defense.py` and keep it open for the duration of the module. Pandas and Matplotlib have been imported.

For this module there are three DataFrames that have been prepared: `games`, `info` and `events`. Import them from `.frames`.

## Query Function	

After the import statements use the `query()` function to select all rows of the `games` DataFrame that have a `type` of `play` but do not have `NP` as an `event`. 

Save the resulting DataFrame as `plays`.

## Column Labels

Adjust the columns labels of the `plays` DataFrame so they match these values: `'type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year'`.

## Shift DataFrame

There are some spots in the event data where there are consecutive rows that represent the same at bat. 

To calculate plate appearances which is a factor of DER these need to be removed. 

To remove these consecutive rows it is best to use the `shift()` function. The `shift()` function moves the index a specified amount up or down. 

To select all rows that do not match either other in the player column use `plays['player'].shift() != plays['player']` in a `loc[]` function. 

Also refine the columns to `year`, `game_id`, `inning`, `team`, `player`. The resulting DataFrame should be called `pa`.

## Group Plate Appearances

We need to then calculate the plate appearances for each team for each game.

Below the `pa` DataFrame  use a `groupby()` function to group the `pa` DataFrame by `year`, `game_id`, and `team`. 

As usual we will use the `size()` function to count the plate appearances. 

Chain a call to `reset_index()` after `size()`, passing in the right keyword argument to name the column for plate appearances, `PA`.

## Unstack the DataFrame

In order to calculate the DER of a team we need to reshape the data by the type of event that happened at each plate appearance. The event types need to be the columns of our DataFrame. The `unstack()` function is perfect for this. 

Before we `unstack()` the index needs to be adjust. 

Set the index of the `events` DataFrame to four columns, `year`, `game_id`, `team`, and `event_type` with the `set_index()` function. 

Make sure you reassign the resulting DataFrame to `events`.

Then, call `unstack()` on the `events` DataFrame, also chaining two more calls to `fillna(0)` and `reset_index()`. 

`reset_index()` returns a DataFrame so reassign it to `events`.

## Manage Column Labels

After we `unstack()` our `events` DataFrame it will have multiple levels of column labels use `droplevel()` to remove one level. 

`droplevel()` needs to be called on `events.columns` and then re-assigned to `events.columns`.

Next, change the `events` DataFrame column labels to `'year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', and 'SO'`.

Lastly, remove the label of the index using `rename_axis()`. Pass in a label of `None` and make sure it is on the columns axis. This operation returns a new DataFrame so save it to `events`.

## Merge - Plate Appearances

We now have two DataFrames that have similar columns. The `pa` DataFrame has `year`, `game_id`, `team` and `PA`.  

The `events` DataFrame has `year`, `game_id`, and `team` as well as a column for every `event_type`. For convenience lets merge them together with `pd.merge()`. 

As the first two arguments `pd.merge()` requires the two DataFrames to merge, in our case `events` and `pa`.  

The are, several other keyword arguments that can be used with `pd.merge()`. 

In our case, we will use `how` set to `outer`, and both `left_on` and `right_on` set to a list of columns to merge on, `year`, `game_id`, and `team`.  

Like many Pandas functions `pd.merge()` returns a DataFrame, save this one as `events_plus_pa`.

## Merge - Team

`events_plus_pa` contains almost all of the information we need to calculate the DER of each All-star team. 

The final piece needed is which league was the home team and which was the visiting team. 

The `info` DataFrame that was imported from `frames` has already been prepared with the necessary columns and configuration. 

We can do a straight across merge between `events_plus_pa` and `info` to add the correct team.

Call `pd.merge()` only passing in the two DataFrames to merge. Save the result as `defense`.

## Calculate DER

Below the `pd.merge()` call calculate the DER of each team. 

Add a new column to the `defense` DataFrame with `defense.loc[:, 'DER']`

Set this equal to the calculation: 1 - ((H + ROE) / (PA - BB - SO - HBP - HR)), pulling each of these as a column from the `defense` DataFrame.

Convert the `year` column of the `defense` DataFrame to numeric values with `loc[]` and `pd.to_numeric()`.

## Reshape With Pivot

We are only going to plot the DER of the All-star teams in the last 40 years. 

Select these rows of our `defense` DataFrame with `loc[]` and a condition of `defense['year'] >=  1978`. Keep in mind we only need the `year`, `defense`, and `DER` columns.  Assign the resulting DataFrame to `der`.

Call `pivot`on `der` to adjust the data for potting. Use the keyword arguments `index`, `columns` and `values` in pivot with the correct column labels.

## Plot Formatting - `xticks`

For the DER plot, we will use the default line plot type. 

Call plot on `der` with a few keyword arguments `x_compat` set to `True`, `xticks` set to a `range(1978, 2018, 4)` and rotate the labels by 45 degrees with `rot=45`. 

Show the `der` plot with `plt.show()`.