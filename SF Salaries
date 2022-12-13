{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "TcIKaLLLXyT8"
   },
   "source": [
    "# Week 1 Exercise: SF Salaries \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "weALGKXgXyUC"
   },
   "source": [
    "### Step 1: Import libraries: pandas and seaborn\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "sJWsYyHuXyUD"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hURqqDR8XyUE"
   },
   "source": [
    "### Step 2: Read Data\n",
    "\n",
    "##### code for reference\n",
    "\n",
    "#### If you are using Jupyter notebook:\n",
    "first save the salaries.csv to your local folder:\n",
    "\n",
    "sal = pd.read_csv(\"`your path here`/salaries.csv\")\n",
    "\n",
    "#### If you are using google colab, please mount your Google Drive on your runtime using an authorization code:\n",
    "from google.colab import drive\n",
    "\n",
    "drive.mount('/content/drive')\n",
    "\n",
    "path = '/content/drive/`your path here`/salaries.csv'\n",
    "\n",
    "sal = pd.read_csv(path)\n",
    "\n",
    "\n",
    "\n",
    "#### Feel free to use any other prefered IDEs for python.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "YQbbt33cXyUF"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\apere\\AppData\\Local\\Temp\\ipykernel_9248\\1829207488.py:1: DtypeWarning: Columns (11) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  sal = pd.read_csv('C:/Users/apere/OneDrive/Desktop/CIS 508/Salaries.csv')\n"
     ]
    }
   ],
   "source": [
    "sal = pd.read_csv('C:/Users/apere/OneDrive/Desktop/CIS 508/Salaries.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "QbZOmZ7oXyUF"
   },
   "source": [
    "### Step 3: Follow the instructions below and answer questions.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "jR72saJZhCGc"
   },
   "source": [
    "**Check the head of the DataFrame**\n",
    "##### code for reference:\n",
    "sal.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "YZS1s2JoXyUG",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>EmployeeName</th>\n",
       "      <th>JobTitle</th>\n",
       "      <th>BasePay</th>\n",
       "      <th>OvertimePay</th>\n",
       "      <th>OtherPay</th>\n",
       "      <th>Benefits</th>\n",
       "      <th>TotalPay</th>\n",
       "      <th>TotalPayBenefits</th>\n",
       "      <th>Year</th>\n",
       "      <th>Agency</th>\n",
       "      <th>Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>NATHANIEL FORD</td>\n",
       "      <td>GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY</td>\n",
       "      <td>167411.18</td>\n",
       "      <td>0.00</td>\n",
       "      <td>400184.25</td>\n",
       "      <td>NaN</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>GARY JIMENEZ</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>155966.02</td>\n",
       "      <td>245131.88</td>\n",
       "      <td>137811.38</td>\n",
       "      <td>NaN</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>ALBERT PARDINI</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>212739.13</td>\n",
       "      <td>106088.18</td>\n",
       "      <td>16452.60</td>\n",
       "      <td>NaN</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>CHRISTOPHER CHONG</td>\n",
       "      <td>WIRE ROPE CABLE MAINTENANCE MECHANIC</td>\n",
       "      <td>77916.00</td>\n",
       "      <td>56120.71</td>\n",
       "      <td>198306.90</td>\n",
       "      <td>NaN</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>PATRICK GARDNER</td>\n",
       "      <td>DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)</td>\n",
       "      <td>134401.60</td>\n",
       "      <td>9737.00</td>\n",
       "      <td>182234.59</td>\n",
       "      <td>NaN</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Id       EmployeeName                                        JobTitle  \\\n",
       "0   1     NATHANIEL FORD  GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY   \n",
       "1   2       GARY JIMENEZ                 CAPTAIN III (POLICE DEPARTMENT)   \n",
       "2   3     ALBERT PARDINI                 CAPTAIN III (POLICE DEPARTMENT)   \n",
       "3   4  CHRISTOPHER CHONG            WIRE ROPE CABLE MAINTENANCE MECHANIC   \n",
       "4   5    PATRICK GARDNER    DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)   \n",
       "\n",
       "     BasePay  OvertimePay   OtherPay  Benefits   TotalPay  TotalPayBenefits  \\\n",
       "0  167411.18         0.00  400184.25       NaN  567595.43         567595.43   \n",
       "1  155966.02    245131.88  137811.38       NaN  538909.28         538909.28   \n",
       "2  212739.13    106088.18   16452.60       NaN  335279.91         335279.91   \n",
       "3   77916.00     56120.71  198306.90       NaN  332343.61         332343.61   \n",
       "4  134401.60      9737.00  182234.59       NaN  326373.19         326373.19   \n",
       "\n",
       "   Year         Agency Status  \n",
       "0  2011  San Francisco    NaN  \n",
       "1  2011  San Francisco    NaN  \n",
       "2  2011  San Francisco    NaN  \n",
       "3  2011  San Francisco    NaN  \n",
       "4  2011  San Francisco    NaN  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "XQFBzsh2Lkpb"
   },
   "source": [
    "**Q1: How many columns and rows are there in the dataset?** \n",
    "\n",
    "##### code for reference:\n",
    "sal.shape\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "5BI-YkCQLlhb"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(148654, 12)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "9WFbJi3LXyUI"
   },
   "source": [
    "**Q2: What the average of total pay ['TotalPay'] of San Francisco’s city employees?**\n",
    "\n",
    "##### code for reference:\n",
    "You can either use:\n",
    "\n",
    "sal.desribe() or \n",
    "\n",
    "sal[\"TotalPay\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "g02CInrZXyUI"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74768.321971703"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal[\"TotalPay\"].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LmDMpshKXyUK"
   },
   "source": [
    "\n",
    "\n",
    "\n",
    "**Q3: What is the maximum benefit received by a city employee?** \n",
    "\n",
    "##### code for reference:\n",
    "\n",
    "sal.desribe()  or \n",
    "\n",
    "sal['Benefits'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "1LnJ5W5kXyUL"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "567595.43"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal['TotalPay'].max()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JNK1N0z4XyUN"
   },
   "source": [
    "**Q4: How much benefits did JOSEPH DRISCOLL receive?** (Hint: Use 'TotalPayBenefits' variable)\n",
    "\n",
    "##### code for reference:\n",
    "sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "X3YgXGJHXyUN"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24    270324.91\n",
       "Name: TotalPayBenefits, dtype: float64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "pYKBxtlwIXLg"
   },
   "source": [
    "**Q5: What is the average ’total benefits’ received by Special Nurse?**\n",
    "\n",
    "##### code for reference\n",
    "sal[sal['JobTitle']=='Special Nurse']['TotalPayBenefits'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "2u0VW7n-Ih8C"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36372.276962861666"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal[sal['JobTitle']=='Special Nurse']['TotalPayBenefits'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "91vkh77HMIcL"
   },
   "source": [
    "**Q6: What is the name of the employee in the 3500th record?**\n",
    "\n",
    "##### code for reference\n",
    "sal.iloc[ ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "5_RMEkPFhCGk"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>EmployeeName</th>\n",
       "      <th>JobTitle</th>\n",
       "      <th>BasePay</th>\n",
       "      <th>OvertimePay</th>\n",
       "      <th>OtherPay</th>\n",
       "      <th>Benefits</th>\n",
       "      <th>TotalPay</th>\n",
       "      <th>TotalPayBenefits</th>\n",
       "      <th>Year</th>\n",
       "      <th>Agency</th>\n",
       "      <th>Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>NATHANIEL FORD</td>\n",
       "      <td>GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY</td>\n",
       "      <td>167411.18</td>\n",
       "      <td>0.00</td>\n",
       "      <td>400184.25</td>\n",
       "      <td>NaN</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>GARY JIMENEZ</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>155966.02</td>\n",
       "      <td>245131.88</td>\n",
       "      <td>137811.38</td>\n",
       "      <td>NaN</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>ALBERT PARDINI</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>212739.13</td>\n",
       "      <td>106088.18</td>\n",
       "      <td>16452.60</td>\n",
       "      <td>NaN</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>CHRISTOPHER CHONG</td>\n",
       "      <td>WIRE ROPE CABLE MAINTENANCE MECHANIC</td>\n",
       "      <td>77916.00</td>\n",
       "      <td>56120.71</td>\n",
       "      <td>198306.90</td>\n",
       "      <td>NaN</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>PATRICK GARDNER</td>\n",
       "      <td>DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)</td>\n",
       "      <td>134401.60</td>\n",
       "      <td>9737.00</td>\n",
       "      <td>182234.59</td>\n",
       "      <td>NaN</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3495</th>\n",
       "      <td>3496</td>\n",
       "      <td>TIMOTHY LIPPS</td>\n",
       "      <td>TRANSIT POWER LINE WORKER SUPERVISOR II</td>\n",
       "      <td>107916.00</td>\n",
       "      <td>25657.52</td>\n",
       "      <td>2233.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135806.52</td>\n",
       "      <td>135806.52</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3496</th>\n",
       "      <td>3497</td>\n",
       "      <td>GARY ALTENBERG</td>\n",
       "      <td>FIREFIGHTER</td>\n",
       "      <td>123028.00</td>\n",
       "      <td>5065.76</td>\n",
       "      <td>7691.20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135784.96</td>\n",
       "      <td>135784.96</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3497</th>\n",
       "      <td>3498</td>\n",
       "      <td>DANIEL EVERSON</td>\n",
       "      <td>INSPECTOR III, (POLICE DEPARTMENT)</td>\n",
       "      <td>130481.58</td>\n",
       "      <td>489.89</td>\n",
       "      <td>4812.88</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135784.35</td>\n",
       "      <td>135784.35</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3498</th>\n",
       "      <td>3499</td>\n",
       "      <td>LAWRENCE LAU</td>\n",
       "      <td>MAINTENANCE MACHINIST</td>\n",
       "      <td>74651.50</td>\n",
       "      <td>56722.22</td>\n",
       "      <td>4390.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135763.72</td>\n",
       "      <td>135763.72</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3499</th>\n",
       "      <td>3500</td>\n",
       "      <td>DANNY LOPEZ</td>\n",
       "      <td>SERGEANT III (POLICE DEPARTMENT)</td>\n",
       "      <td>130457.64</td>\n",
       "      <td>943.62</td>\n",
       "      <td>4340.11</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135741.37</td>\n",
       "      <td>135741.37</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3500 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        Id       EmployeeName                                        JobTitle  \\\n",
       "0        1     NATHANIEL FORD  GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY   \n",
       "1        2       GARY JIMENEZ                 CAPTAIN III (POLICE DEPARTMENT)   \n",
       "2        3     ALBERT PARDINI                 CAPTAIN III (POLICE DEPARTMENT)   \n",
       "3        4  CHRISTOPHER CHONG            WIRE ROPE CABLE MAINTENANCE MECHANIC   \n",
       "4        5    PATRICK GARDNER    DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)   \n",
       "...    ...                ...                                             ...   \n",
       "3495  3496      TIMOTHY LIPPS         TRANSIT POWER LINE WORKER SUPERVISOR II   \n",
       "3496  3497     GARY ALTENBERG                                     FIREFIGHTER   \n",
       "3497  3498     DANIEL EVERSON              INSPECTOR III, (POLICE DEPARTMENT)   \n",
       "3498  3499       LAWRENCE LAU                           MAINTENANCE MACHINIST   \n",
       "3499  3500        DANNY LOPEZ                SERGEANT III (POLICE DEPARTMENT)   \n",
       "\n",
       "        BasePay  OvertimePay   OtherPay  Benefits   TotalPay  \\\n",
       "0     167411.18         0.00  400184.25       NaN  567595.43   \n",
       "1     155966.02    245131.88  137811.38       NaN  538909.28   \n",
       "2     212739.13    106088.18   16452.60       NaN  335279.91   \n",
       "3      77916.00     56120.71  198306.90       NaN  332343.61   \n",
       "4     134401.60      9737.00  182234.59       NaN  326373.19   \n",
       "...         ...          ...        ...       ...        ...   \n",
       "3495  107916.00     25657.52    2233.00       NaN  135806.52   \n",
       "3496  123028.00      5065.76    7691.20       NaN  135784.96   \n",
       "3497  130481.58       489.89    4812.88       NaN  135784.35   \n",
       "3498   74651.50     56722.22    4390.00       NaN  135763.72   \n",
       "3499  130457.64       943.62    4340.11       NaN  135741.37   \n",
       "\n",
       "      TotalPayBenefits  Year         Agency Status  \n",
       "0            567595.43  2011  San Francisco    NaN  \n",
       "1            538909.28  2011  San Francisco    NaN  \n",
       "2            335279.91  2011  San Francisco    NaN  \n",
       "3            332343.61  2011  San Francisco    NaN  \n",
       "4            326373.19  2011  San Francisco    NaN  \n",
       "...                ...   ...            ...    ...  \n",
       "3495         135806.52  2011  San Francisco    NaN  \n",
       "3496         135784.96  2011  San Francisco    NaN  \n",
       "3497         135784.35  2011  San Francisco    NaN  \n",
       "3498         135763.72  2011  San Francisco    NaN  \n",
       "3499         135741.37  2011  San Francisco    NaN  \n",
       "\n",
       "[3500 rows x 12 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal.iloc[:3500]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "g9cB-Uy3hCGk"
   },
   "source": [
    "**Q7: How many missing values does variable 'BasePay' have?** \n",
    "\n",
    "##### code for reference\n",
    "\n",
    "sal.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "id": "V1m_9lbmhCGk"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Id                       0\n",
       "EmployeeName             6\n",
       "JobTitle                 4\n",
       "BasePay                609\n",
       "OvertimePay              4\n",
       "OtherPay                 4\n",
       "Benefits             36163\n",
       "TotalPay                 0\n",
       "TotalPayBenefits         0\n",
       "Year                     0\n",
       "Agency                   0\n",
       "Status              110535\n",
       "dtype: int64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5ijNpll4hCGk"
   },
   "source": [
    "**Q8: Create a boxplot of TotalPay variable across different job status (Status). Which of the following statements is NOT true?** \n",
    "\n",
    "##### code for reference\n",
    "sns.boxplot(x=,y=,data=)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "id": "1eQP2R0MhCGk"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Status', ylabel='TotalPay'>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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adq0abY2B4SiM7e0effdd4PCVWRkpIYPH84tbYAQFhsb26pxhL8WBas//OEPev3111VbW6sbbrhBd911l0aPHq3Ro0e3VX9AyOGWNgDQeTV7KfA3v/mNZs6cqd27d+ujjz7SPffco8WLF7dlb0DI4pY2QHhiuwU0pdnB6qmnntKDDz6ojz76SO+9956ef/55rV69ui17A0LarFmz1KdPH0niljZAmGhqWyG2HUKzg9Wnn36q73//+9bztLQ0VVdXq7S0tE0aA0Idt7QBws/FF1/cqnGEv2afY1VVVaUePXpYzyMjI+V2u/Xll1+2SWNAOBg3bpzGjRvndBsAbHL06NFWjSP8tejk9eeeey4oXJ06dUpr1qwJugpi3rx59nUHhLjnn39e69at06xZs3TnnXc63Q4AoI25TDN3KxwwYECTVzO5XC59+umntjQWriorK+X1euX3+xUTE+N0O2hDx44d080336z6+npFRETotdde00UXXeR0WwBa4cUXX9Svf/3rRsfvvvtuffe7323HjtBemvv7u9kzVgcPHrSjL6DTeOihh1RfXy9Jqq+v18MPP6xf/vKXDncFoDV27drV5DjBqnNr8c7rAJq2e/du7du3L+jY+++/r927dzvUEQA7cPI6mtKsGauW/JXNOVbo7Orr67V06dIGx5YuXarXX39dERH8TQOEosrKylaNI/w1K1itWrWqWe/M5XIRrNDp7dy5s9EfrpWVldq5c6fGjh3bzl0BsENTV8JzpTyaFawOHDjQ1n0AYWPUqFGKjIw85ybM0ultSkaNGuVAVwCA9sB6BGCz4uLiBkOVJNXV1am4uLidOwJgl+ZcHY/OrUX7WJ1RXFysN954Q4WFhaqpqQkay8zMtKUxIFQlJSVp5MiRysvLO2ds1KhRSkpKcqArAHaora1t1TjCX4uD1ebNmzVt2jQNHDhQH330kZKTk3Xw4EEZYzRs2LC26BEIKS6XS/Pnz9dtt912ztj8+fP5ixYIYdXV1a0aR/hr8VLg4sWLtXDhQhUUFMjj8ejVV19VUVGRUlJS9J3vfKctegTCRjP34wXQQXFLGzSlxcHqb3/7m26//XZJUpcuXax7CC5dulSPP/647Q0CocYY0+j3wuOPP064AkJYU0v5LPWjxcGqe/fu1lSnz+fT3//+d2vs888/t68zIEQdOnTonM1Bz9i3b58O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1dXVfH+DpUCgLURHR6u2ttbpNgAA7YxgBdhs165dysrK0vXXX+90KwBs8qc//Uk9evSwHt/5znecbgkdFEuBgA3O/NA9deqUamtrddNNN+mpp55yui0ANrnuuuv0zDPPWM+7d+/uYDfoyAhWgA3O/NDt2rWrfD6funbt6nRLAGzUvXt3DRo0yOk2EAIIVoAN+KELAJA4xwoAAMA2BCsAAACbuIwxxukmAAAAwgEzVgAAADYhWAEAANiEYAUAAGATghUAAIBNCFYAAAA2IVgBAADYhGAFAABgE4IVAACATQhWAAAANiFYAei0ysrKdPfddyspKUlut1vx8fGaOHGiduzYIUlyuVx6/fXXW/x+BwwYoCeeeMLeZgGEhC5ONwAATrnllltUW1ur3/3ud7r00kt19OhRbd68WV988YXTrQEIUcxYAeiUjh07pm3btunxxx/Xddddp/79+2vUqFFavHixJk+erAEDBkiSpk+fLpfLZT3/+9//rptuuklxcXHq0aOHRo4cqb/85S/W+7322mt16NAh3X///XK5XHK5XJKkJUuW6J//+Z+DenjiiSes9ytJb7/9tkaNGqXu3bvroosu0tVXX61Dhw615acBgM0IVgA6pR49eqhHjx56/fXXVV1dfc54Xl6eJOmFF15QSUmJ9fzEiRP613/9V/3lL3/R3r17NXHiRE2dOlWFhYWSpNdee00JCQlaunSpSkpKVFJS0qx+Tp06pW9/+9tKSUnR+++/rx07duiuu+6yghmA0MBSIIBOqUuXLlqzZo3S09P17LPPatiwYUpJSdGtt96qq666ShdffLEk6aKLLlJ8fLz1dkOHDtXQoUOt5//xH/+h9evX64033tCcOXPUu3dvRUZGqmfPnkFv15TKykr5/X5NmTJFX/va1yRJV155pU2vFkB7YcYKQKd1yy236MiRI3rjjTc0ceJEvf322xo2bJjWrFnT6NucPHlSDzzwgAYPHqyLLrpIPXr00IcffmjNWF2o3r17a/bs2dYM2JNPPtns2S4AHQfBCkCn5vF4NH78eD388MPavn27Zs+erUceeaTR+h/96Ed69dVX9bOf/UzvvPOO8vPzNWTIENXU1Jz340RERMgYE3SstrY26PkLL7ygHTt2aNy4cXrppZd0+eWXKzc398JfHIB2R7ACgK8YPHiwTp48KUnq2rWr6urqgsbfeecdzZ49W9OnT9eQIUMUHx+vgwcPBtVERUWd83YXX3yxSktLg8JVfn7+OR//G9/4hhYvXqzt27crOTlZWVlZ9rwwAO2CYAWgUyovL9e3vvUtrV27Vu+//74OHDigP/zhD1qxYoVuuukmSaf3o9q8ebNKS0tVUVEhSRo0aJBee+015efn67333lNqaqrq6+uD3veAAQO0detWHT58WJ9//rmk01cLfvbZZ1qxYoX+/ve/61e/+pU2bNhgvc2BAwe0ePFi7dixQ4cOHVJOTo4+/vhjzrMCQgzBCkCn1KNHD40ePVqrVq3SN7/5TSUnJ+uhhx5Senq6Vq9eLUn6xS9+oU2bNikxMVHf+MY3JEmrVq1Sr169NG7cOE2dOlUTJ07UsGHDgt730qVLdfDgQX3ta1+zToK/8sor9fTTT+tXv/qVhg4dql27dmnRokXW23Tr1k0ffvihbrnlFl1++eW66667NGfOHN19993t9BkBYAeXOXvRHwAAABeEGSsAAACbEKwAAABsQrACAACwCcEKAADAJgQrAAAAmxCsAAAAbEKwAgAAsAnBCgAAwCYEKwAAAJsQrAAAAGxCsAIAALDJ/wfqJh5EVkgl5gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Status',y='TotalPay',data=sal)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "kNVh3TzfhCGl"
   },
   "source": [
    "**Q9: Create a boxplot of BasePay variable across different years (Year variable). Which of the following statement is NOT true?** \n",
    "##### code for reference \n",
    "sns.boxplot(x=,y=,data=)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "id": "3SSgEYnNhCGl"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Year', ylabel='BasePay'>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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OKS5vcRWrVol22MSETmSLhVWVVVVN5w75ePjgwULFnQpKSJSrldeeQV/+ctfxNt//etf7ZgNEZFtdamwur6ounr1KhobG03inJSsHHIODZ06dQp//OMfLcbfeecd3HrrrZI+JoeG7O++++4Tf/fy8jLbg0VE5Ky6VFhduXIFL730Ej7++GPU1ta2iTc3N1udGNmGnENDd911l1VxUr5t27bZOwUiIpvq0gKhc+bMwe7du/H2229DrVbjn//8J1599VVotVqsX79e6hxJwfbt29ep40RERErWpcJq27ZtePvtt/HYY4/Bw8MD999/P/7v//4Pixcv5l5R1Ea/fv1Mbt955512yoSIiEheXSqsLly4gMjISADX5lNduHABwLW5FeyJoNb+/ve/m9xes2aNnTIhIiKSV5cKq1tvvRVlZWUAgP79++Pjjz8GcK0n6/q1rIhak3MNJSIiInvrUmH1+9//Hv/5z38AAHPnzhXnWr344ov405/+JGmCRERERErRpasCX3zxRfH3kSNH4vvvv8eRI0dw22234e6775YsOSIiIiIl6VRhZTQasXz5cnz22WdobGzEqFGjMH/+fERERCAiIkKuHImIiIgUoVNDgW+88Qb+/Oc/w8/PDz179sSKFSswY8YMuXIjIiIiUpROFVbr1q3DqlWrkJOTg61bt+Kzzz7D+vXrIQiCXPkRERERKUanCqvTp08jISFBvB0fHw9BEHD27FnJEyMiIiJSmk4VVgaDwWT7E5VKBS8vL+j1eskTIyIiIlKaTl8V+Morr5hswmwwGLBo0SJoNBrx2IoVK6TJjoiIiEhBOlVYPfDAAzhx4oTJsWHDhuHUqVPibZVKJU1mRERERArTqcLq66+/likNIiIiIuXr0srrLQwGA06cOIGmpiap8iEiIiJSrC4VVj///DOmTJkCX19f3HXXXSgvLwcAzJgxA6+//rqkCRIREREpRZcKq7lz5+I///kPvv76a3h7e4vHR40ahU2bNkmWHBEREZGSdGmvwM8++wybNm3C0KFDTSar9+/fHz/++KNkyREREREpSZd6rM6fP4/g4OA2x69cucKrAomIiMhldamwGjx4MLZv3y7ebimm3n//fcTExEiTGREREZHCdGkocMmSJRgzZgyOHz+OpqYm/O1vf8O3336LvLw87N27V+ociYiIiBShSz1Ww4YNw4ED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+HD4+PggOTkZy5YtE9toNBrk5uZi2rRpGDRoEAIDA5Geni7mTERERKQSBC4dbkv19fXQaDTQ6XRib5izu3r1qvhNjVfcWOZMQwUt32S3bt0Kb29vO2dkHbkuv7/+fdH8sILnWDmDJsB9y7Uv43L9jbr+fL8EwEvyR7ANAUDj/373hDKn1BkAvPG/3ztzvjv6+c23sgNzpg9ac78rlVwftBwqcEz8MkBS8wLgpciS5BrlX44lb38SCysHxg9ax8QPWiIisoSFFZED+scDF6F2V+YovSAABuO1373cACVe26FvVmHavpvsnQYRKRALK4W4cs8kwE2hp0sQAGPTtd/dPJT5SWtsgt83mTZ7OLW7AG8FL6uj/P48ZRa1RGR/Cv2kdkFuHoC7kheLUepUTSIioo5z+C1tiIiIiJSChRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRDzsnQARkSsSBOGXG032y4Ng8vqbnBeiLmBhRURkB3q9XvzdfZu7HTOh6+n1evj6+to7DVIwFlZEREQyu74nzHDtiL1ScXmG636Xo4eShRWRg7j+Da5vtmMiZPL6yzU0pFarxd+bE5v519iemn7pNbz+vEjp+h7KN2R5BOoKOXoo+VYmchDX/+Gdti/QjpnQ9eQaGlKpVL/c8AD/GjsIk/NC1AV8Kzswk2/KzY32S4RMXn9ObiWizrq+J+wlAF72S8XlGfBLr6EcPZQsrBzY9T0Yfkc32jETup5cPRjXv8H/8UAd1JzPbDf65l96DeUaGiLXcn1PmBcAL7BnzH5++XIsRw8lCysiB3H9G1ztDnizsHIIHBoios5gYeXArv+mfOXXyYC7px2zcXHNjWKvIXswiIjIEhZWDszkm7K7JwsrB8EeDCIisoRb2hARERFJhIUVERERkURYWBERERFJhIUVERERkURYWBERERFJhIUVERERkURYWBERERFJxKELq4ULF0KlUpn8hIaGinFBELBw4UJotVr4+PhgxIgR+Pbbb03uQ6/XY/r06QgKCoKfnx+SkpJQWVlp0qaurg4pKSnQaDTQaDRISUnBxYsXTdqUl5cjMTERfn5+CAoKwowZM2AwGGR77kRERKQ8Dl1YAcBdd92Fqqoq8ae4uFiMLV26FCtWrMDq1atRUFCA0NBQjB49GpcuXRLbzJw5E1u2bEFWVhb279+Py5cvIyEhAc3NzWKb5ORkFBUVITs7G9nZ2SgqKkJKSooYb25uxrhx43DlyhXs378fWVlZ2Lx5M2bNmmWbF4GIiIgUweFXXvfw8DDppWohCALeeustvPzyy3jkkUcAAB9++CFCQkKwceNGPPvss9DpdPjggw+wYcMGjBo1CgCQkZGB8PBwfPXVV4iPj8d3332H7Oxs5OfnY8iQIQCA999/HzExMThx4gT69euHnJwcHD9+HBUVFdBqtQCA5cuXIzU1FYsWLUJAQIDF/PV6vclmyvX19ZK9NkRERORYHL7H6ocffoBWq0VkZCR+97vf4dSpUwCA0tJSVFdXIy4uTmyrVqsRGxuLgwcPAgAKCwvR2Nho0kar1SIqKkpsk5eXB41GIxZVADB06FBoNBqTNlFRUWJRBQDx8fHQ6/UoLCxsN/8lS5aIQ4wajQbh4eFWviJERETkqBy6sBoyZAjWr1+PnTt34v3330d1dTWGDRuG2tpaVFdXAwBCQkJM/k1ISIgYq66uhpeXFwIDA9ttExwc3Oaxg4ODTdq0fpzAwEB4eXmJbSyZO3cudDqd+FNRUdGJV4CIiIiUxKGHAseOHSv+Hh0djZiYGNx222348MMPMXToUABtN8QVBOGGm+S2bmOufVfamKNWq6FWq9ttQ0RERM7BoXusWvPz80N0dDR++OEHcd5V6x6jmpoasXcpNDQUBoMBdXV17bY5d+5cm8c6f/68SZvWj1NXV4fGxsY2PVlERETkuhRVWOn1enz33Xfo2bMnIiMjERoaitzcXDFuMBiwd+9eDBs2DAAwcOBAeHp6mrSpqqpCSUmJ2CYmJgY6nQ6HDx8W2xw6dAg6nc6kTUlJCaqqqsQ2OTk5UKvVGDhwoKzPmYiIiJTDoYcCZ8+ejcTERERERKCmpgZ//etfUV9fj8mTJ0OlUmHmzJlYvHgx+vTpgz59+mDx4sXw9fVFcnIyAECj0WDKlCmYNWsWevToge7du2P27NmIjo4WrxK88847MWbMGKSlpWHNmjUAgGeeeQYJCQno168fACAuLg79+/dHSkoK3nzzTVy4cAGzZ89GWlpau1cEEhERkWtx6MKqsrISEydOxE8//YSbb74ZQ4cORX5+Pnr16gUAmDNnDq5evYqpU6eirq4OQ4YMQU5ODvz9/cX7WLlyJTw8PDBhwgRcvXoVDz74INatWwd3d3exTWZmJmbMmCFePZiUlITVq1eLcXd3d2zfvh1Tp07F8OHD4ePjg+TkZCxbtsxGrwQREREpgUMXVllZWe3GVSoVFi5ciIULF1ps4+3tjVWrVmHVqlUW23Tv3h0ZGRntPlZERAS++OKLdtsQERGRa1PUHCsiIiIiR8bCioiIiEgiLKyIiIiIJMLCioiIiEgiDj15nYjIJTTZOwErCACa//e7O4D2N6NwTEp+/cnhsLAiIrIz923uN25ERIrAoUAiIiIiibDHisgB6ZtVuDbGojyCABiM1373cgNusE+5Q7r2+svL29sbO3fulP1x5NbQ0ICHHnoIALB161Z4e3vbOSPrKD1/sj8WVkphVPAkAEH4JX83D2V+0tr49Z+27yabPh7Znkqlgo+Pj73TkJS3t7fTPSeizmJhpRB+32TaOwUiIiK6ARZWRA6CQ0OOSen5E5FtsbByYPygdUxy5c+hISLXYACg2DmUABr/97snlLm6hkHm+2dh5cD4QUtE5HzesHcCJCsut0BEREQkEfZYERERyYxTOxyTHPmzsCIiIpIZp3a4Dg4FEhEREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhRURERGRRFhYEREREUmEhVUXvP3224iMjIS3tzcGDhyIf//73/ZOiYiIiBwAC6tO2rRpE2bOnImXX34ZR48exf3334+xY8eivLzc3qkRERGRnXnYOwGlWbFiBaZMmYI//OEPAIC33noLO3fuxDvvvIMlS5bYObvOEwQBDQ0Nsj7G9fcv92N5e3tDpVLJ+hhKxvPtWni+XQvPt2NQCYIg2DsJpTAYDPD19cUnn3yChx9+WDz+wgsvoKioCHv37m3zb/R6PfR6vXi7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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Year',y='BasePay',data=sal)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BDXkr71ehCGl"
   },
   "source": [
    "**Q10: Create a histogram for TotalPay variable. Which of the following statement is NOT true?** \n",
    "\n",
    "##### code for reference \n",
    "sns.histplot(sal['variable name here'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "id": "jdepTsdJhCGl"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='TotalPay', ylabel='Count'>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Zltf15U+aF3TXn131Jh/TC7097+TefPmaf/+/dq5c2ebffRf+4YOHaqysjLV1NTo1Vdf1T333KOSkhJrP/3WvmPHjunhhx/W9u3bFR4efs46+q99U6ZMsf55xIgRyszM1Ne+9jVt2LBBo0aNardd9F1gYITIT+Lj49WvX782KbyqqqpNYu+rWlZedNQHLpdLTU1Nqq6u7rDmxIkTbY5/8uRJn5rW31NdXa3Tp093WFNVVSWp7d/oetL8+fP12muv6a233tKVV15pbaf/OhYaGqohQ4bopptuUn5+vq677jo999xz9Nt5lJaWqqqqSunp6QoODlZwcLBKSkr0i1/8QsHBweccQaD/2te/f3+NGDFCH3/8Mf/tBTgCkZ+EhoYqPT1dxcXFPtuLi4s1evRoP7WqZw0ePFgul8unD5qamlRSUmL1QXp6ukJCQnxq3G63ysvLrZrMzEx5PB7t3bvXqnn33Xfl8Xh8asrLy+V2u62a7du3KywsTOnp6VbN22+/7bMsdfv27UpOTtagQYO6vwPOwxijefPmacuWLXrzzTc1ePBgn/30X+cYY9TY2Ei/nce4ceN04MABlZWVWa+bbrpJd999t8rKynT11VfTf53Q2NioQ4cOKSkpif/2Al2PTN1Gu1qW3a9bt858+OGHJicnx/Tv3998+umn/m5at6mrqzMffPCB+eCDD4wks2zZMvPBBx9YtxZ45plnjNPpNFu2bDEHDhww3/ve99pdgnrllVeaHTt2mPfff99885vfbHcJ6siRI83u3bvN7t27zYgRI9pdgjpu3Djz/vvvmx07dpgrr7zSZwlqTU2NSUxMNN/73vfMgQMHzJYtW0x0dLTflqA++OCDxul0mj/96U8+S3j//ve/WzX0X/sWL15s3n77bXPkyBGzf/9+8/jjj5ugoCCzfft2Ywz91llnrzIzhv7ryMKFC82f/vQn88knn5g9e/aYrKwsExUVZf25Tt8FLgKRnz3//PNm4MCBJjQ01Nx4443Wkuq+4q233jKS2rzuueceY8yZZahPPvmkcblcJiwszHzjG98wBw4c8DlGQ0ODmTdvnomNjTUREREmKyvLHD161Kfmiy++MHfffbeJiooyUVFR5u677zbV1dU+NZ999pm5/fbbTUREhImNjTXz5s3zWW5qjDH79+83X//6101YWJhxuVwmNzfXb8tP2+s3SaagoMCqof/a94Mf/MD6/+qKK64w48aNs8KQMfRbZ7UORPTfubXcVygkJMQkJyeb6dOnm4MHD1r76bvA5TDGrrekBAAAOIM5RAAAwPYIRAAAwPYIRAAAwPYIRAAAwPYIRAAAwPYIRAAAwPYIRAAAwPYIRAAAwPYIRADwD4MGDdKKFSv83QwAfkAgAhBwHA5Hh6977733vJ//7W9/e9HtGDRokPWdkZGRSktL05o1ay76uAACT7C/GwAArZ39hO5XXnlFP/3pT3X48GFrW0RERI+15amnntLs2bNVX1+v9evX64EHHtDll1+u7373uz3WBgCXHiNEAAKOy+WyXk6nUw6Hw2fb5s2b9bWvfU2hoaEaOnSoXn75ZeuzgwYNkiR9+9vflsPhsN7/3//9n+644w4lJibqsssu080336wdO3acty1RUVFyuVwaMmSIfv7znys1NdUafXrsscd0zTXXKDIyUldffbWeeOIJnT59WpL06aefKigoSO+9957P8VauXKmBAweKx0gCgYVABKBX2bp1qx5++GEtXLhQ5eXlmjNnju677z699dZbkqR9+/ZJkgoKCuR2u6339fX1+ta3vqUdO3bogw8+0KRJkzR16lQdPXq0U98fHh5uhZ6oqCitX79eH374oZ577jmtXbtWy5cvl3QmmI0fP14FBQU+ny8oKNC9994rh8NxUf0AoJsZAAhgBQUFxul0Wu9Hjx5tZs+e7VPzne98x3zrW9+y3ksyW7duPe+xhw8fblauXGm9HzhwoFm+fHm770+fPm0KCgqMJPPCCy+0e7ylS5ea9PR06/0rr7xiYmJizKlTp4wxxpSVlRmHw2GOHDly3rYB6FmMEAHoVQ4dOqRbbrnFZ9stt9yiQ4cOdfi5L7/8Uo8++qiGDx+uyy+/XJdddpk++uij844QPfbYY7rssssUERGhuXPn6sc//rHmzJkjSfqv//ov3XrrrXK5XLrsssv0xBNP+BzvzjvvVHBwsLZu3SpJ+tWvfqXbbrvNuowHIHAQiAD0Oq0vNxljznsJ6sc//rFeffVVPf3003rnnXdUVlamESNGqKmp6byfKysr02effab6+notXbpUQUFB2rNnj+666y5NmTJFv//97/XBBx9oyZIlPscLDQ1Vdna2CgoK1NTUpM2bN+sHP/hB108cwCXDKjMAvcqwYcO0c+dO/fu//7u1bdeuXRo2bJj1PiQkRM3NzT6fe+edd3Tvvffq29/+tqQzc4o+/fTT835ffHy8hgwZ0mb7n//8Zw0cOFBLliyxtn322Wdt6n74wx8qLS1NL7zwgk6fPq3p06ef9zsB9DwCEYBe5cc//rFmzJihG2+8UePGjdPvfvc7bdmyxWfF2KBBg/TGG2/olltuUVhYmGJiYjRkyBBt2bJFU6dOlcPh0BNPPCGv19vldgwZMkRHjx5VYWGhbr75Zv3hD3+wLo2dbdiwYRo1apQee+wx/eAHP+jRWwYAuHBcMgPQq9x555167rnn9B//8R+69tprtWbNGhUUFGjs2LFWzbPPPqvi4mKlpKTohhtukCQtX75cMTExGj16tKZOnapJkybpxhtv7HI77rjjDv3oRz/SvHnzdP3112vXrl164okn2q2dNWuWmpqauFwGBDCHMdwMAwAupaefflqFhYU6cOCAv5sC4BwYIQKAS6S+vl779u3TypUrtWDBAn83B0AHCEQAcInMmzdPt956q8aMGcPlMiDAcckMAADYHiNEAADA9ghEAADA9ghEAADA9ghEAADA9ghEAADA9ghEAADA9ghEAADA9ghEAADA9v4/B647lq9kSR4AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(sal['TotalPay'])"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "name": "Week 1 Exercise_SF Salaries Student Version.ipynb",
   "provenance": [],
   "toc_visible": true
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
